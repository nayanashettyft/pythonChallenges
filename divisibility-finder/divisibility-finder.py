#!/usr/local/bin/python3
import argparse

class ValidationProcessing:
	def __init__(self, args):
		for k,v in args.items():
			setattr(self, k, v)

	def is_positive(self):
		if self.number > 0:
			return True
		else:
			return False

class DivisionProcessing:
    def __init__(self):
        pass


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--number', required=True, type=int, help="--number NUMBER")
	args = parser.parse_args()
	vp = ValidationProcessing(vars(args))
	if not vp.is_positive():
		print("Number is not positive")
		exit()
	dp = DivisionProcessing()


#  This is main
if __name__ == "__main__":
    main()