import os
import math
import random

Names = ["Peter", "Bruce", "Steve", "Tony", "Natasha", "Clint", "Wanda", "Hope", "Danny", "Carol"]
Numbers = [100, 50, 10, 1, 2, 7, 11, 17, 53, -8, -4, -9, -72, -64, -80]

#Objective 1
Switch = 0
for i in range(len(Names)):
    if (Switch == 0):
        Switch = 1
        print(Names[i])
    else:
        Switch = 0

