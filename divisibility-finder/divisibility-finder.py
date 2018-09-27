#!/usr/local/bin/python3
import argparse


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--number', required=True, type=int, help="--number NUMBER")
	args = parser.parse_args()
	print(vars(args))


#  This is main
if __name__ == "__main__":
    main()