for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    #My answers but wrong for their test cases
    # print(*[a for a in range(1,i)],*[b for b in range(i,0,-1)],sep="")
    #  print(*range(1,i), *range(i,0,-1))
    # print(*list(range(1,i)), *list(range(i,0,-1)), sep="")

    # print(i,1+1,1,sep="")
    # names = [1,2,3,4]
    # print(*names, sep = "")
    print((10**i//9)**2) # accepted answer