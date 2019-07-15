
# if pass a < b, increasing. b is succesor of a

def InsertionSort(arr, comp):
    N = len(arr)
    cnt = 0
    for i in range(1, N):
        for j in range(i, 0, -1):
            if comp(arr[j], arr[j-1]):
                cnt += 1
                arr[j-1], arr[j] = arr[j], arr[j-1]
    # return swap time
    return cnt

A = list(map(int, input().split()))
InsertionSort(A, lambda x, y: x > y)
print(A)
