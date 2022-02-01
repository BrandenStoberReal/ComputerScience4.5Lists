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
#Objective 4
for i in range(len(Numbers)):
    if (Numbers[i] % 2 == 1):
        print(Numbers[i])

print("\n")
#Objective 5
for i in range(len(Names)):
    if (Names[i] > "Thor"):
        print(Names[i])

print("\n")
Buffer = Numbers[0]
Buffer2 = Numbers[0]
#Objective 6
for i in range(len(Numbers)):
    if (Numbers[i] > Buffer):
        Buffer = Numbers[i]

for i in range(len(Numbers)):
    if (Numbers[i] < Buffer2):
        Buffer2 = Numbers[i]

print("Max Value: " + str(Buffer))
print("Min Value: " + str(Buffer2))