#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from wierzcholek import Graf
from time import perf_counter
from bruteforce import bruteforce
from bruteforce2 import bruteforce2
from re import findall
from os.path import isfile

nazwy_plików = ["graf1000000", "graf2000000", "graf3000000", "drzewo50000", "drzewo1000000", "drzewo10000000"]

for nazwa in nazwy_plików:
    print(f"Plik {nazwa}")
    id_celu = str(int(findall(r'\d+', nazwa)[-1]) - 1) #szuka ostatniej liczby w ciągu znaków, np. "graf1000" -> 1000
    if "graf" in nazwa:
        id_start = str(int(int(id_celu) / 2)) #wychodzimy ze środka grafu
    else:
        id_start = '0'  

    graf = Graf()
    graf.czytaj_plik(nazwa)

    if nazwa not in ["drzewo1000000", "drzewo10000000"]:
        #początek = perf_counter()
        #bruteforce2(graf, id_start, id_celu)
        #koniec = perf_counter()
        #print(f"czas bruteforce: {koniec - początek}")

        początek = perf_counter()
        ścieżka_dijkstra, koszt_dijkstra, odwiedzonych_dijkstra = graf.dijkstra(id_start, id_celu)
        koniec = perf_counter()
        print(f"czas dijkstra: {koniec - początek}, odwiedzono {odwiedzonych_dijkstra} wierzcholki")

    graf.oblicz_heurystykę(id_celu)
    początek = perf_counter()
    ścieżka_astar, koszt_astar, odwiedzonych_astar = graf.a_star(id_start, id_celu)
    koniec = perf_counter()
    print(f"czas A*: {koniec - początek}, odwiedzono {odwiedzonych_astar} wierzcholki")

    if nazwa not in ["drzewo1000000", "drzewo10000000"]:
        assert koszt_dijkstra == koszt_astar