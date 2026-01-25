""" A dictionary is used to store data in key → value pairs.

Instead of indexes (0, 1, 2), you use keys.

Dictionaries are written using curly braces {} """

# Dictionaries in Python
person = {
  "name": "Erkan",
  "age": 25,
  "is_student": False
}

# Accessing Values
print(person) # 
print(person["name]") # Erkan
print(person["age]") # 25

# using (get) safe way!
print(person.get("name")) # Erkan
print(person.get("job")) # None
print(person.get("job", "N/A")) # N/A

# adding new key-value pairs
