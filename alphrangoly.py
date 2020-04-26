# N,M = map(int,input().split())
# for i in range(1, N, 2): 
#     print (( str('.|.')*i ).center(M, '-'))
# print (str('WELCOME').center(M, '-'))
# for i in range(N-2, -1, -2): 
#     print(( str('.|.')*i ).center(M, '-'))
# def print_rangoli(size):
#     # your code goes here
#     for i in range(size)

# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)
import string
n = 5 
alphabet_string = string.ascii_lowercase
print((alphabet_string[n-1]).center((n-1)**2,"-"))

for i in range(n-1,-1,-1):
    print((alphabet_string[n-1] + "-" + alphabet_string[i] + "-" + alphabet_string[n-1]).center((n-1)**2,"-"))
# # for i in (n-1,1,-1):
# #     print((str("-a-")*i).center(n,'-a-'))

