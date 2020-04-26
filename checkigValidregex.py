import re
a = int(input())
strings = []
for _ in range(a):
    strings.append(input())
print(strings)
for a in strings:
    try:
        re.compile(a)
        is_valid = True
        print(is_valid)
    except re.error:
        is_valid = False
        print(is_valid)
"""
    2

    /^(?!\.)(?=.)[d-\.]$/

    [a-zA-Z0-9,.' ]+
"""