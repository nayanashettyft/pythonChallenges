
import argparse
#from ...leapyearfinder.leapyear import Validator 

class FibSum:
	def __init__(self, args):
		for name,value in args.items():
			setattr(self, name, value)
		print(self.number) 


	def fibR(n):
		if n==0:
			return 0
		elif n==1:
			return 1
		else:
			return fibR(n-1)+fibR(n-2)


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--number', required=True, type=int, help="--number Valid number")
	args = parser.parse_args()
	fib_sum = FibSum(vars(args))
	print(fib_sum.fibR())
	#validator = Validator(vars(args))
	#if (validator.isPositiveDigit()):
	#	fib_sum = LeapYearFinder(vars(args))
	#	print("Sum: {}".format(fib_sum))
	#else:
	#	print ("Not a valid input")


if __name__ == "__main__":
	main()