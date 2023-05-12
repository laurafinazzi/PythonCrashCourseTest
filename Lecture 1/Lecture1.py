
# This is a comment

print("Hello, World!")

a = 15.9
b = 6

print("a =", a)
print("b =", b)

#using python as calculator

print('Addition:', a + b)
print('Subctraction:', a -b)
print('Multiplication:', a*b)
print('Division:', a/b)

print("Integer division:", a//b)
print("Modulo:", a%b) #useful when working with angles 

#Wrapping angles
print(( 265 + 180)%360)

print("a squared:", a**2)
print("a cubed:", a**3)
print("a^9:", a**9)

print("sqrt(2):", 2**(1/2))

#rounding

c = round(1.1/3, 4)
print(c)

# Swapping variable values
print("Before", a, b)
a, b = b, a
print("After:", a, b)

# Strings

name = "Monty Python"
title = "Holy Grail"

print(name)
print(title)

full_title = name + " and the " + title
print(full_title)

# First character
print(name[0]) # python is a 0 indexed programming language, unlike Matlab which is 1 indexed 

# Last character of variable name
print(name[-1])

# Ranges of chars
print(name[0:5])
print(name[6:])
print(title[:4])

# Every other charcter
print(name[::2])
print(name[1::2])
print(name[1:8:2])

print(title[:-1] + 'n')

# String length
print(len(name))

print("First line\nSecond line")

# Repeating the same string all over 
print("Hello! "*10)

# Count how many 'n' there are in the variable name
print(name.count('n'))

# Replacing
print(name.replace('o', 'a'))

##############################

x = "3.14"
y = float(x) # float is a number with a decimal point
z = int(y)

print(x, y, z)

#############################

# Lists!

apollo_moon = [11, 12, 14, 15, 16, 17]

print(apollo_moon)

apollo_commanders = ["Armstrong", "Conrad", "Shephard", "Young", "Cernan"]

print("Post-13 commanders:", apollo_commanders[2:])

apollo_commanders[0] = "Lovell"

print("If Neil got sick before the trip:", apollo_commanders)

# Appending an entry
apollo_moon.append(18)
apollo_moon.append(19)

print("Added cancelled missions:", apollo_moon)

# Removing the last entry
cancelled = apollo_moon.pop()

print(cancelled)
print(apollo_moon)

# Insert the failed Apollo 13
apollo_moon.insert(2, 13)
print(apollo_moon)

# Remove an entry by value
apollo_moon.remove(13)
print(apollo_moon)

# Remove by index
apollo_moon.pop(-1)
print(apollo_moon)

print("Index of Apollo 11:", apollo_moon.index(11))

print('Commander of Apollo 16:', apollo_commanders[apollo_moon.index(16)])

# Reverse a list in place
apollo_moon.reverse()
print(apollo_moon)

# Reverse without modifying
print("Back to normal:", apollo_moon[::-1])

# List unpacking
apollo12_crew = ["Pete", "Rick", "Al"]
commander, cm_pilot, lm_pilot = apollo12_crew
print(commander, cm_pilot, lm_pilot)

# 2D list
list2d = [[1, 2], [3, 4]]
print(list2d[0][1])

mission_details = [1969, 'Apollo 12', ['Conrad', 'Gordon', 'Bean'], 10.19194]

print(mission_details)

# How to print "Al Bean"

print(apollo12_crew[-1], mission_details[2][2])


ww2 = [1939, 1940, 1941, 1942, 1943, 1944, 1945]

# Convert every element into a string
ww2 = list(map(str,ww2))
print(ww2) # Now the integers are no longer numbers, they are strings

# Joining list members by a delimiter
print(", ".join(ww2)) 

##############

# Other lists operations

x = [1, 2, 20, 21, 22, 23, 1, 1]

print(sum(x)) # Get the sum of a list
print(max(x))
print(min(x))
print(x.count(1)) # Count how many times an item is on the list

# Sorting a list in place
x.sort()
print(x)

# Reversing a list
x.reverse()
print(x)

# Sorting a list in a descending order
print(list(reversed(sorted(x))))

################################

# Lists: shallow VS deep copy

a = [1, 2, 3, 4]


b = a

print(a, b)

a[0] = 100

print(a, b)

# Make a copy of a (deep copy)
b = list(a)

a[0] = 0

print(a, b)

