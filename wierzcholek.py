#!/usr/bin/env python3
# -*- coding: utf-8 -*-

maxZapamiętanychKrawędzi = 100

class Wierzchołek:
    def __init__(self, sąsiedzi=[]):
        self.sąsiedzi = list(sąsiedzi)
        
    def dodaj_sąsiada(self, id_celu, koszt):
        self.sąsiedzi.append((id_celu, float(koszt)))

class Graf:
    def __init__(self, wierzchołki={}):
        self.wierzchołki = dict(wierzchołki)
        self.krawędzieMalejąco = list()
        
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
            if(len(self.krawędzieMalejąco) < maxZapamiętanychKrawędzi):
                self.krawędzieMalejąco.append((float)(koszt))
            self.dodaj_wierzchołek(id_swoje, id_celu, koszt)
        self.krawędzieMalejąco.sort(reverse=True)
        plik.close()