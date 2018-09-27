#!/usr/local/bin/python3
import argparse

class ValidationProcessing:
	def __init__(self, args):
		for k,v in args.items():
			setattr(self, k, v)


class DivisionProcessing:
    def __init__(self):
        pass


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--number', required=True, type=int, help="--number NUMBER")
	args = parser.parse_args()
	vp = ValidationProcessing(vars(args))


#  This is main
if __name__ == "__main__":
    main()