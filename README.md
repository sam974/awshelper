# awshelper

This repository provides helper to allow IP address from its domaine name.

Please ensure your AWS credentials are set: https://docs.aws.amazon.com/credref/latest/refdocs/file-location.html

## Usage

if you installed from wheel:
``
updateip  -d "yourdomainname" -f "<file_to_config>"
``

else:
``
python .\scripts\__main__.py  -d "yourdomainname" -f "<file_to_config>"
``

## File config format

Config format is described thanks to the sample file: aws-config-sample.json