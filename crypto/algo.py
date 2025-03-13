from math import gcd

def est_premier(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def liste_premier_inf(n):
    return [i for i in range(2, n+1) if est_premier(i)]

def pgcd(a, b):
    while b:
        a, b = b, a % b
    return a

def cle_publique_possible(a, b):
    n = a * b
    return [i for i in range(1, n) if pgcd(i, n) == 1]

def inverse(e, n):
    t, newt = 0, 1
    r, newr = n, e
    while newr != 0:
        quotient = r // newr
        t, newt = newt, t - quotient * newt
        r, newr = newr, r - quotient * newr
    if r > 1:
        raise ValueError("L'inverse modulaire n'existe pas")
    if t < 0:
        t += n
    return t

def chaine_en_liste(chaine):
    return [ord(c) for c in chaine]

def chiffre(e, N, liste):
    return [pow(x, e, N) for x in liste]

def dechiffre(d, N, liste):
    return [pow(x, d, N) for x in liste]

def liste_en_chaine(liste):
    return ''.join(chr(x) for x in liste)

a, b = 61, 53
N = a * b
phi = (a - 1) * (b - 1)
e = 17
d = inverse(e, phi)

message = "RSA"
message_code = chaine_en_liste(message)
message_chiffre = chiffre(e, N, message_code)
message_dechiffre = dechiffre(d, N, message_chiffre)
message_final = liste_en_chaine(message_dechiffre)

print("Message initial:", message)
print("Message chiffré:", message_chiffre)
print("Message déchiffré:", message_final)
