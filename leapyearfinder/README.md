# Leap Year Finder
This program is meant to find if an input from a user is a leap year or not.

### Usage
```
python leapyear.py --year ValidYear
```
Use -- help for usage details
```
python leapyear.py --help 
```

### Pre-requisites
Make sure you are running python3

### Tests scenarios:

* input = 1804 - It is a leap year
* input = 2000 - it is not a leap year
* input = 1903 - It is not a leap year
* input = 0 - ?
* input = -100 - it is not a year
* input = 345678980011 -
* input = "Two Thousand"
* input = "10-12-2015"
* input = ""

### Our Learnings:
- Use main() to start the function which gives us the ability to run modules in the code without actually running code in main()
```
def main():
	code code code

if __name__ == "__main__":
    main()
```
- Use argparse to get arguments from users. This give user the explicit help option
```
import argparse
	parser = argparse.ArgumentParser()
    parser.add_argument('--year', required=True, type=int, help="--year YEAR")
    args = parser.parse_args()
```

