#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from generator import wygeneruj_graf, wygeneruj_drzewo_binarne

wygeneruj_graf("graf1000000", 1000000)
wygeneruj_graf("graf2000000", 2000000)
wygeneruj_graf("graf3000000", 3000000)
wygeneruj_graf("graf10", 10)

wygeneruj_drzewo_binarne("drzewo50000", 50000)
wygeneruj_drzewo_binarne("drzewo1000000", 1000000)
wygeneruj_drzewo_binarne("drzewo10000000", 10000000)