#comments in python are started with a #.
#testing out the print statements.

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
#this is the St. Potatosburg city population below.
city_pop = 340000

print ("The City of " + (city_name), "has a population of : ", + (city_pop))
#comments of the code can be added and used for description of the code to benefit the next programmer who may interact with the code.

# NUMBERS 

#integers are numbers, whole numbers and numbers can be given to variables as values. 

int1 = 1
print (int1)
int2 = 2
print (int2)
int3 = 3
print (int3)

#float refers to numbers which have decimal points and or remainders. floats can also be placed as values to variables.
float1 = 1.1
print (float1)
float2 = 2.2
print (float2)
float3 = 3.3
print (float3)

#float can also be referred to via the scientific notation using "e".
#this evaluates to 150.0
float4 = 1.5e2
print (float4)

cucumbers = 40
print("cucumbers", + cucumbers)

price_per_cucumber = 3.25
print("price per cucumber", +  price_per_cucumber)

total_cost = cucumbers * price_per_cucumber
print("total cost", total_cost)

# FLOAT CONTINUED...
#To yield a float as the result instead, programmers often change either the numerator or the denominator (or both) to be a float:
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
