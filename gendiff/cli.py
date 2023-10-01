import argparse


def get_args():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', default="stylish", help="-f FORMAT, \
    --format FORMAT set format of output")
    args = parser.parse_args()
    return {
        'first_file': args.first_file,
        'second_file': args.second_file,
        'formator': args.format
    }