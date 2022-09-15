import glob
import argparse
import importlib
import helpers.online
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--version', help='Show program version', action='store_true')
subparsers = parser.add_subparsers(
    title='Commands',
)

modules = list(Path.cwd().joinpath(__file__).resolve().parent.joinpath('namespace').glob('*.py'))
for file in modules:
    module = importlib.import_module('namespace.' + file.name.replace('.py', ''))
    module.add_args(subparsers)

args = parser.parse_args()

if args.version:
    print('v1.0.0')

if hasattr(args, 'func'):
    args.func(args)
else:
    parser.print_help()
