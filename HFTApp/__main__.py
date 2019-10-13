import argparse
parser = argparse.ArgumentParser()

parser.add_argument('-H', '--host', nargs='+', help="Output Host", required=True)
parser.add_argument('-l', '--log-level', default="INFO", help="Log output level.",required=False)

args = parser.parse_args()

print(args)

from HFTApp.extensions import logger
logger = logger.setLevel(args.l.upper())