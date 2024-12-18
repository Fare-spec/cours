
def fusion_rec(a, b):
    if len(a) == 0:
        return b
    if len(b) == 0:
        return a
    if a[0] <= b[0]:
        return [a[0]] + fusion_rec(a[1:], b)
    return [b[0]] + fusion_rec(a, b[1:])

def tri(liste):
    if len(liste) <= 1:
        return liste
    liste1 = liste[:len(liste) // 2]
    liste2 = liste[len(liste) // 2:]
    liste1 = tri(liste1)
    liste2 = tri(liste2)
    return fusion(liste1, liste2)
