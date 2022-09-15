import argparse
import importlib
import helpers.online
import namespace.cloud

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--version', help='Show program version', action='store_true')
subparsers = parser.add_subparsers(
    title='Commands',
)

namespace.cloud.add_args(subparsers)

args = parser.parse_args()

if args.version:
    print('v1.0.0')

if hasattr(args, 'func'):
    args.func(args)
else:
    parser.print_help()
