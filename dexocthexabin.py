#my solutions
# dec = int(input())  
# # a = len(bin(dec)) why is this greater than the second method?
# a = len("{0:b}".format(dec))
# for i in range(1,dec+1):
#     print ("{0:{width}d} {0:{width}o} {0:{width}x} {0:{width}b}".format(i, width=a))
# Others
# # n = int(input())
# # w = len("{0:b}".format(n))
# # for i in range(1,n+1):
# #   print ("{0:{width}d} {0:{width}o} {0:{width}x} {0:{width}b}".format(i, width=w))

def print_formatted(number):
    # a = len(bin(dec)) why is this greater than the second method?
    a = len("{0:b}".format(number))
    width = len('{:b}'.format(number))
    for i in range(1,number+1):
        print(str.rjust(str(i),width),str.rjust(str(oct(i)[2:]),width),str.rjust(str(hex(i).upper()[2:]),width),str.rjust(str(bin(i)[2:]),width))
    # for i in range(1,number+1):
    #     print ("{0:{width}d} {0:{width}O} {0:{width}X} {0:{width}B}".format(i, width=a))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)