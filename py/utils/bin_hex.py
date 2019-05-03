mode = int(input("N to bin,hex:0\nbin to N,hex:1\nhex to N,bin:2\n"))

if(mode ==0):
    N = int(input())

    binstr = bin(N)[2:]
    hexstr = hex(N)[2:].upper()

    print("binary ex: 0b" + binstr)
    print("hexadecimal ex: 0x" + hexstr)
elif(mode == 1):
    N = int(input(), 2)
    hexstr = hex(N)[2:].upper()

    print("decimal ex: " + str(N))
    print("hexadecimal ex: 0x" + hexstr)
else:
    N = int(input(), 16)
    binstr = bin(N)[2:]

    print("decimal ex: " + str(N))
    print("binary ex: 0b" + binstr)
