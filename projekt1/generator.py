#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv
from random import uniform

def wygeneruj_graf(nazwa_pliku, ilość_wierzchołków):
    plik_wyjściowy = open(nazwa_pliku, "w")

    for i in range(0, ilość_wierzchołków):
        for j in range(i + 1, min(ilość_wierzchołków, i + 11)):
            plik_wyjściowy.write(str(i) + " " + str(j) + " " + str(int(uniform(1, 1000))) + "\n")
    
    plik_wyjściowy.close()

def wygeneruj_drzewo_binarne(nazwa_pliku, ilość_wierzchołków):
    plik_wyjściowy = open(nazwa_pliku, "w")

    id_aktualne = 0
    while id_aktualne < ilość_wierzchołków:
        id_następne = id_aktualne * 2 + 1
        if(id_następne < ilość_wierzchołków):
            plik_wyjściowy.write(str(id_aktualne) + " " + str(id_następne) + " " + "1" + "\n")
            if(id_następne + 1 < ilość_wierzchołków):
                plik_wyjściowy.write(str(id_aktualne) + " " + str(id_następne + 1) + " " + "1" + "\n")
        id_aktualne += 1

    plik_wyjściowy.close()