#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 01:18:23 2020

@author: kristofer
"""

def bruteforce(graf, id_startowe, id_celowe):
    # lista odwiedzonych już wierzchołków
    odwiedzone = []
    id_startowe = str(id_startowe)
    id_celowe = str(id_celowe)
    
    ścieżki = []
    koszty = []
    
    def przeszukaj_sąsiadów(id_obecne, odwiedzone, koszt):
        odwiedzone = list(odwiedzone)
        odwiedzone.append(id_obecne)
        
        if id_obecne == id_celowe:
            nonlocal ścieżki
            nonlocal koszty
            ścieżki.append(odwiedzone)
            koszty.append(koszt)
            #print('Wynik: ', odwiedzone, ', ', koszt)
            return
        
        for sąsiad in graf.wierzchołki[id_obecne].sąsiedzi:
            id_sąsiada = sąsiad[0]
            if id_sąsiada not in odwiedzone:
                koszt_sąsiada = koszt + sąsiad[1]
                przeszukaj_sąsiadów(id_sąsiada, odwiedzone, koszt_sąsiada)
    
    przeszukaj_sąsiadów(id_startowe, odwiedzone, 0)
    
    #print('Ścieżka: ', ścieżki[koszty.index(min(koszty))])
    #print('Koszt: ', min(koszty))
    
    return ścieżki[koszty.index(min(koszty))]