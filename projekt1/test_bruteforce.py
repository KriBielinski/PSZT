#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from wierzcholek import Graf
from bruteforce import bruteforce

def test_bruteforce():
    graf = Graf()
    graf.czytaj_plik("wejscie.txt")

    assert bruteforce(graf, '1', '2') == ['1','2']
    assert bruteforce(graf, '1', '3') == ['1','3']
    assert bruteforce(graf, '1', '4') == ['1','3','4']
    assert bruteforce(graf, '1', '5') == ['1','3','5']
    assert bruteforce(graf, '1', '6') == ['1','6']

    assert bruteforce(graf, '2', '1') == ['2','1']
    assert bruteforce(graf, '2', '3') == ['2','3']
    assert bruteforce(graf, '2', '4') == ['2','4']
    assert bruteforce(graf, '2', '5') in [['2','3','5'], ['2','4','5']]
    assert bruteforce(graf, '2', '6') in [['2','3','6'], ['2','1','6']]

    assert bruteforce(graf, '3', '1') == ['3','1']
    assert bruteforce(graf, '3', '2') == ['3','2']
    assert bruteforce(graf, '3', '4') in [['3','4'], ['3','5','4']]
    assert bruteforce(graf, '3', '5') == ['3','5']
    assert bruteforce(graf, '3', '6') == ['3','6']

    assert bruteforce(graf, '4', '1') == ['4','3','1']
    assert bruteforce(graf, '4', '2') == ['4','2']
    assert bruteforce(graf, '4', '3') in [['4','3'], ['4','5','3']]
    assert bruteforce(graf, '4', '5') == ['4','5']
    assert bruteforce(graf, '4', '6') == ['4','5','6']

    assert bruteforce(graf, '5', '1') == ['5','3','1']
    assert bruteforce(graf, '5', '2') in [['5','3','2'], ['5','4','2']]
    assert bruteforce(graf, '5', '3') == ['5','3']
    assert bruteforce(graf, '5', '4') == ['5','4']
    assert bruteforce(graf, '5', '6') == ['5','6']

    assert bruteforce(graf, '6', '1') == ['6','1']
    assert bruteforce(graf, '6', '2') in [['6','3','2'], ['6','1','2']]
    assert bruteforce(graf, '6', '3') == ['6','3']
    assert bruteforce(graf, '6', '4') == ['6','5','4']
    assert bruteforce(graf, '6', '5') == ['6','5']