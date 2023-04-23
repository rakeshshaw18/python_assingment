#QUESTION 1:- Find the data type of these two declarations:
x=5
y='John'
print(type(x))
print(type(y))

#QUESTION 2:- Check whether the following syntax is valid or invalid for naming a variable. : Example: abc=100 #valid syntax

# #3a=10  #Invalid Syntax
# @abc=10 # Invalid Syntax
# a100=100 #Valid Syntax
# a984_=100 #Valid Syntax
# a9967$=100 #Invalid Syntax
# xyz-2=100 #Invalid Syntax


# QUESTION 3:- Check if element exists in list in Python:
# test_list=[1,6,3,5,3,4]
# Check if 3 exist or not.
# Check if 9 exists or not.

test_list=[1,6,3,5,3,4]

if 3 in test_list:
    print("3 in test_list")
else:
    print("3 is not in test_list")

test_list=[1,6,3,5,3,4]
if 9 in test_list:
    print("9 is in test_list")
else:
    print("9 is not in test_list")


#QUESTION 4:- Take the user input to print the current date
from datetime import date
today = date.today()
print("Today date is: ", today)

# QUESTION 5:- What is the out put of the following code:
# a.print 9//2
# b.print 9%2
print(9//2)
print(9%2)

# QUESTION 6:- Print First 10 natural numbers using a while loop?
i = 1
while(i<=10):
    print(i)
    i += 1

# QUESTION 7:- Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number
# For example, If the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)

n = int(input("Enter a number: "))
s = 0
for i in range(n + 1):
   s += i
print("The sum of all numbers from 1 to the given number is: ", s)

# QUESTION 8:- Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

for FizzBuzz in range(51):
    if FizzBuzz % 3 == 0 and FizzBuzz % 5 == 0:
        print("FizzBuzz")
        continue
    elif FizzBuzz % 3 == 0:
        print("Fizz")
        continue
    elif FizzBuzz % 5 == 0:
        print("Buzz")
        continue
    print(FizzBuzz)
