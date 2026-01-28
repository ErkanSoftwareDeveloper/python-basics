""" What is a for loop?

A for loop repeats a block of code for each item in a sequence (list, string, range…).

It’s used to iterate over elements. """


# looping over a list
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
  print(fruit) """ apple
                 banana
                 cherry """

# looping over a string
word = "Python"

for letter in word:
  print(letter) """ P
                    y
                    t
                    h
                    o
                    n """
  
# using range() with For loops
for i in range(5):
  print(i) """0
              1
              2
              3
              4
                """
  
# range(start, end) 
for i in range(2, 6):
  print(i) """2
              3
              4
              5 """
  
# range(start, end, step) specify step
for i in range(0, 10, 2):
    print(i) """0
                2
                4  
                6
                8 """
  
# using break and continue ! break is the exit loop
for i in range(5):
  if i == 3:
    break
  print(i) """0
             1
             2 """
  
# and for continue use "continue"
for i in range(5):
  if i == 3:
    continue
  print(i) """0
              1
              2
              4 """
  
# loop with else (optional)
for i in range(3):
  print(i)
else:
  print"Loop finished!") """0
                            1
                            2
                            Loop finished! """
  





  


