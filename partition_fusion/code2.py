from random import shuffle
i = 0
def fusion(liste_1,liste_2):
    global i
    i+=1
    if len(liste_1) == 0:
        return liste_2
    if len(liste_2) == 0:
        return liste_1
    if liste_1[0] <= liste_2[0]:
        return [liste_1[0]] + fusion(liste_1[1:],liste_2)

    return [liste_2[0]] + fusion(liste_1,liste_2[1:])

def tri_pf(liste):
    if len(liste)<=1:
        return liste
    millieu = len(liste)//2
    return fusion(tri_pf(liste[:millieu]), tri_pf(liste[millieu:]))



test = [23,8,20,10,13,1]
print(test)
test = tri_pf(test)
print(test, i )
