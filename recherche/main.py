if __name__ == "__main__":
    liste1 = [12,1,20,5,23,8,29,10]
    liste2 = [23,5,19,11,18,20,29,1,5,10,8]

def recherche_naive(l1, l2):
    if not l1 or not l2:
        return []
    if l1[0] == l2[0]:
        return [l1[0]] + recherche_naive(l1[1:], l2[1:])
    else:
        seq1 = recherche_naive(l1[1:], l2)
        seq2 = recherche_naive(l1, l2[1:])
        return seq1 if len(seq1) >= len(seq2) else seq2