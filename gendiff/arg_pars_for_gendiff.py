import argparse


class ArgparseForGendiff:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Generate diff')
        self.parser.add_argument('first_file', type=str)
        self.parser.add_argument('second_file', type=str)
        self.parser.add_argument('-f', '--format', default="stylish", help="-f FORMAT, \
    --format FORMAT set format of output")

    def get_args(self):
        args = self.parser.parse_args()
        return {
            'first_file': args.first_file,
            'second_file': args.first_file,
            'formator': args.format
        }
