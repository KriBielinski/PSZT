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
    
    def przeszukaj_sąsiadów(id_obecne, odwiedzone):
        odwiedzone = list(odwiedzone)
        odwiedzone.append(id_obecne)
        
        if id_obecne == id_celowe:
            print('Wynik: ', odwiedzone)
            return
        
        for sąsiad in graf.wierzchołki[id_obecne].sąsiedzi:
            id_sąsiada = sąsiad[0]
            if id_sąsiada not in odwiedzone:
                przeszukaj_sąsiadów(id_sąsiada, odwiedzone)
    
    przeszukaj_sąsiadów(id_startowe, odwiedzone)