""" What is an Error?

An error is when Python cannot run your code. 

ZeroDivisionError	  10 / 0
NameError	          print(x) if x is undefined
TypeError	          5 + "5"
IndexError	        [1,2][5]
KeyError	          {"a":1}["b"] 

"""

# didiving by 0 is impossible
print(10 / 0) # ZERODivisionError

# example

try:
  number = int(input("Enter a number: "))
  print(10 / number)
except:
  print("Something went wrong!")
""" if user types: 0 = divison error!
    if user types: hello = conversion error
  instead of crashing, it prints:
  "Sometwhing went wrong!"
"""

# instead of crashing we can catch errors!
try:
  x = 10 / 0
except ZeroDivisionError:
  print("Cannot divide by zero!")

# handling multiple exceptions
try:
  x = int("hello")
except ValueError:
  print("Cannot convert string to int")
except ZeroDivisionError:
  print("Cannot divide by zero")

# catch all exceptions (Not recommended for beginners but okay for safety)
try:
  x = 10 / 0
except Exception as e:
  print("Error:", e)

# else in try except (runs if no error occurred)
try;
  x = 10 / 2
except ZeroDivisionError:
  print("Error!")
else:
  print("No error, result:", x)

# finally in try-except (runs always, even if theres an error)
try:
  x = 10 / 0
except ZeroDivisionError:
  print("Error!")
finally:
  print("This runs anyway")

# real life example (file reading)
try:
  with open("data.txt", "r") as file:
    print(file.read())
except FileNotFoundError:
  print("File not found!")



