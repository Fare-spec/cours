def triage(liste:list) -> list:
    if len(liste) < 2:
        return list
    for i in range(len(liste)-1):
        if liste[i] > liste[i+1]:
            liste[i], liste[i+1] = liste[i+1], liste[i]
            return triage(liste)
    return liste

def triii(liste: list) -> list:
    if liste == [] :
        return []
    mini = 0
    for i in range(1, len(liste)):
        if liste[i] < liste[mini]:
            mini = i
    liste[0], liste[mini] = liste[mini], liste[0]
    return [liste[0]] + triii(liste[1:])