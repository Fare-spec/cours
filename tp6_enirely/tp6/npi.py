def evaluer_npi(expression):
    """fais la notation polonaise inversée (NPI) d'une expression arithmétique
    Args:
        expression (_type_): String contenant l'expression arithmétique

    Returns:
        _type_: Integer contenant le resultat.
    """
    
    pile = []

    
    elements = expression.split()

    for element in elements:
        if element.isdigit():  
            pile.append(int(element))
        else:
            
            droite = pile.pop()  
            gauche = pile.pop()  

            if element == '+':
                resultat = gauche + droite
            elif element == '-':
                resultat = gauche - droite
            elif element == '*':
                resultat = gauche * droite
            elif element == '/':
                resultat = gauche / droite
            else:
                raise ValueError(f"Opérateur inconnu: {element}")

            
            pile.append(resultat)

    
    if len(pile) != 1:
        raise ValueError("L'expression est mal formée.")
    
    return pile.pop()  


expression = "100 60 / 60 + 90 *"
resultat = evaluer_npi(expression)
print(f"Le résultat de l'expression '{expression}' est: {resultat}")
