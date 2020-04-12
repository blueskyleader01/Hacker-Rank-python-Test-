#!/bin/python3

import math
import os
import random
import re
import sys
a = [1,2,3,4,5]

d = 4

# Complete the rotLeft function below.
def rotLeft(a, d):
    for value in a:
        if value == 0:
            return (" error: non zero valus are required")
    if d < 1 :
        return 'the rotation value must be greater than zero'
    if len(a) < 1:
        return 'the array cannot be empty'
    while d >= 1:
        popped_value = a.pop(0)
        a.append(popped_value)
        d = d- 1
    return a
print(rotLeft(a,d))


##if __name__ == '__main__':
##    fptr = open(os.environ['OUTPUT_PATH'], 'w')
##
##    nd = input().split()
##
##    n = int(nd[0])
##
##    d = int(nd[1])
##
##    a = list(map(int, input().rstrip().split()))
##
##    result = rotLeft(a, d)
##
##    fptr.write(' '.join(map(str, result)))
##    fptr.write('\n')
##
##    fptr.close()
