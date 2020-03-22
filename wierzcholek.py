class Wierzchołek:
    def __init__(self, sąsiedzi=[]):
        # lista sąsiadów w postaci '(id sąsiada, koszt dojazdu do sąsiada)'
        self.sąsiedzi = list(sąsiedzi)
        
    def dodaj_sąsiada(self, id_celu, koszt):
        self.sąsiedzi.append((id_celu, float(koszt)))

class Graf:
    def __init__(self, wierzchołki={}):
        # słownik wierzchołków w grafie '{id -> Wierzchołek}'
        self.wierzchołki = dict(wierzchołki)
        
    def dodaj_wierzchołek(self, id_swoje, id_celu=None, koszt=None):
        # jeżeli wierzchołka nie ma jeszcze w grafie, to go stwórz
        if id_swoje not in self.wierzchołki:
            self.wierzchołki[id_swoje] = Wierzchołek()
        # dodaj do wierzchołka odpowiedniego sąsiada
        self.wierzchołki[id_swoje].dodaj_sąsiada(id_celu, koszt)
        
    def czytaj_plik(self, nazwa_pliku):
        plik = open(nazwa_pliku)
        # dla każdej linii z pliku
        for linia in plik:
            linia = linia.strip().split()
            id_swoje = linia[0]
            id_celu = linia[1]
            koszt = linia[2]
            self.dodaj_wierzchołek(id_swoje, id_celu, koszt)
        plik.close()