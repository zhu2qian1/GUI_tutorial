def genpassword(ID: str = None, l: int = 8, punc: bool = True) -> tuple:
    """"""
    chars: list = []
    from random import choice
    from string import ascii_letters, digits

    chars.extend((ascii_letters * 2 + digits))
    if punc:
        from string import punctuation

        chars.extend(punctuation)

    return (ID, "".join([choice(chars) for i in range(l)]))
