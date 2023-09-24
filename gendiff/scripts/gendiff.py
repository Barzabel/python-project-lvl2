from gendiff.gendiff import generate_diff
from gendiff.arg_pars_for_gendiff import ArgparseForGendiff


args = ArgparseForGendiff()


def main():
    print(args['formator'])
    print(generate_diff(args['first_file'], args['second_file'], args['formator'])


if __name__ == '__main__':
    main()
