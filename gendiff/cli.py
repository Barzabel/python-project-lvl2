import argparse


def get_args():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', default="stylish", help="-f FORMAT, \
    --format FORMAT set format of output")
    return parser.parse_args()
