from inspect import currentframe
from sys import exit, stderr
src = list(str(input()))
tokens = [tok for tok in src if tok != " "]

def debug(*args):
    names = {id(v):k for k,v in currentframe().f_back.f_locals.items()}
    print(', '.join(names.get(id(arg),'???') + str(id(arg)) +' = '+repr(arg) for arg in args), file=stderr)
print(tokens)
# "" as EOF
tokens.append("")
cur = 0
def parse_expr():
    global cur
    if tokens[cur] is "":
        return
    lhs = parse_mul()
    if tokens[cur] is "+":
        cur += 1
        lhs += parse_expr()
    elif tokens[cur] is "-":
        cur += 1
        lhs -= parse_expr()
    debug(lhs, cur)
    return lhs

def parse_mul():
    global cur
    lhs = parse_term()
    if tokens[cur] is "*":
        cur += 1
        lhs *= parse_mul()
    elif tokens[cur] is "/":
        cur += 1
        lhs /= parse_mul()
    # debug(lhs, cur)
    return lhs

def parse_term():
    global cur
    if tokens[cur].isdigit():
        lhs = int(tokens[cur])
        cur += 1
    elif tokens[cur] is "(":
        cur += 1
        lhs = parse_expr()
        if tokens[cur] != ")":
            raise Exception("not closed")
        cur += 1
    return lhs

print(parse_expr())
