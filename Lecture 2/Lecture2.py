
# While loop
# it is going to repeat a certain condition is met and then it stops

# Fibonacci series
a, b = 0, 1
while b < 50:
    print(b, end =',') 
    a,b = b, a + b

print()
prev = 0
current = 1
while current < 50:
    print(current, end=',')
    temp = current
    current = prev + current
    prev = temp

# # Infinite loop
# while 1:
#     print('a')

#################################

# If statement

a = 9

print() 
print("a is", end=' ')
if a%2 == 0:
    print("even number")
else: 
    print("odd number")    


# Relational operators
# == equal to
# != not equal to
# < less than
# > greater than 
# <= less than or equal (leq)
# >= greater than or equal (geq)

print(8 == 8)
print(1 == 2 )
print(True == 1)
print(False == 0)

var = None

# The proper way to test if a variable is None
if var is None:
    print("The variable is None!")

# This None trick can be used in astronomical observations when sometimes there are no values

# Combining conditions - airline ticket pricing
age = 2

if age <= 2:
    print("Free fare")
elif (age > 2) and (age < 12):
    print("50% off")

else:
    print("Full fare")

# Logical operators:
# and, or, ^ (xor), not
# xor means on or the other but not together

# Testing strings
test_str = "It is not safe to go alone. Take this!"

if "safe" in test_str:
    print("Thanks!")

test_list = [1, 2, 3.14, 4]

if 3.14 in test_list:
    print(test_list)


# List as condition
test_list = [5]
if test_list:
    print("The list is not empty")
else:
    print("The list is empty")

test_list = []
if len(test_list) > 0:
    print("The list is not empty")
else:
    print("The list is empty")


# Find a number that is divisible by 2,3 and 7 at the same time

x = 1
while x < 100:

    if (x%2 == 0) and (x%3 == 0) and (x%7 == 0):
        print(x)
        break

    x += 1

# Leap years from 1990 to 2030
x = 1990
while x <= 2030:

    x +=1
    
    #these are the conditions of a leap year
    if ((x%4 == 0) and (x%100 != 0)) or (x%400 == 0):
        print(x, "leap")
        continue
    print(x)

# For loop

# First 50 numbers in the Fibonacci sequence

a, b = 0,1
for i in range(50):
    print(b, end=',')
    a, b = b, a + b

cities = ["New York", "Paris", "Peckham"]
print()
for city in cities:
    print(city)

for i, city in enumerate(cities):
    print(i, city)

countries = ["USA", "France", "UK"]
for country, city in zip(countries, cities):
    print(country, city)

#################################

# Reading files
file_name = "data.txt"

# opening a file in the read mode
with open(file_name, 'r') as f:

    print(f.closed)
    print(f.readline())
print(f.closed)

# reading the file line by line 
with open(file_name) as f:
    for line in f:
        print(line)


a = 'one,two,three,four'
print(a.split(','))

b = "    center   "
print(b.strip())

# Printing the file contents as a list
with open(file_name) as f:

    for line in f:

        # Remove the newline char
        line = line.replace('\n', '')

        # Split the line into a list
        line = line.split(',')

        print(line)






