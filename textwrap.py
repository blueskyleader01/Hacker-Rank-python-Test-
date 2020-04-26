#my solution
strings = input()
n = int(input())
print(strings[0:n])
for i in range(0,len(strings),n):
    print(strings[i:i+n])

#another problematic solution
# import textwrap

# def wrap(string, max_width):
#     return textwrap.fill(string, width=max_width)

# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)