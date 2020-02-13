#comments in python are started with a #.
#testing out the print statements.
# Note the () around many of the PRINT statements are only there to ensure they work in this code editor.
# Else the () would not be needed especially where you see them doubled up.

# PRINT STATEMENTS

print ("Hello World!")
print ("My Name is Miles Lacek")
print ("I am 30 years old and I love to bike")
# expected results in terminal is the print statements to read as they are above. CHECK.
# python 2 and python 3 are similar but syntax for python 3 uses parantheses.

# CONCATENATION 
print ("Miles" + "Lacek") # joins the two strings together without space.
print ("Miles " + "Lacek") # joins the two strings BUT has a space after the first string with a space after "Miles ". 

# VARIABLES
todays_date = "January 29th" # todays_date has been given the value of the string.
print (todays_date) # as expected in the terminal we see the value for the variable.

# ARITHAMATIC
one_addition = 1 + 1
print("this is addition", one_addition)

two_subtraction = 2 - 1
print("this is subtraction", two_subtraction)

three_multiplication = 3 * 1
print("this is multiplication", three_multiplication)

remainder = 1398 % 11
print("this is the remainder", remainder)

product = 2 * 2
print("this is the product", product)

# UPDATING VARIABLES
january_to_june_rainfall = 1.93 + 0.71 + 3.53 + 3.41 + 3.69 + 4.50
annual_rainfall = january_to_june_rainfall

july_rainfall = 1.05
annual_rainfall += july_rainfall

august_rainfall = 4.91
annual_rainfall += august_rainfall

september_rainfall = 5.16
annual_rainfall += september_rainfall

october_rainfall = 7.20
annual_rainfall += october_rainfall

november_rainfall = 5.06
annual_rainfall += november_rainfall

december_rainfall = 4.06
annual_rainfall += december_rainfall

print (round(annual_rainfall))
# round is a python command that rounds the numeric value of any variable or number down.

# COMMENTS 
city_name = ("St. Potatosburg")
# this is the St. Potatosburg city population below.
city_pop = 340000

print ("The City of " + (city_name), "has a population of : ", + (city_pop))
# comments of the code can be added and used for description of the code to benefit the next
# programmer who may interact with the code.

# NUMBERS 

# integers are numbers, whole numbers and numbers can be given to variables as values. 

int1 = 1
print (int1)
int2 = 2
print (int2)
int3 = 3
print (int3)

# float refers to numbers which have decimal points and or remainders. floats can also be placed as values to variables.
float1 = 1.1
print (float1)
float2 = 2.2
print (float2)
float3 = 3.3
print (float3)

# float can also be referred to via the scientific notation using "e".
# this evaluates to 150.0
float4 = 1.5e2
print (float4)

cucumbers = 40
print("cucumbers", + cucumbers)

price_per_cucumber = 3.25
print("price per cucumber", +  price_per_cucumber)

total_cost = cucumbers * price_per_cucumber
print("total cost", total_cost)

# FLOAT CONTINUED...
# To yield a float as the result instead, programmers often change either the numerator or 
# the denominator (or both) to be a float:
quotient1 = 7./2
# the value of quotient1 is 3.5
print(quotient1)

quotient2 = 7/2.
# the value of quotient2 is 3.5
print(quotient2)

quotient3 = 7./2.
# the value of quotient3 is 3.5
print(quotient3)

#An alternative way is to use the float() method:
quotient1 = float(7)/2
# the value of quotient1 is 3.5
print(quotient1)

cucumbers = 100
num_people = 6

whole_cucumbers_per_person = int(cucumbers / num_people)
print (whole_cucumbers_per_person)

float_cucumbers_per_person = float(cucumbers / num_people)
print (float_cucumbers_per_person)

# MULTI LINE STRINGS
haiku = """The old pond,
A frog jumps in:
Plop!"""

print (haiku)

#BOOLEANS 

# Hi! I'm Maria and I live in script.py.
# I'm an expert Python coder.
# I'm 21 years old and I plan to program cool stuff forever.

# created a boolean relationship for if Maria's age is 12 and it is not so it is False.
age_is_12 = False
print (age_is_12)

# created a boolean relationship for if Maria's name is Maria and it is true as a boolean.
name_is_maria = True
print (name_is_maria)

# VALUE ERROR
float_1 = 0.25
float_2 = 40.0

product = float_1 * float_2
print (product)

# printing out the product as a string with the float converted to an integer.
big_string = "The product was " + str(int(product))
print (big_string)

number1 = "100"
number2 = "10"

string_addition = number1 + number2
print (string_addition)
# string_addition now has a value of "10010"

int_addition = int(number1) + int(number2)
print (int_addition)
# int_addition has a value of 110

string_num = "7.5"
print (string_num)
print (float(string_num))


def cube(number):
  return number * number * number


cube(9)
print (cube(9))
# gives result of the cube function of 9 * 9 * 9 = 729
cube(3)
print (cube(3))
# gives result of the cube function of 3 * 3 * 3 = 27


def by_three(number):
  if number % 3 == 0:
    return cube(number)
  else:
    return False

# Don’t forget that if and else statements need a : at the end of #that line!


# testing the function to return a True value as it should due to #the logic that 
# 90 is divisible by 3 thus then the function calls #the cube function to run the cube of 90 = 729,000
by_three(90)
print (by_three(90))

