if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    arr = set(arr)
    max_score = max(arr)
    arr = list(arr)
    print(max_score)
    for i in arr:
        if i == max_score:
            arr.remove(i)
    print(max(arr))
