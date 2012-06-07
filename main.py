def lexer(string):
    """
    >>> lexer('1')
    [1]
    >>> lexer('2')
    [2]
    >>> lexer('1.5')
    [1.5]
    >>> lexer('1 + 2')
    [1, '+', 2]
    """
    ret = []
    for token in string.split():
        if token.isdigit():
            ret.append(int(token))
        elif '.' in token:
            ret.append(float(token))
        else:
            ret.append(token)
    return ret

def ast_builder(tokens):
    """
    >>> ast_builder([1])
    1
    >>> ast_builder([2])
    2
    >>> ast_builder([1, '+', 2])
    (1, '+', 2)
    >>> ast_builder([1, '+', 2, '*', 3])
    (1, '+', (2, '*', 3))
    >>> ast_builder([1, '*', 2, '+', 3])
    ((1, '*', 2), '+', 3)
    """
    if len(tokens) == 3:
        return tuple(tokens[:3])
    elif len(tokens) == 1:
        return tokens[0]
    else:
        if tokens[1] in "+-":
            return tuple(tokens[:2] + [ast_builder(tokens[2:])])
        else:
            return ast_builder([tuple(tokens[:3])] + tokens[3:])

def evaluate(ast):
    """
    >>> evaluate(1)
    1
    >>> evaluate(2)
    2
    >>> evaluate((1, '+', 2))
    3
    >>> evaluate((1, '-', 2))
    -1
    >>> evaluate((1, '*', 2))
    2
    >>> evaluate((1., '/', 2))
    0.5
    >>> evaluate((1, '+', (2, '+', 3)))
    6
    >>> evaluate(((1, '+', 2), '+', 3))
    6
    """
    if type(ast) != tuple:
        return ast
    elif len(ast) == 3:
        expr1, op, expr2 = ast
        val1, val2 = evaluate(expr1), evaluate(expr2) 
        if op == '+':
            return val1 + val2
        elif op == '-':
            return val1 - val2
        elif op == '*':
            return val1 * val2
        elif op == '/':
            return val1 / val2

def main(argv):
    tokens = lexer(" ".join(argv))
    ast = ast_builder(tokens)
    print evaluate(ast)

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
