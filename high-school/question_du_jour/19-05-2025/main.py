# Trouver la plus grande séquence de caractère commune entre de listes ou string
from random import randint
if __name__ =="__main__":
    l1 = [randint(0,100) for _ in range(100)]   
    l2 = [randint(0,100) for _ in range(100)]
adef lcs(a, b):
    """
    Renvoie la plus longue sous-séquence commune entre séquences a et b.
    """
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if a[i] == b[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
    i, j = n, m
    seq = []
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            seq.append(a[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return seq[::-1]


if __name__ == "__main__":
    from random import randint
    l1 = [randint(0, 100) for _ in range(100)]
    l2 = [randint(0, 100) for _ in range(100)]
    commun = lcs(l1, l2)
    print(commun)
