import sys
import socket
import traceback
import json
import argparse

import args_init
import boto3
import vpc_helper


def main():
    """Main function of program."""
    if sys.version_info < (3, 5):
        print("This program requires Python 3.5 or above")
        sys.exit(1)

    try:
        args = args_init.argparse_init()
        if args is None:
            sys.exit(1)
    except argparse.ArgumentError as exc:
        print(exc.message, '\n', exc.argument)
        sys.exit(1)

    try:
        ip_address = None
        if args.domain_name:
            print(f"Domain:{args.domain_name} ---> {socket.gethostbyname(args.domain_name)}")
            ip_address = socket.gethostbyname(args.domain_name)
        if args.ip_address:
            ip_address = args.ip_address
        
        if not ip_address:
            raise Exception("Either domain name or IP address must be given.")
        
        print(f"Update the IP based on the config file: {args.file}")
        vpc_cfg = json.load(open(args.file))

        vpc_helper.update_network_acl_ip(vpc_cfg["network-acl-id"], vpc_cfg["rule-number"], ip_address)
        ec2 = boto3.resource('ec2')
        for group in vpc_cfg["security-groups"]:
            print(f"ID={group['security-group-id']}#desc={group['description']}#port={group['port']}")
            security_group = ec2.SecurityGroup(group['security-group-id'])
            wanted_desc = group['description']
            allowed_port = group['port']
            try:
                old_ip_address = vpc_helper.get_ip_from_description(security_group, wanted_desc)
                vpc_helper.remove_ip(security_group, old_ip_address, allowed_port, wanted_desc)
            except Exception:
                print(f"No IP address matching the description: {wanted_desc}")
                print(traceback.format_exc())
            vpc_helper.replace_ip_with_desc_into_security_group(security_group, ip_address, allowed_port, wanted_desc)

    except Exception as e:
        print(traceback.format_exc())


if __name__ == "__main__":
    main()
