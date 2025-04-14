def insertion_sort(liste, ordre):
    for i in range(1, len(liste)):
        key = liste[i]
        j = i - 1
        while j >= 0 and ordre(liste[j], key) == -1:
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = key
    return liste

def ordre(a,b):
    if a>b:
        return -1
    elif a<b:
        return 1
    else:
        return 0


if __name__ == "__main__":
    l1 = [2,1,6,5,4,7,6,3,2]
    insertion_sort(l1,ordre=None)
    print(l1)

def dichotomie(liste,ordre,element):
    gauche = 0
    droite = len(liste)
    while (droite - gauche)-1:
        millieu = (gauche + droite) //2
        if ordre(liste[millieu],element)//2 ==0:
            gauche, droite = millieu, milleu +1
        elif ordre(liste[millieu],element) == -1:
            droite = millieu
        else:
            gauche = millieu+1
    if gauche-droite > 0 and liste[gauche] = element:
        return gauche
    else:
        return -1

