#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from wierzcholek import Wierzchołek, Graf

graf = Graf()
graf.czytaj_plik("wejscie.txt")
assert graf.wierzchołki.get('1').sąsiedzi == [('2',4), ('3',2), ('6',3)]
assert graf.wierzchołki.get('2').sąsiedzi == [('1',4), ('3',3), ('4',5)]
assert graf.wierzchołki.get('3').sąsiedzi == [('2',3), ('1',2), ('4',3), ('5',2), ('6',4)]
assert graf.wierzchołki.get('4').sąsiedzi == [('2',5), ('3',3), ('5',1)]
assert graf.wierzchołki.get('5').sąsiedzi == [('4',1), ('3',2), ('6',4)]
assert graf.wierzchołki.get('6').sąsiedzi == [('5',4), ('3',4), ('1',3)]

assert graf.krawędzieMalejąco == [5, 4, 4, 4, 3, 3, 3, 2, 2, 1]