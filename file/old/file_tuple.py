def creer_file_vide():
    return ()

def est_vide(file: tuple)-> bool:
    return () == file

def tete(file: tuple):
    assert not(est_vide(file)), "file vide"
    element, reste = file

    return element

def queue(file):
    element,reste = liste
    return reste

def inserer_tete(file,elt):
    return (elt,file)

def inserer_queue(file,elt):
    if est_vide(file):
        return inserer_tete(file,elt)
    return inserer_tete(inserer_queu(queue(file),elt)tete(file))
