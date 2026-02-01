""" What is a Function?

A function is a reusable block of code.

Instead of writing the same code again and again, you:

write it once

call it whenever you need it

Think of it like a machine:

you give it input

it does something

it may give you output """

# defining a function
def say_hello():
  print("Hello!")

say_hello() # Hello!

# function with Parameters!
def greet(name):
  print("Hello", name)
  
greet("Erkan") # Hello Erkan
greet("Python") # Hello Python

# function with return value
def add(a, b):
  return a + b
result = add(3, 5)
print(result) # 8

# why return is important (withouth return the function returns none)
def square(x):
  return x * x
print(square(4)) # 16 

# default parameters
def greet(name="Guest"):
  print("Hello", name)
  
greet() # Hello Guest
greet("Erkan") # Hello Erkan

# functions + Conditions
def check_age(age):
  if age >= 18:
    return "Adult"
  else:
    return "Minor"
    
print(check_age(20)) # Adult

# funtions + loops
def print_numbers(n):
  for i in range(n):
    print(i)

print_numbers(5) """ 0
                     1
                     2
                     3
                     4 """"
    

