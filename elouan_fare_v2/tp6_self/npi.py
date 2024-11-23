def npi(exp: str) -> float:
    """Calcule une expression arithmétique en NPI (notation polonaise inverse).

    Args:
        exp (str): L'expression arithmétique à calculer.

    Returns:
        float: Le résultat de l'expression.
    """
    assert exp, "L'expression est vide."
    pile = []

    for token in exp.split():
        if token in "+-*/":
            if len(pile) < 2:
                print("Erreure : Pas assez d'opérandes.")
                return None
            
            b, a = pile.pop(), pile.pop()
            match token:
                case '+': pile.append(a + b)
                case '-': pile.append(a - b)
                case '*': pile.append(a * b)
                case '/':
                    if b == 0:
                        print("Erreur : Division par zéro.")
                        return None
                    pile.append(a / b)
        elif token.replace('.', '', 1).isdigit():  # isdigit verifie si 'token' est un nombre ou un chiffre
            pile.append(float(token))
        else:
            print(f"erreur : '{token}' n'est pas un opérande valide.")
            return None

    if len(pile) != 1:
        print("erreur : Expression mal formée.")
        return None

    return pile[0]  # On aurait pu mettre pile[-1]

if __name__ == "__main__":
    # Test
    exp = "3 4 + 5 * 2 /" # correspond a (3+4)(5/2) soit 7 * 2.5 = 17.5
    print(npi(exp))
