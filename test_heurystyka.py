#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from wierzcholek import Graf

graf = Graf()
graf.czytaj_plik("wejscie.txt")
graf.oblicz_heurystykę(id_celu='5')

assert graf.wierzchołki.get('5').heurystyka == 0
assert graf.wierzchołki.get('3').heurystyka == 1
assert graf.wierzchołki.get('4').heurystyka == 1
assert graf.wierzchołki.get('6').heurystyka == 1
assert graf.wierzchołki.get('2').heurystyka == 3
assert graf.wierzchołki.get('1').heurystyka == 3