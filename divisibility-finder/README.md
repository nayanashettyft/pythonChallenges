# Divisibility Finder
This program is meant to find if an input from a user is divisible by 3 or not.

### Usage
```
python divisibility-finder.py --number {NUMBER}
```
Use -- help for usage details
```
python divisibility-finder.py --help 
```

### Pre-requisites
Make sure you are running python3

### Tests scenarios:

* input = 1 - Not Divisible by 3
* input = 3 - Divisible by 3
* input = 5 - Not Divisible by 3
* input = 8 - Not Divisible by 3
* input = 9 - Divisible by 3
* input = 10 - Not Divisible by 3
* input = 123456789 - Not Divisible by 3
* input = 36396363 - Divisible by 3
* input = 0 - Number is not positive
* input = -10 - Number is not positive
* input = "Two Thousand" - Error
* input = "123?" - Error
* input = "" - help shown