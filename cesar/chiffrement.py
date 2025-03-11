import string

def load_file():
    with open("message.txt", "r", encoding="utf-8") as f:
        content = f.read()
    return content

lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase

def dechiffrer(content, step):
    resultat = ""

    for char in content:
        if char in lower_case:
            index = (lower_case.index(char) - step) % 26
            resultat += lower_case[index]
        elif char in upper_case:
            index = (upper_case.index(char) - step) % 26
            resultat += upper_case[index]
        else:
            resultat += char

    return resultat

contenu = load_file()
texte_dechiffre = dechiffrer(contenu, step=17)

print("Texte déchiffré :")
print(texte_dechiffre)
