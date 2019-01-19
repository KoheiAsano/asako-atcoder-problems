import sys
dic = {"A":0,"B":0,"C":0,"D":0,"E":0, "F":0}
S = str(input())
for s in S:
    dic[s]+=1
n = 0
print(str(dic["A"]) + " " + str(dic["B"]) + " " + str(dic["C"]) + " " + str(dic["D"]) + " " + str(dic["E"]) + " " + str(dic["F"]))
# for v in dic.values():
#     sys.stdout.write(str(v))
#     if n != 5:
#         sys.stdout.write(" ")
# sys.stdout.write("\n")
