def card_conv(x:int, y:int) -> str:
    d=''

    dchar = '0123456789abcdefghijklmnopqrspuvwxyz'

    while x > 0:
        d += dchar[x%y]
        x //=y

    return d[::-1]