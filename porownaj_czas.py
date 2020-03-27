#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from wierzcholek import Graf
from time import perf_counter
from bruteforce import bruteforce
from bruteforce2 import bruteforce2
from re import findall

nazwy_plików = ["graf100", "graf1", "graf2", "graf3"]

for nazwa in nazwy_plików:
    print(f"Plik {nazwa}")
    id_celu = str(int(findall(r'\d+', nazwa)[-1]) * 10**6 - 1) #szuka ostatniej liczby w ciągu znaków, np. "graf1000" -> 1000
    if(nazwa == "graf100"):
        id_celu = "99"
    id_start = str(int(int(id_celu) / 2)) #wychodzimy ze środka grafu

    graf = Graf()
    graf.czytaj_plik(nazwa)

    początek = perf_counter()
    bruteforce2(graf, id_start, id_celu)
    koniec = perf_counter()
    print(f"czas bruteforce: {koniec - początek}")

    początek = perf_counter()
    graf.dijkstra(id_start, id_celu)
    koniec = perf_counter()
    print(f"czas dijkstra: {koniec - początek}")

    graf.oblicz_heurystykę(id_celu)
    początek = perf_counter()
    wynik = graf.a_star(id_start, id_celu)
    koniec = perf_counter()
    print(f"czas A*: {koniec - początek}")