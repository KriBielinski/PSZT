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