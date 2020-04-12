#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    result = []
    for i in queries:
        result.append(0)
    for aquery in range(len(queries)):
        for astring in range(len(strings)):
            if queries[aquery] == strings[astring]:
                result[aquery] = result[aquery] + 1
    return result
"""
4
aba
baba
aba
xzxb
3
aba
xzxb
ab
"""
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    print('\n'.join(map(str, res)))
    print('\n')

    # fptr.write('\n'.join(map(str, res)))
    # fptr.write('\n')

    # fptr.close()
