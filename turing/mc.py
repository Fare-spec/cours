import Tabidir, exemples
class Configuration:
    def __init__(self, ruban,position, etat_courant):
        self.ruban = ruban
        self.position = position
        self.etat_courant = etat_courant

    def _str__(self):
        chaine = ' '
        chaine = chaine +(self.position-ruban.imin())*2*' '+self.etat_courant
        chaine = chaine + ' '+ (self.position+ruban.imin()*2*' '+ '|'+'\n')
        chaine = chaine+slef.ruban.__str__()
        return chaine

if __name__ == "__main__":
    ruban = Ta


class Machine:
