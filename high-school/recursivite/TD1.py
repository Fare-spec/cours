def factorielle(number: int):
    if number == 0:
        return 1
    else:
        return number * factorielle(number - 1)


def modulo(a, b):
    if b - a < 0:
        return b
    elif b == 0:
        return b
    else:
        return modulo(a, b - a)


def somme(n):
    if n == 0:
        return n
    else:
        return n + somme(n - 1)


def init_quotient(a, b):
    i = 0
    return quotient(a, b, i)


def quotient(a, b, i):
    if b == 0 or b - a < 0:
        return i
    else:
        return quotient(a, b - a, i + 1)


print(init_quotient(6, 18))
