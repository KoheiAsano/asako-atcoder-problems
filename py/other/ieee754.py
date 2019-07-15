class ieee754_64:
    # インプットは全部bit文字列
    def __init__(self, s : str, e : str, m : str):
        self.sign = 1 if s == 0 else -1
        self.exponent = 2**(int(e, 2)-127)
        tmpman = 0
        pow = 0.5
        for i in range(1, 24):
            tmpman += int(m[i-1])*pow
            pow *= 0.5
        self.mantissa = 1 + tmpman

    def __str__(self):
        return str(self.sign*self.exponent*self.mantissa)

    def __repr__(self):
        return str(self.sign*self.exponent*self.mantissa)


s = '0'
e = '10000010'
m = '11010000000000000000000'
print(len(s), len(e), len(m))
print(ieee754_64(s, e, m))
