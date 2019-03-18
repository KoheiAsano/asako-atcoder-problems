module = ["a","b","c"]
def f(rest, s):
    if(rest == 0):
        print(s)
    else:
        for c in module:
            f(rest -1, s + c)
N = int(input())


f(N,"")
