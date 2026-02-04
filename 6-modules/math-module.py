""" What is a Module?

A module is a file that contains ready-made code (functions, variables).

Python already comes with many built-in modules.
math is one of them.

👉 Instead of writing math logic yourself, you import it. """

# importing the math module
import math
print(math.sqrt(16)) # 4.0 (4 * 4 = 16 )

# common math module functions
print(math.pow(2, 3)) # 2*2*2 = 8 

# rounding
print(math.floor(3.7)) # 3
print(math.ceil(3.2)) # 4

# absolute value
print(math.fabs(-5)) # 5.0

# constants
print(math.pi) # 3.141592653589793
print(math.e) # 2.718281828459045

# trigonometric Functions
print(math.sin(math.pi / 2)) # 1.0 
print(math.cos(0)) # 1.0

# importing specific functions (import only sqrt and pi)
from math import sqrt, pi

print(sqrt(25)) # 5*5 = 25 = 5
print(pi) # 3.141592653589793

# renaming a module (alias)
import math as m
print(m.sqrt(9)) # 3.0
print(m.pi) # 3.141592653589793
