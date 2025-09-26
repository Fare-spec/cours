def appartient(elt, tableau):
    for i in tableau:
        if i == elt:
            return True
        else:
            continue
    return False


if __name__ == "__main__":
    print(appartient(5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(appartient(5, [1, 2, 3, 4, 6, 7, 8, 9, 10]))
