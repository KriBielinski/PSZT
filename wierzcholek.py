#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Wierzchołek:
    def __init__(self, sąsiedzi=[]):
        # lista sąsiadów w postaci '(id sąsiada, koszt dojazdu do sąsiada)'
        self.sąsiedzi = list(sąsiedzi)

class Graf:
    def __init__(self, wierzchołki={}):
        # słownik wierzchołków w grafie '{id -> Wierzchołek}'
        self.wierzchołki = dict(wierzchołki)