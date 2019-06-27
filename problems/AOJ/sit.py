INF = 10**10
while(True):
    N, M = [int(n) for n in input().split()]
    if N + M == 0:
        break
    chair = ["#" for _ in range(N)]
    for i in range(M):
        a = str(input())
        if a == "A":
            for i in range(N):
                if chair[i] == "#":
                    chair[i] = "A"
                    break
        elif a == "B":
            OK = False
            for i in range(N-1, -1, -1):
                if chair[i] == "#":
                    if i != 0 and chair[i-1] == "A":
                        continue
                    if i != N-1 and chair[i+1] == "A":
                        continue
                    chair[i] = "B"
                    OK = True
                    break
            if OK:
                continue
            for i in range(N):
                if chair[i] == "#":
                    chair[i] = "B"
                    break
        elif a == "C":
            if chair.count("#") == N:
                chair[(N)//2] = "C"
                continue
            OK = False
            for i in range(N):
                if chair[i] != "#":
                    if i != N-1 and chair[i+1] == "#":
                        chair[i+1] = "C"
                        OK = True
                        break
                    if i != 0 and chair[i-1] == "#":
                        chair[i-1] = "C"
                        OK = True
                        break
        elif a == "D":
            if chair.count("#") == N:
                chair[0] = "D"
                continue
            start = False
            distmap = [0 for _ in range(N)]
            dist = 0
            for i in range(N):
                if chair[i] != "#":
                    dist = 0
                    distmap[i] = dist
                    start = True
                elif start:
                    dist += 1
                    distmap[i] = dist
                else:
                    distmap[i] = INF
            start = False
            for i in range(N-1, -1, -1):
                if chair[i] != "#":
                    dist = 0
                    distmap[i] = min(dist, distmap[i])
                    start = True
                elif start:
                    dist += 1
                    distmap[i] = min(dist, distmap[i])
            target = max(distmap)
            for i in range(N):
                if distmap[i] == target and chair[i] == "#":
                    chair[i] = "D"
                    break
    print("".join(chair))
