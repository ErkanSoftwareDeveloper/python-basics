"""" A list is used to store multiple values in one variable.

Lists are written using square brackets [].

A list can contain different data types. """

# Example:
numbers = [1, 2, 3, 4]
names = ["Erkan", "Hakan", "Can"]
mixed = [1, "hello", 3.14, True]

# Instead of doing this, you do this:
a = 1
b = 2
c = 3
# this
numbers = [1, 2, 3]

# Key points to remember:
names = ["Erkan", "Hakan", "Can"]
print(names[0]) # Erkan
print(names[2]) # Can

# Append add ONE item to the end
numbers = [1, 2, 3]
numbers.append(4)

print(numbers) # [1, 2, 3, 4]

# Insert add itemt at a specific index
numbers = [1, 2, 3]
numbers.insert(1, 10)

print(numbers) # [1, 10, 2, 3]

# Remove by Value
numbers = [1, 2, 3, 4]
numbers.remove = (3)

print(numbers) # [1, 2, 4]

# Remove by Index
numbers = [1, 2, 3, 4]
numbers.pop(1)

print(numbers) # [1, 3, 4]

# Canging Items in a List
names = ["Erkan", "Hakan", "Can]
names[1] = "Mehmet"

print(names) # ['Erkan', 'Mehmet', 'Can']

# List Length
names = ["Erkan", "Hakan", "Can]
print(len(names)) # 3

# Checking items in a List
names = ["Erkan“, “Hakan", "Can]

print("Erkan" in names) # True
print("Veli" in names) # False

# Looping Through a List
names = ["Erkan", "Hakan", "Can"]

for name in names:
    print(name) # Erkan
                # Hakan
                # Can

# List Slicing
numbers = [1, 2, 3, 4, 5]

print(numbers[1:4]) # [2, 3, 4]
print(numbers[:3]) # [1, 2, 3]
print(numbers[2:]) # [3, 4, 5]
