#Doc→https://docs.python.org/ja/3/library/bisect.html
import bisect
print(bisect.__file__)
def grade(score, breakpoint=[60,70,80,90], grades='FDCBA'):
    i = bisect.bisect_right(breakpoint,score)
    print(i)
    return grades[i]

scores = [60,89,11,100]#→側、つまり以上
for s in scores:
    print(grade(s))
