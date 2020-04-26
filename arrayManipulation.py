# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# """
# 0 0 0 0 0 0 0 0 0 0
# 5 3
# 1-1 2+1 100
# 2 5 100
# 3 4 100
# 00000
# 100 100 0 0 0
# 100 200 100 100 100
# 100 200 200 200 100
# max 200
# """

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    dummylist = [0 for _ in range(n)]

    for aquery in queries:
        value_to_add = aquery[2]
        indices_to_start = aquery[0]
        indices_to_finish = aquery[1]
        l = 0
        for i in range(len(dummylist)):
            if i >= indices_to_start or i <= indices_to_finish:
                dummylist[i] =  dummylist[i] + value_to_add

#         [dummylist[dummy]+value_to_add for dummy in range(indices_to_start,indices_to_finish)]
# #         for dummy in range(indices_to_start,indices_to_finish):
# #             dummylist[dummy] =  dummylist[dummy] + value_to_add
        
# #         # while indices_to_start < indices_to_finish:
# #         #     dummylist[indices_to_start] += value_to_add
# #         #     indices_to_start += 1
    return max(dummylist)




# if __name__ == '__main__':
#     # fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     nm = input().split()

#     n = int(nm[0])

#     m = int(nm[1])

#     queries = []

#     for _ in range(m):
#         queries.append(list(map(int, input().rstrip().split())))

#     result = arrayManipulation(n, queries)

#     print(str(result) + '\n')
#     # fptr.write(str(result) + '\n')

#     # fptr.close()

# def arrayManipulation(n, queries):
#     arr = [0]*n
#     for i in queries:
#         arr[i[0] - 1] += i[2]
#         if i[1] != len(arr):
#             arr[i[1]] -= i[2]
#     maxval = 0
#     itt = 0
#     print(arr)
#     for q in arr:
#         itt += q
#         if itt > maxval:
#             maxval = itt
#     return maxval

nm = input().split()

n = int(nm[0])

m = int(nm[1])

queries = []

for _ in range(m):
    queries.append(list(map(int, input().rstrip().split())))

result = arrayManipulation(n, queries)

print(str(result) + '\n')