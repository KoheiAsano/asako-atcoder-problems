N = int(input())

binstr = bin(N)[2:]
hexstr = hex(N)[2:].upper()

print("binary ex: 0b" + binstr)
print("hexadecimal ex: 0x" + hexstr)
