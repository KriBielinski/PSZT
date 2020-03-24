#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 01:20:33 2020

@author: kristofer
"""

def bruteforce2(graf, id_startowe, id_celowe):
    
    class Węzeł:
        def __init__(self, id_obecne, węzeł_poprzedni):
            self.id = str(id_obecne)
            self.węzeł_poprzedni = węzeł_poprzedni
        
    def lista_id(węzeł):
        wynik = [węzeł.id]
        root = węzeł
        while(root.węzeł_poprzedni is not None):
            wynik.append(root.węzeł_poprzedni.id)
            root = root.węzeł_poprzedni
        return list(reversed(wynik))
    
    id_startowe = str(id_startowe)
    id_celowe = str(id_celowe)
    
    ścieżki = []
    koszty = []
    
    def przeszukaj_sąsiadów(id_obecne, odwiedzony, koszt):
        węzeł_obecny = Węzeł(id_obecne, odwiedzony)
        
        if id_obecne == id_celowe:
            nonlocal ścieżki
            nonlocal koszty
            ścieżki.append(węzeł_obecny)
            koszty.append(koszt)
            #print('Wynik: ', lista_id(węzeł_obecny), ', ', koszt)
            return
        
        for sąsiad in graf.wierzchołki[id_obecne].sąsiedzi:
            id_sąsiada = sąsiad[0]
            if id_sąsiada not in lista_id(węzeł_obecny):
                koszt_sąsiada = koszt + sąsiad[1]
                przeszukaj_sąsiadów(id_sąsiada, węzeł_obecny, koszt_sąsiada)
    
    przeszukaj_sąsiadów(id_startowe, None, 0)
    
    print('Ścieżka: ', lista_id(ścieżki[koszty.index(min(koszty))]))
    print('Koszt: ', min(koszty))