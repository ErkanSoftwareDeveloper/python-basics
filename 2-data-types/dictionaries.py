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
print(person) # {'name': 'Erkan', 'Age': 25, 'is_student': False}
print(person["name]") # Erkan
print(person["age]") # 25

# using (get) safe way!
print(person.get("name")) # Erkan
print(person.get("job")) # None
print(person.get("job", "N/A")) # N/A

# adding new key-value pairs
person["job"] = "Developer"
print(person.get("job")) # Developer

# updating values
person["age"] = 26
print(person.get("age")) # 26

person["name"] = "Ece"
print(person.get("name")) # Ece

# removing items
person.pop("is_student")
print(person) # {'name': 'Ece', 'age': 26}

del person["age"] # {'name': 'Ece'}

# dictionary Length
print(len(person)) # 1

# loop keys
for key in person:
    print(key) # name, age, is_student

# loop values 
for value in person.values():
    print(value) # Erkan, 25, False
  
# Loop key and value
for key, value in person.items():
    print(key, ":", value)
""" name : Erkan
age : 25
is_student : False """

# checking keys
print("name" in person) # True
print("salary" in person) # False

# dictionary Methods (Important)
print(person.keys()) # dict_keys(['name', 'age', 'is_student'])             
print(person.values())) # dict_values(['Erkan', 25, False])
print(person.items()) # dict_items([('name', 'Erkan'), ('age', 25), ('is_student', False)])

# copying dictionaries
person = {"name": "Mert", "age": 30}

person_copy = person.copy()

person_copy["age"] = 31

print(person) # {'name': 'Erkan', 'age': 30}
print(person_copy) # {'name': 'Erkan', 'age': 31}

# nested Dictionaries
users = {
  "user1": {"name": "Erkan", "age": 25},
  "user2": {"name": "Ali", "age": 30}
}

print(users["user1"]["name])
# Erkan

# clear dictionary
person.clear() 
print(person) # {}



  
