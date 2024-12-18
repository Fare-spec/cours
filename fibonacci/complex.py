import numpy as np
import time
import matplotlib.pyplot as plt
import math

# Définir les fonctions
def fibobo(n):
    if n <= 1:
        return n
    return fibobo(n - 1) + fibobo(n - 2)

def fibibi(n):
    fibi = np.array([[1, 1], [1, 0]])
    return np.linalg.matrix_power(fibi, n)[0][-1]

# Benchmark des temps d'exécution
n_values_recursive = range(1, 35, 1)  # Plage raisonnable pour fibobo (approche récursive)
n_values_matrix = range(1, 50, 1)    # Limiter n pour éviter les dépassements avec 2^n

# Temps pour fibobo
times_recursive = []
for n in n_values_recursive:
    start_time = time.time()
    fibobo(n)
    times_recursive.append(time.time() - start_time)

# Temps pour fibibi
times_matrix = []
for n in n_values_matrix:
    start_time = time.time()
    fibibi(n)
    times_matrix.append(time.time() - start_time)

# Calculer log(n) et 2^n pour comparaison
log_n = [math.log(n) for n in n_values_matrix]
exp_2_n = [2**n for n in n_values_matrix]

# Graphique
plt.figure(figsize=(12, 8))

# Graphe des temps pour fibobo
plt.plot(n_values_recursive, times_recursive, label="fibobo (récursif)", marker='o')

# Graphe des temps pour fibibi
plt.plot(n_values_matrix, times_matrix, label="fibibi (matriciel)", marker='s')

# Ajouter log(n) pour comparaison simple
plt.plot(n_values_matrix, log_n, label="log(n)", linestyle="--")

# Ajouter 2^n pour comparaison simple
plt.plot(n_values_matrix, exp_2_n, label="2^n", linestyle=":")

# Ajuster l'échelle de l'axe y pour éviter les dépassements
plt.yscale('log')  # Échelle logarithmique pour mieux visualiser les variations
plt.ylim(1e-6, 1e10)  # Limiter les valeurs extrêmes

plt.title("Comparaison des performances avec log(n) et 2^n")
plt.xlabel("Valeur de n")
plt.ylabel("Temps d'exécution ou croissance (échelle logarithmique)")
plt.legend(loc="upper left")
plt.grid()
plt.show()
