""" A while loop repeats a block of code as long as a condition is True.

Think of it as:

Keep doing this while this condition is true."""

count = 0
while count < 5:
  print(count)
  count += 1 """ 0
                 1
                 2
                 3
                 4 """
  
# same way but different typ
count = 0
while count < 5:
  print(count)
  count += 2 """ 0
                 2
                 4 """

# using break in while loops
count = 0

while True:
  print(count)
  count += 1
  if count == 3:
    break """ 0
              1
              2 """

# using continue in While loops

count = 0

while count < 5:
  count += 1
  if count == 3:
    continue
  print(count) """ 1
                   2
                   4
                   5 """
  # else in while loops (optional)
count = 0
while count < 3:
    print(count)
    count += 1
else:
  print("Loop finished!") """ 0
                              1
                              2
                              Loop finished! """
# infinite loops 
while True:
  print("Thiw will run forever!") """ This will run forever
                                      This will run forever
                                      This will run forever
                                      This will run forever
                                      This will run forever... """
  
