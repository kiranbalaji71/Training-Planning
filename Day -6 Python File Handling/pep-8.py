# PEP-8

# Indentation
# Use 4 spaces per indentation level
Var = 11
if(Var == 11):
    print('Var is equal to 11')

# Line length and Line break
# Limit all lines to a maximum of 79 characters
English_mark = Language_mark = Math_mark = chemistry_mark = physics_mark = 60
total_mark = (English_mark
              + Language_mark
              + Math_mark
              +(chemistry_mark + physics_mark))

# Blank lines
# Surround top-level function and class definitions with two blank lines
def area(l,w):
    def perimeter():
        return 2(l + w)
    return l * w

area(2,4)

# Imports
# It should usually be on separate lines
import os
import sys

# Whitespace
# Avoid extraneous whitespace
x = 4
y = 5
if x == 4: print(x, y); x, y = y, x

# Comments
# Comment and docstring line lengths are limited to 72 characters
# There are two type: Block and Inline Comment 