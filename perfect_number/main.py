import math


def find_diviseur(number):
    diviseurs = []
    limit = int(number / 2)
    for i in range(1, limit):
        if number % i == 0:
            diviseurs.append(i)
    return diviseurs


if __name__ == "__main__":
    print(find_diviseur(15))
