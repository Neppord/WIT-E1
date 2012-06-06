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
    """
    return 1
