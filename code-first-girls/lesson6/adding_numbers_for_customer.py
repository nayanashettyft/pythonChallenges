# Build an app that adds numbers 1 and 2 everytime before you print a statment

# version 1
sum = 1 + 2
print("Sum of 1 and 2 is {}.".format(sum))

print("Hello! This is Statement 1")

sum = 1 + 2
print("Sum of 1 and 2 is {}.".format(sum))

print("How are you! This is Statement 2")

sum = 1 + 2
print("Sum of 1 and 2 is {}.".format(sum))

print("Bye! This is Statement 3")

print("")

# version 2
# Oh but now I would like the app to add 3 and 4

# Lets create a function
def add_3_and_4():
    sum = 3 + 4
    print("Sum of 3 and 4 is {}.".format(sum))

add_3_and_4()
print("Hello! This is Statement 1") # Calling this function
add_3_and_4()
print("How are you! This is Statement 2")
add_3_and_4()
print("Bye! This is Statement 3")
print("")

# version 3
# Oh but now I want to be able to add 2 unique numbers everytime

# Lets use arguments in a function
def calculate_sum(number1, number2):
    sum = number1 + number2
    print("Sum of {0} and {1} is {2}.".format(number1, number2, sum))

calculate_sum(1,2)
print("Hello! This is Statement 1")
calculate_sum(3,4)
print("How are you! This is Statement 2")
calculate_sum(7,9)
print("Bye! This is Statement 3")
print("")

# version 4
# Can we add the sum of the 2 numbers at the end of each statement Please

# Lets return the results out of the function
def calculate_sum(number1, number2):
    sum = number1 + number2
    print("Sum of {0} and {1} is {2}.".format(number1, number2, sum))
    return sum

sum_returned = calculate_sum(1,2)
print("Hello! This is Statement 1 {}".format(sum_returned))
sum_returned = calculate_sum(3,4)
print("How are you! This is Statement 2 {}".format(sum_returned))
sum_returned = calculate_sum(7,9)
print("Bye! This is Statement 3 {}".format(sum_returned))
print("")

# version 5
# Oh can we now change this statement to take a name from the user and print that in the statement rather than "This is Statement x"

# Lets take inputs from users
def calculate_sum(number1, number2):
    sum = number1 + number2
    print("Sum of {0} and {1} is {2}.".format(number1, number2, sum))

print("Please enter your name:")
name = input()
calculate_sum(1,2)
print("Hello! {}".format(name))
calculate_sum(3,4)
print("How are you! {}".format(name))
calculate_sum(7,9)
print("Bye! {}".format(name))
print("")
