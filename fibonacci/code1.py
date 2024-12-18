import numpy as np
def fibobo(n):
    if n<= 1:
        return n
    return fibobo(n-1) + fibobo(n-2)


print(fibobo(30))

def fibibi(n):
    fibi = np.array([[1,1],[1,0]])
    return np.linalg.matrix_power(fibi,n)[0][-1]
print(fibibi(100))
