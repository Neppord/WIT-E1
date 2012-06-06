def lexer(string):
    """
    >>> lexer('1')
    [1]
    >>> lexer('2')
    [2]
    >>> lexer('1 + 2')
    [1, '+', 2]
    """
    return [
        int(token) if token.isdigit() else token for token in string.split()
    ]
