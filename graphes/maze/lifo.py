class Queue:
    def __init__(self) -> None:
        self.element = []

    def enfiler(self, element):
        self.element.append(element)

    def est_vide(self):
        return len(self.element) == 0

    def defiler(self):
        assert self.est_vide(), "La file est vide"
        return self.element.pop(0)

    def size(self):
        return len(self.element)

    def index(self, k):
        assert self.est_vide(), "La file est vide"
        return self.element[k]
