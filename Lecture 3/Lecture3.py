

file_name = 'data.txt'

data_list = []

with open(file_name) as f:

    # Skip the header
    next(f)

    for line in f:

        # Strip the newline character from the end
        line = line.replace("\n", "")

        # Split the line by a comma
        line = line.split(",")

        # Parse the line
        num = line[0]
        name = line[1].strip()
        epoch = int(line[2])
        elements = list(map(float, line[3:9]))
        ref = line[9]

        data_list.append([num, name, epoch, elements, ref])

print(data_list)

# Wile E. Coyote rewrites history...
for line in data_list:
    line[1] = 'Coyote'

print(data_list)

# Converting floats to strings
x = 3.14159

print('{:8.2f}'.format(x))

# Signed formatting
print('{:06.2f}'.format(x))

# More decimals
print('{:7.5f}'.format(x))

y = 2.71
print("{:7.5f}".format(y))
print("{:7.2f}".format(y))

# Integers
z = 42
print("{:7d}".format(z))

# Strings - always left aligned
print("{:10}".format('wile e'))
print("{:>10}".format('wile e'))

# Named argument
print("{a} {b} {c}".format(a=5, b=8, c=10))

print("Pi is {:4.2f}".format(x))

####################################

# Writing files
new_file_name = "true_data.txt"

with open(new_file_name, 'w') as f:

    # Write the header
    f.write("Num,Name,Epoch,q,e,i,w,Node,Tp,Ref\n")

    for line in data_list:

        # Compose a line string
        str_line = ["{:>5}".format(line[0]), "{:16s}".format(line[1]), "{:6d}".format(line[2])]

        for element in line[3]:
            str_line.append("{:7.3f}".format(element))

        str_line.append(line[-1])
        
        print(str_line)

        final_line = ",".join(str_line)

        # Write the line
        f.write(final_line + "\n")

# Appending to a file

with open(new_file_name, 'a') as f:
    f.write("Wile E. was here")


######################################

import math

print(math.sqrt(2))

print(math.sin(math.pi))

print(math.log10(100))

import random

print(random.randint(1, 100))

print(random.random()*5)

# List shuffling
a = [1, 2, 3, 4]
random.shuffle(a)
print(a)

# Sampling
b = list(range(1, 100))
print(random.sample(b, 10))

# Sampling a gaussian distribution
for i in range(10):
    print(random.gauss(0, 2))

#####################

# Ways of importing modules

# Module alias
import math as m

print(m.sqrt(2))

# Importing indivudal functions
from math import sqrt
print(sqrt(2))

# Don't do this!
from math import *
print(cos(pi))
print(sin(tan(pi/2)))

########################################

import os

# Get the contents of the current directory
print(os.listdir("."))

# Print the current directory path (cwd= current working directory)
print(os.getcwd())

print(os.sep)

# Construct a path to a new directory
new_dir_path = os.path.join(os.getcwd(), "test")
print(new_dir_path)

# Make a new directory
if not os.path.exists(new_dir_path):
    os.mkdir(new_dir_path)
    print("Make a new dir!")

else:
    print("The new dir already exists!")

file_name = "top_secret.txt"
file_path = os.path.join(new_dir_path, file_name)
with open(file_path, 'w') as f:
    pass

# Deleting a file
if os.path.isfile(file_path):
    os.remove(file_path)
else:
    print("The file does not exist!")

#####################################

import shutil

# Make the example file again
with open(file_path, 'w') as f:
    pass

# Copy the file
copy_path = "unclassified.txt"
shutil.copy2(file_path, copy_path)

# Move/rename the file
new_name = "public_release.txt"
shutil.move(copy_path, new_name)

