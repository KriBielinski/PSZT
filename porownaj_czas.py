#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from wierzcholek import Graf
from bruteforce import bruteforce
from bruteforce2 import bruteforce2
from re import findall
from os.path import isfile

nazwy_plików = ["graf10", "graf20", "graf1000000", "graf2000000", "graf3000000", "drzewo50000", "drzewo1000000", "drzewo10000000"]
licz_bruteforce = True
licz_dijkstra = True

for nazwa in nazwy_plików:
    print(f"Plik {nazwa}")
    id_celu = str(int(findall(r'\d+', nazwa)[-1]) - 1) #szuka ostatniej liczby w ciągu znaków, np. "graf1000" -> 1000
    if "graf" in nazwa:
        id_start = str(int(int(id_celu) / 2)) #wychodzimy ze środka grafu
    else:
        id_start = '0'  

    graf = Graf()
    graf.czytaj_plik(nazwa)

    if licz_bruteforce:
        ścieżka_brueforce, koszt_bruteforce, odwiedzonych_bruteforce, czas_bruteforce = bruteforce(graf, id_start, id_celu)
        print(f"czas bruteforce: {czas_bruteforce}, odwiedzono {odwiedzonych_bruteforce} wierzcholki")
        if czas_bruteforce >= 60:
            licz_bruteforce = False

    if licz_dijkstra:
        ścieżka_dijkstra, koszt_dijkstra, odwiedzonych_dijkstra, czas_dijkstra = graf.dijkstra(id_start, id_celu)
        print(f"czas dijkstra: {czas_dijkstra}, odwiedzono {odwiedzonych_dijkstra} wierzcholki")
        if czas_dijkstra >= 60:
            licz_dijkstra = False

    ścieżka_astar, koszt_astar, odwiedzonych_astar, czas_astar = graf.a_star(id_start, id_celu)
    print(f"czas A*: {czas_astar}, odwiedzono {odwiedzonych_astar} wierzcholki")

    if licz_bruteforce:
        assert koszt_bruteforce == koszt_astar
    if licz_dijkstra:
        assert koszt_dijkstra == koszt_astar