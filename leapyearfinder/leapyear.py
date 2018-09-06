import argparse

class Validator:
    def __init__(self, args):
        for name,value in args.items():
            setattr(self, name, value)
        print(self.year) 
    
    def isPositiveDigit(self):
        return 1 if int(self.year) > 0 else 0

class LeapYearFinder:
    def __init__(self, args):
        for name,value in args.items():
            setattr(self, name, value)
        print(self.year) 

    def is_a_leap_year(self):
        return self.is_divisible_by_four_hundred() or (self.is_not_divisible_by_one_hundred() and self.is_divisible_by_four())
    
    def is_divisible_by_four(self):
        return self.year % 4 == 0
    
    def is_not_divisible_by_one_hundred(self):
        return self.year % 100 != 0
    
    def is_divisible_by_four_hundred(self):
        return self.year % 400 == 0
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--year', required=True, type=int, help="--year YEAR")
    args = parser.parse_args()
    validator = Validator(vars(args))
    if (validator.isPositiveDigit()):
        leapyearfinder = LeapYearFinder(vars(args))
        if (leapyearfinder.is_a_leap_year()):
            print ("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print ("Not a valid year")


if __name__ == "__main__":
    main()