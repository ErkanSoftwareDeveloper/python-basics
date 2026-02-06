""" File Read & Write in Python (file-read-write.py)
️ What does “file read / write” mean?

It means:

Read data from a file

Write data into a file

Save information permanently

Example use cases:

saving user data

logs

config files

simple databases """

# opening a File
file = open("example.txt", "r")


""" File modes:
Mode	Meaning
"r"	read
"w"	write (overwrites)
"a"	append
"x"	create new file """

# read entire file
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()

# read line by line
file = open("example.txt", "r")

for line in file:
  print(line.strip()))

file.close()

# read into a list
file = open("example.txt", "r")
lines = file.readlines()
file.close()

print(lines)

# writing to a file
file = open("example.txt", "w")
file.write("Hello Python\n")
file.write("File writing is easy")
file.close()

# appending to a file
file = open("example.txt", "a")
file.write("\nThis is appended text")
file.close()

# using with  (you dont need close() )
with open("example.txt", "r") as file:
  print(file.read())

# writing
with open("example.txt", "w") as file:
  file.write("Clean and safe")

# cheking if a file exists
import os

if os.path.exists("example.txt"):
  print("file exists")
else:
  print("file not found")

# simple real example
with open("numbers.txt", "w") as file:
  for i in range(5):
    file.write(str(i) + "\n")



