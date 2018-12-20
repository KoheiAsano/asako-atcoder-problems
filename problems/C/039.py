# PIANO = "WBWBWWBWBWBW"
# MAP = {0:"Do",1:"Do", 2:"Re",
#        3:"Re", 4:"Mi", 5:"Fa",
#        6:"Fa", 7:"So", 8:"So",
#        9:"La", 10:"La", 11:"Si"}

ANS = {"WBWBWWBWBWBWWBWBWWBW":"Do",
       "WBWWBWBWBWWBWBWWBWWB":"Re",
"WWBWBWBWWBWBWWBWWBWB":"Mi",
"WBWBWBWWBWBWWBWWBWBW":"Fa",
"WBWBWWBWBWWBWWBWBWWB":"So",
"WBWWBWBWWBWWBWBWWBWB":"La",
"WWBWBWWBWWBWBWWBWBWB":"Si"}

S = str(input())
print(ANS[S])
#
# for i in range(len(S)):
#     if(S[i:i+12] == PIANO):
#         print(MAP[(12-i)%12])

# print()
# for i in range(20 -1):
#     # print(MAP[i+1])
#     print(Do[(i+1)%12:] + PIANO[:(i+1)%12] + ":" +MAP[(i+1)%12])
# # Do
# # WBWBWWBWBWBWWBWBWWBW
# # Do
# # BWBWWBWBWBW:WBWBWWBWB
