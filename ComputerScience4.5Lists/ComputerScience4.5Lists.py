import os
import math
import random

Names = ["Peter", "Bruce", "Steve", "Tony", "Natasha", "Clint", "Wanda", "Hope", "Danny", "Carol"]
Numbers = [100, 50, 10, 1, 2, 7, 11, 17, 53, -8, -4, -9, -72, -64, -80]

#Objective 1
for i in range(len(Names)):
    if (i % 2 == 0):
        print(Names[i])

print("\n")

#Objective 2
for i in range(len(Numbers)):
    if (Numbers[i] > 0):
        print(Numbers[i])

print("\n")
#Objective 3
Sum = 0
for i in range(len(Numbers)):
    Sum = Sum + Numbers[i]
print(Sum)

print("\n")