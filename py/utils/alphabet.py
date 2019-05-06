alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
        'h', 'i', 'j', 'k', 'l', 'm', 'n',
         'o', 'p', 'q', 'r', 's', 't', 'u',
          'v', 'w', 'x', 'y', 'z']
alp = [a.upper() for a in alp]
index = [n for n in range(1, 27)]
print(alp)
print(dict(zip(alp, index)))
