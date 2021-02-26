import boto3


def update_network_acl_ip(network_acl_id, rule_number, new_ip_address):
    """ Replace IP address related to the rule_number with the new IP address"""
    print(f"Replace entry which the rule number is '{rule_number}'' with new IP: {new_ip_address}")
    client = boto3.client('ec2')
    client.replace_network_acl_entry(
        CidrBlock=f"{new_ip_address}/32",
        NetworkAclId=network_acl_id,
        Egress=False,
        Protocol='-1',
        RuleAction='allow',
        RuleNumber=rule_number
    )
    # response = client.describe_network_acls(NetworkAclIds=[
    #     network_acl_id,
    # ])
    # print(f"RESPONSE AFTER={response}")


def remove_ip(security_group, cidr, port, description):
    security_group.revoke_ingress(
        DryRun=False,
        GroupName=security_group.group_name,
        IpPermissions=[
            {
                'FromPort': port,
                'IpProtocol': 'TCP',
                'IpRanges': [
                    {
                        'CidrIp': cidr,
                        'Description': description
                    }
                ],
                'ToPort': port
            }])


def get_ip_from_description(security_group, description):
    client = boto3.client('ec2')
    response = client.describe_security_groups(
        GroupNames=[
            security_group.group_name
        ],
        DryRun=False
    )
    ip_ranges = response['SecurityGroups'][0]['IpPermissions'][0]['IpRanges']
    cidr = [ip_entry['CidrIp']
            for ip_entry in ip_ranges if ip_entry['Description'] == description]
    print(f"Old IP address associated to the description '{description}':{cidr}")
    return cidr[0]


def replace_ip_with_desc_into_security_group(security_group, myip, port, description):
    security_group.authorize_ingress(
        GroupName=security_group.group_name,
        IpPermissions=[
            {
                'FromPort': port,
                'IpProtocol': 'TCP',
                'IpRanges': [
                    {
                        'CidrIp': f"{myip}/32",
                        'Description': f"{description}"
                    },
                ],
                'ToPort': port,
            },
        ],
        DryRun=False
    )
