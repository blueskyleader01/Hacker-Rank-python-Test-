# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools as it

def comb(a,k):
    g =  len(list(it.combinations(a, k)))
    print(g)
    l = 0
    # print(list(it.combinations(a, k)))
    for i in list(it.combinations(a, k)):
        if "a" in i:
            l = l + 1
    return round(l / g,12)



n = int(input())
c = input()
a = []
for i in c.rstrip().split():
    a.append(i)
k = int(input())

result = comb(a,k)
print(result)