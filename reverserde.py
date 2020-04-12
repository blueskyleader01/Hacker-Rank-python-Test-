def dynamicArray(n,queries):

    seqList = []
    lastAnswer = 0
    for seq in range(n):
        seqList.append([])
    for i in range(len(queries)):
        z = queries[i]
        query = z[0]
        x = z[1]
        y = z[2]
        if query == 1:
            seqList[x ^ lastAnswer % n].append(y)
        elif query == 2:
            #query 2
            size = len(seqList[x^lastAnswer % n])
            lastAnswer = seqList[x^lastAnswer % n][y % size]
    q = []
    q.append(seqList[1])
    q.append(lastAnswer)        
    return q


firt_mult_input = input().rstrip().split()
n = int(firt_mult_input[0])
q = int(firt_mult_input[1])
queries = []
for _ in range(q):
    queries.append(list(map(int, input().rstrip().split())))
result = dynamicArray(n,queries)
print(result)