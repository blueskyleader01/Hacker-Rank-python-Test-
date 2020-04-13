import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    dummylist = [0 for _ in range(n)]
    for aquery in queries:
        k = aquery[2]
        a = aquery[0] -1
        b = aquery[1]
        if k > 1000000000:
            return "k too large"
        if a > b:
            return "a cannot be greater than b"
        if a > n or b > n:
            return "a or b cannot be greater than n"
        for dummy in range(a,b):
            dummylist[dummy] =  dummylist[dummy] + k
    return max(dummylist)
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    if n < 3 or n > 10000000:
        print("n too large or too")
    elif m < 1 or m > 100000:
        print('m too large or small')
    else:
        queries = []

        for _ in range(m):
            queries.append(list(map(int, input().rstrip().split())))

        result = arrayManipulation(n, queries)

        print(result)

        # fptr.write(str(result) + '\n')

    # fptr.close()
