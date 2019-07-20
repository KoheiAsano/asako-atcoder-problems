from inspect import currentframe
from sys import exit, stderr

tokens = []
cur = 0
# def debug(*args):
#     names = {id(v):k for k,v in currentframe().f_back.f_locals.items()}
#     print(', '.join(names.get(id(arg),'???') + str(id(arg)) +' = '+repr(arg) for arg in args), file=stderr)
def parse_expr():
    global cur, tokens
    if tokens[cur] == "":
        return
    lhs = parse_mul()
    while(tokens[cur] == "+" or tokens[cur] == "-"):
        if tokens[cur] == "+":
            cur += 1
            lhs += parse_mul()
        elif tokens[cur] == "-":
            cur += 1
            lhs -= parse_mul()
        # debug(lhs, cur)
    return lhs

def parse_mul():
    global cur, tokens
    lhs = parse_term()
    while(tokens[cur] == "*" or tokens[cur] == "/"):
        if tokens[cur] == "*":
            cur += 1
            lhs *= parse_term()
        elif tokens[cur] == "/":
            cur += 1
            divisor = parse_term()
            if lhs < 0 and lhs % divisor != 0:
                lhs //= divisor
                lhs += 1
            else:
                lhs //= divisor
    return lhs

def parse_term():
    global cur, tokens
    if tokens[cur].isdigit():
        lhs = int(tokens[cur])
        cur += 1
        while(tokens[cur].isdigit()):
            lhs *= 10
            lhs += int(tokens[cur])
            cur += 1
    elif tokens[cur] == "(":
        cur += 1
        lhs = parse_expr()
        cur += 1
    return lhs

src = list(str(input()))
tokens = [tok for tok in src if tok != " "]

# "" as EOF
tokens.append("")

cur = 0
print(parse_expr())
