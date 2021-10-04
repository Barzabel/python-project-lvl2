import argparse


parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)

parser.add_argument('-f', '--format', action='store_true', 
    help="-f FORMAT, --format FORMAT set format of output")


args = parser.parse_args()

def main():
    pass


if __name__ == "__main__":
	main()
