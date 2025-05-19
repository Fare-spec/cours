if __name__ == "__main__":
    liste1 = [12,1,20,5,23,8,29,10]
    liste2 = [23,5,19,11,18,20,29,1,5,10,8]


def recherche(l1, l2):
    ln1 = len(l1)
    ln2 = len(l2)
    if ln1>ln2:
        for element in l2:
            t = True
            while t:
                b = l1[index(element)]