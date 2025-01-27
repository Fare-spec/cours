class Pile:
    def __init__(self) -> None:
        self.element = []

    def empiler(self,element)->None:
        self.element.append(element)

    def est_vide(self)->bool:
        return len(self.element) == 0

    def defiler(self):
        assert not self.est_vide(), "La pile est vide"
        return self.element.pop()

    def size(self)->int:
        return len(self.element)

    def index(self, k):
        assert not self.est_vide(), "La pile est vide"
        return self.element[k]
