from gendiff.gendiff import generate_diff
from gendiff.cli import get_args


args = get_args()


def main():
    print(generate_diff(
        args['first_file'],
        args['second_file'],
        args['formator']))


if __name__ == '__main__':
    main()
