import sys
pm = ["+", "-"]
# table1 = [0007,0016,0025,0034,0043,0052,0061,0070,0106,0115,0124,0133,0142,0151,0160,
# 0205,0214,0223,0232,0241,0250,0304,0313,0322,0331,0340,0403,0412,0421,0430,0502,
# 0511,0520,0601,0610,0700,1006,1015,1024,1033,1042,1051,1060,1105,1114,1123,1132,1141,1150,1204,1213,
# 1222,1231,1240,1303,1312,1321,1330,1402,1411,1420,1501,1510,1600,2005,2014,2023,
# 2032,2041,2050,2104,2113,2122,2131,2140,2203,2212,2221,2230,2302,2311,2320,2401,
# 2410,2500,3004,3013,3022,3031,3040,3103,3112,3121,3130,3202,3211,3220,3301,3310,
# 3400,4003,4012,4021,4030,4102,4111,4120,4201,4210,4300,5002,5011,5020,5101,5110,
# 5200,6001,6010,6100,7000]
ABCD = str(input())
for s0 in pm:
    for s1 in pm:
        for s2 in pm:
            if(eval(ABCD[0] + s0 + ABCD[1] + s1 + ABCD[2] + s2 + ABCD[3] ) == 7):
                print(ABCD[0] + s0 + ABCD[1] + s1 + ABCD[2] + s2 + ABCD[3] + "=7")
                sys.exit()
