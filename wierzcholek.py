#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Wierzchołek:
    def __init__(self, sąsiedzi=[]):
        self.sąsiedzi = list(sąsiedzi)
        self.heurystyka = 0
        
    def dodaj_sąsiada(self, id_celu, koszt):
        self.sąsiedzi.append((id_celu, float(koszt)))

class Graf:
    def __init__(self, wierzchołki={}):
        self.wierzchołki = dict(wierzchołki)
        self.krawędzie_malejąco = list()
        
    def dodaj_wierzchołek(self, id_swoje, id_celu=None, koszt=None):
        if id_swoje not in self.wierzchołki:
            self.wierzchołki[id_swoje] = Wierzchołek()
        self.wierzchołki[id_swoje].dodaj_sąsiada(id_celu, koszt)

        if id_celu not in self.wierzchołki:
            self.wierzchołki[id_celu] = Wierzchołek()
        self.wierzchołki[id_celu].dodaj_sąsiada(id_swoje, koszt)
        
    def czytaj_plik(self, nazwa_pliku):
        plik = open(nazwa_pliku)

        for linia in plik:
            linia = linia.strip().split()

            id_swoje = linia[0]
            id_celu = linia[1]
            koszt = linia[2]

            self.krawędzie_malejąco.append((float)(koszt))
            self.dodaj_wierzchołek(id_swoje, id_celu, koszt)
            
        self.krawędzie_malejąco.sort(reverse=True)
        plik.close()

    def oblicz_heurystykę(self, id_celu):
        aktualna_heurystyka = 0

        odwiedzone = dict()
        for id in self.wierzchołki.keys():
            odwiedzone[id] = False

        wierzchołki = list()
        wierzchołki.append(id_celu)
        odwiedzone[id_celu] = True

        while(len(wierzchołki) > 0):
            wierzchołki_na_następnym_poziomie = list()

            for id in wierzchołki:
                self.wierzchołki.get(id).heurystyka = aktualna_heurystyka
                for (sąsiad, koszt) in self.wierzchołki.get(id).sąsiedzi:
                    if(odwiedzone[sąsiad] == False):
                        wierzchołki_na_następnym_poziomie.append(sąsiad)
                        odwiedzone[sąsiad] = True

            wierzchołki = wierzchołki_na_następnym_poziomie

            aktualna_heurystyka += self.krawędzie_malejąco[-1]
            if(len(self.krawędzie_malejąco) > 1):
                self.krawędzie_malejąco.pop(-1)

    def a_star(self, id_start, id_celu):
        return self.algorytm(id_start, id_celu)

    def dijkstra(self, id_start, id_celu):
        return self.algorytm(id_start, id_celu)

    def algorytm(self, id_start, id_celu):
        id_wierzchołków_do_sprawdzenia = [id_start]
        id_poprzednika = dict()

        koszt_ze_startu = dict()
        for id_wierzchołka in self.wierzchołki.keys():
            koszt_ze_startu[id_wierzchołka] = float("inf")
            
        koszt_ze_startu[id_start] = 0

        koszt_do_celu = dict()
        for id_wierzchołka, wierzchołek in self.wierzchołki.items():
            koszt_do_celu[id_wierzchołka] = wierzchołek.heurystyka

        odwiedzonych_wierzchołków = 0
        
        while(len(id_wierzchołków_do_sprawdzenia) != 0):
            id_aktualnego = id_wierzchołków_do_sprawdzenia[0]

            for i in range(1, len(id_wierzchołków_do_sprawdzenia)):
                if koszt_do_celu[id_wierzchołków_do_sprawdzenia[i]] < koszt_do_celu[id_aktualnego]:
                    id_aktualnego = id_wierzchołków_do_sprawdzenia[i]

            odwiedzonych_wierzchołków += 1

            if id_aktualnego == id_celu:
                return self.ścieżka(id_poprzednika, id_aktualnego), koszt_ze_startu[id_celu], odwiedzonych_wierzchołków
            
            id_wierzchołków_do_sprawdzenia.remove(id_aktualnego)

            for (sąsiad, koszt) in self.wierzchołki.get(id_aktualnego).sąsiedzi:
                możliwy_koszt_ze_startu = koszt_ze_startu[id_aktualnego] + koszt

                if możliwy_koszt_ze_startu < koszt_ze_startu[sąsiad]:
                    id_poprzednika[sąsiad] = id_aktualnego
                    koszt_ze_startu[sąsiad] = możliwy_koszt_ze_startu
                    koszt_do_celu[sąsiad] = koszt_ze_startu[sąsiad] + self.wierzchołki.get(sąsiad).heurystyka

                    if sąsiad not in id_wierzchołków_do_sprawdzenia:
                        id_wierzchołków_do_sprawdzenia.append(sąsiad)

        return list(), -1, odwiedzonych_wierzchołków

    def ścieżka(self, id_poprzednika, id_celu):
        odp = [id_celu]
        while(id_celu in id_poprzednika.keys()):
            id_celu = id_poprzednika[id_celu]
            odp.insert(0, id_celu)
        return odp