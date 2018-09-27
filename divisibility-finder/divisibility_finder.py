#!/usr/local/bin/python3
import argparse
from lib.Validator import ValidationProcessing
from lib.Division import DivisionProcessing


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--number', required=True, type=int, help="--number NUMBER")
	args = parser.parse_args()
	vp = ValidationProcessing(vars(args))
	if not vp.is_positive():
		print("Number is not positive")
		exit()
	dp = DivisionProcessing()
	if dp.checkDivisibleByThree(vp.number):
		print("Divisible by 3")
	else:
		print("Not Divisible by 3")


#  This is main
if __name__ == "__main__":
    main()