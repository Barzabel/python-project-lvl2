from gendiff.gendiff import generate_diff
from gendiff.arg_pars_for_gendiff import ArgparseForGendiff


args = ArgparseForGendiff()


def main():
    print(*args.get_args().values())
    print(generate_diff(*args.get_args().values()))


if __name__ == '__main__':
    main()
