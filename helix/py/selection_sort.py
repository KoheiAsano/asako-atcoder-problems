# Selection Sort
def SelectionSort(arr, comp):
    N = len(arr)
    cnt = 0
    for i in range(0, N):
        swaptarg = i
        for j in range(N-1, i, -1):
            if comp(arr[j],arr[swaptarg]):
                swaptarg = j
        if i != swaptarg:
            cnt += 1
            arr[swaptarg], arr[i] = arr[i], arr[swaptarg]
    # return swap time
    return cnt


A = list(map(int, input().split()))
InsertionSort(A, lambda x, y: x > y)
print(A)
