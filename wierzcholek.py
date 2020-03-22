#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Wierzchołek:
    def __init__(self, sąsiedzi=None):
        # lista sąsiadów w postaci '(id sąsiada, koszt dojazdu do sąsiada)'
        self.sąsiedzi = sąsiedzi