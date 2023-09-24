from gendiff.gendiff import generate_diff
import argparse
from gendiff.arg_pars_for_gendiff import ArgparseForGendiff


args = ArgparseForGendiff().get_args()


parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)

parser.add_argument('-f', '--format', default="stylish", help="-f FORMAT, \
    --format FORMAT set format of output")
args = parser.parse_args()


def main():
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