# testing the function to return a False value, as it should and #does.
by_three(10)
print (by_three(10))

# GENERIC IMPORTS
# import math is importing a library of variables and functions already made in python
# to bring all those functions and variables to import a module such as math. It is called a generic import.

import math

print (math.sqrt(25))

print (math.sqrt(100))

print (math.sqrt(250))

# FUNCTION IMPORT
# to import only a certain function from and module is a function import and that is done with a keyword "from".

#from module import function

# looks like this for the same sqrt function from the math module.
from math import sqrt

# UNIVERSAL IMPORTS
# from module import * = from the module / library of funcitions import ALL.
# This way you don't have to continue to type out math. or whatever module you are working with.

# from math import * #UNCOMMENT THIS IF YOU WANT ALL OF THE FUNCTIONS FROM THE MODULE MATH

# Universal imports may look great on the surface, but they’re not a good idea for one very important reason: 
# they fill your program with a ton of variable and function names without the safety of those names 
# still being associated with the module(s) they came from.

# If you have a function of your very own named sqrt and you import math, 
# your function is safe: there is your sqrt and there is math.sqrt. 
# If you do from math import *, however, you have a problem: namely, 
# two different functions with the exact same name.

# Even if your own definitions don’t directly conflict with names from imported modules, 
# if you import * from several modules at once, you won’t be able to figure out which variable or 
# function came from where.

# For these reasons, it’s best to stick with either import module and type module.name or
# just import specific variables and functions from various modules as needed.

# To print every function from a module in this case specifically math: 
# TYPE import math # Imports the math module
# everything = dir(math)  # Sets everything to a list of things from math
# print everything  # Prints 'em all!

# RESULTS:

#['__doc__', '__name__', '__package__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2',
# 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1',
# 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'hypot', 'isinf', 'isnan', 
# 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 
# 'sqrt', 'tan', 'tanh', 'trunc']

# USING FUNCTIONS ALREADY WITHIN PYTHON 

def biggest_number(*args):
  print (max(args))
  return (max(args))
# Return the largest item in an iterable or the largest of two or more arguments.

# If one positional argument is provided, iterable must be a non-empty iterable 
# (such as a non-empty string, tuple or list). The largest item in the iterable is returned. 
# If two or more positional arguments are provided, the largest of the positional arguments is returned.

maximum = max(1, 2, 3, 4)
# associating maximum to an array of numbers and then running the
# max() function on the array so when maximum is printed it returns
# the highest number / integer / float from the array.
print (maximum)
# expecting 4 and got 4.

def smallest_number(*args):
  print (min(args))
  return (min(args))
# Return the smallest item in an iterable or the smallest of two or more arguments.

# If one positional argument is provided, iterable must be a non-empty iterable 
# (such as a non-empty string, tuple or list). The smallest item in the iterable is returned. 
# If two or more positional arguments are provided, the smallest of the positional arguments is returned.

minimum = min(1, 2, 3, 4)
# associating minimum to an array of numbers and then running the
# min() function on the array so when minimum is printed it returns
# the lowest number / integer / float from the array.

print (minimum)
# expecting 1 and got 1.

def distance_from_zero(arg):
  print (abs(arg))
  return (abs(arg))
# Return the absolute value of a number. The argument may be a plain or long integer or a floating point number.
# If the argument is a complex number, its magnitude is returned.

absolute = abs(-42)
# The abs() function returns the absolute value of the number it # # takes as an argument—that is, that number’s distance from 0 on an # imagined number line.
print (absolute)
# expected 42 got 42.

biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)

# Print out the types of an integer, a float,
# and a string on separate lines below.

# type() function returns the type of the data it receives as an # # argument.

print (type(42))
print (type(4.2))
print (type('spam'))

# FUNCTION PRACTICE with if and elif and else:

# First, def a function, shut_down, that takes one arguments.
# Don’t forget the parentheses or the colon!

# Then, if the shut_down function receives an s equal to "yes", it # should return "Shutting down"

# Alternatively, elif s is equal to "no", then the function should # return "Shutdown aborted".

# Finally, if shut_down gets anything other than those inputs, the
# function should return "Sorry"

# FUNCTION

def shut_down(s):
  if s == "yes":
    return "Shutting down"
  elif s == "no":
    return "Shutdown aborted"
  else:
    return "Sorry"

# TESTING FUNCTION

shut_down("yes")
print (shut_down("yes"))

shut_down("no")
print (shut_down("no"))

shut_down("maybe")
print (shut_down("maybe"))

# FUNCTION TWO 

# First, def a function called distance_from_zero, with one
# argument (choose any argument name you like).

# If the type of the argument is either int or float, the function # should return the abs()olute 
# value of the function input.

# Otherwise, the function should return "Nope".


def distance_away_from_zero(num):
  if type(num) == int or type(num) == float:
    return abs(num)
  else:
    return "Nope"

# TEST CASES FOR FUNCTION


distance_away_from_zero(3.0)
print (distance_away_from_zero(3.0))
# expected 3.0 received 3.0 as num is an float.

distance_away_from_zero(3)
print (distance_away_from_zero(3))
# expected 3 received 3 as num is an int.

distance_away_from_zero('Three')
print (distance_away_from_zero('Three'))
# expected 'Nope' received 'Nope' as string in NOT defined
# within the function for a result, so the else was executed.
