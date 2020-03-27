#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from wierzcholek import Graf

def test_dijkstra():
    graf = Graf()
    graf.czytaj_plik("wejscie.txt")

    assert graf.dijkstra('1', '2') == ['1','2']
    assert graf.dijkstra('1', '3') == ['1','3']
    assert graf.dijkstra('1', '4') == ['1','3','4']
    assert graf.dijkstra('1', '5') == ['1','3','5']
    assert graf.dijkstra('1', '6') == ['1','6']

    assert graf.dijkstra('2', '1') == ['2','1']
    assert graf.dijkstra('2', '3') == ['2','3']
    assert graf.dijkstra('2', '4') == ['2','4']
    assert graf.dijkstra('2', '5') in [['2','3','5'], ['2','4','5']]
    assert graf.dijkstra('2', '6') in [['2','3','6'], ['2','1','6']]

    assert graf.dijkstra('3', '1') == ['3','1']
    assert graf.dijkstra('3', '2') == ['3','2']
    assert graf.dijkstra('3', '4') in [['3','4'], ['3','5','4']]
    assert graf.dijkstra('3', '5') == ['3','5']
    assert graf.dijkstra('3', '6') == ['3','6']

    assert graf.dijkstra('4', '1') == ['4','3','1']
    assert graf.dijkstra('4', '2') == ['4','2']
    assert graf.dijkstra('4', '3') in [['4','3'], ['4','5','3']]
    assert graf.dijkstra('4', '5') == ['4','5']
    assert graf.dijkstra('4', '6') == ['4','5','6']

    assert graf.dijkstra('5', '1') == ['5','3','1']
    assert graf.dijkstra('5', '2') in [['5','3','2'], ['5','4','2']]
    assert graf.dijkstra('5', '3') == ['5','3']
    assert graf.dijkstra('5', '4') == ['5','4']
    assert graf.dijkstra('5', '6') == ['5','6']

    assert graf.dijkstra('6', '1') == ['6','1']
    assert graf.dijkstra('6', '2') in [['6','3','2'], ['6','1','2']]
    assert graf.dijkstra('6', '3') == ['6','3']
    assert graf.dijkstra('6', '4') == ['6','5','4']
    assert graf.dijkstra('6', '5') == ['6','5']