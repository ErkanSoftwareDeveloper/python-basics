""" A string is a sequence of characters, used to represent text.

Strings are written inside quotes: single ' ' or double " ".

Examples: """

# String Concatenation 
first = "Hello"
second = "World"
message = first + " " + second
print(message) # Hello World

# Multiplication
laugh = "Ha"
print(laugh * 3) #HaHaHa

# Indexing Strings
word = "Python"
print(word[0]) # P = first charachter
print(word[3]) # H = fourth charahter
# Negative indexing counts from the end:
print(word[0]) # n = last character
print(word[-2]) # o = second to last

# Slicing Strings
word = "Python"
print(word[0:4]) # Pyth
print(word[2]) # thon
print(word[:3]) # Pyt

# Common string Methods 
text = "Hello World"

print(text.upper()) # HELLO WORLD
print(text.lower()) # hello world
print(text.capitalize()) #Hello world
print(text.title()) # Hello world

# Removing Spaces 
name = " Erkan "
print(name.strip()) # "Erkan"
print(name.lstrip()) # remove left spaces
print(name.rstrip()) # remove right spaces

# Replace Text
text = "I like Python"
new_text = text.replace("Python", "Java" 
print(new_test) # i like Java

# Split
