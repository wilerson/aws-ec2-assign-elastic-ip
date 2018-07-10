""" Command line parser """
import argparse
import sys
try:
    from ConfigParser import SafeConfigParser
except ImportError:
    from configparser import SafeConfigParser
from argparse import RawTextHelpFormatter

if sys.platform in ['win32', 'cygwin']:
    import ntpath as ospath
else:
    import os.path as ospath

SETTINGS = SafeConfigParser()
SETTINGS.read('{0}/settings.conf'.format(
    ospath.dirname(ospath.realpath(__file__))))

PARSER = argparse.ArgumentParser(
    description='Assign EC2 Elastic IP to the current instance',
    formatter_class=RawTextHelpFormatter)
PARSER.add_argument(
    '--version',
    action='count',
    help='Print the aws-ec2-assign-elastic-ip version and exit')
PARSER.add_argument(
    '--region',
    default='us-east-1',
    help='AWS region. Default: us-east-1')
PARSER.add_argument(
    '--access-key',
    help='AWS access key ID')
PARSER.add_argument(
    '--secret-key',
    help='AWS secret access key ID')
PARSER.add_argument(
    '--dry-run',
    action='store_true',
    help=(
        'Turn on dry run mode. No address will be assigned,\n'
        'we will only print which we whould take'))
PARSER.add_argument(
    '--valid-ips',
    help=(
        'A comma separated list of valid Elastic IPs.\nYou can use CIDR '
        'expressions to select ranges.\nValid examples:\n'
        '- 58.0.0.0/8\n'
        '- 123.213.0.0/16,58.0.0.0/8,195.234.023.0\n'
        '- 195.234.234.23,195.234.234.24\n'))
PARSER.add_argument(
    '--invalid-ips',
    help=(
        'A comma separated list of Elastic IP ranges that should not '
        'be used for assigning an ip. \n  You can use CIDR '
        'expressions to select ranges.\nValid examples:\n'
        '- 58.0.0.0/8\n'
        '- 123.213.0.0/16,58.0.0.0/8,195.234.023.0\n'
        '- 195.234.234.23,195.234.234.24\n'))
PARSER.add_argument(
    '--tags',
    help=(
        'A comma separated list of tags (in key:value format) that a valid '
        'EIP should have to be vaild to be used for assigning an ip.\n'
        'Valid examples:\n'
        '- ENV:STAGING\n'
        '- ENV:STAGING,NAME:FOO\n'))
ARGS = PARSER.parse_args()

if ARGS.version:
    print('AWS EC2 Assign Elastic IP: {0}'.format(
        SETTINGS.get('general', 'version')))
    sys.exit(0)
