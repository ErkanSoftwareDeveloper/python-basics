""" What is a Condition?

A condition lets your program make a decision.

“IF something is true → do this
ELSE → do something else” """


# Basic if Statement
age = 18

if age >= 18:
  print("You are an adult") 

# if / else
age = 16

if age >= 18:
  print("You are an adult")
else:
  print("You are under 18")

# elif
score = 75

if score >= 90:
  print("Grade A")
elif score >= 70:
  print("Grade B")
else:
  print("Grade C")

""" Comparison Operators
Operator	Meaning

==	equal
!=	not equal
>	greater than
<	less than
>=	greater or equal
<=	less or equal """

x = 10
print(x == 10) # True
print(x != 5) # True

# Logical Operators
age = 25
is_student = False

""" and """
if age > 18 and not is_student:
  print("Adult and not a student")

""" or """
if age < 18 or is_student:
  print("Discount applies")

""" not """
logged_in = False
if not logged_in:
  print("Please log in")

# Checking String and Lists
name = "Erkan"
if name =="Erkan":
  print("Welcome Erkan")

""" """

users = ["Erkan", "Ali"]

if "Erkan" in users:
  print("User found")

# Truthy & Falsy Values (VERY important concept)
if "":
  print("This will NOT run")

if 0:
  print("Thiw will NOT run")

if[]:
  print("Thiw will NOT run")

""" Truthy examples: """

if "hello":
  print("This WILL run")

if 10:
  print("This WILL run")

# is vs == (basic awareness)
a = 10
b = 10
print(a == b) # True (value comparison)
print(a is b) # True (same object in memory - advanced topic)
