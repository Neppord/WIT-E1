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
    return [
        int(token) if token.isdigit() else
        float(token) if '.' in token else token
        for token in string.split()
    ]
