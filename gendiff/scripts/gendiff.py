from gendiff.gendiff import generate_diff
from gendiff.arg_pars_for_gendiff import ArgparseForGendiff


args = ArgparseForGendiff().get_args()


def main():
    print(generate_diff(
        args['first_file'],
        args['second_file'],
        args['formator']))
    print(generate_diff(
        args['first_file'],
        args['second_file'],
        args['formator']))

if __name__ == '__main__':
    main()
