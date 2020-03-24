from wierzcholek import Graf

graf = Graf()
graf.czytaj_plik("wejscie.txt")

assert graf.a_star('1', '2') == ['1','2']
assert graf.a_star('1', '3') == ['1','3']
assert graf.a_star('1', '4') == ['1','3','4']
assert graf.a_star('1', '5') == ['1','3','5']
assert graf.a_star('1', '6') == ['1','6']

assert graf.a_star('2', '1') == ['2','1']
assert graf.a_star('2', '3') == ['2','3']
assert graf.a_star('2', '4') == ['2','4']
assert graf.a_star('2', '5') in [['2','3','5'], ['2','4','5']]
assert graf.a_star('2', '6') in [['2','3','6'], ['2','1','6']]

assert graf.a_star('3', '1') == ['3','1']
assert graf.a_star('3', '2') == ['3','2']
assert graf.a_star('3', '4') in [['3','4'], ['3','5','4']]
assert graf.a_star('3', '5') == ['3','5']
assert graf.a_star('3', '6') == ['3','6']

assert graf.a_star('4', '1') == ['4','3','1']
assert graf.a_star('4', '2') == ['4','2']
assert graf.a_star('4', '3') in [['4','3'], ['4','5','3']]
assert graf.a_star('4', '5') == ['4','5']
assert graf.a_star('4', '6') == ['4','5','6']

assert graf.a_star('5', '1') == ['5','3','1']
assert graf.a_star('5', '2') in [['5','3','2'], ['5','4','2']]
assert graf.a_star('5', '3') == ['5','3']
assert graf.a_star('5', '4') == ['5','4']
assert graf.a_star('5', '6') == ['5','6']

assert graf.a_star('6', '1') == ['6','1']
assert graf.a_star('6', '2') in [['6','3','2'], ['6','1','2']]
assert graf.a_star('6', '3') == ['6','3']
assert graf.a_star('6', '4') == ['6','5','4']
assert graf.a_star('6', '5') == ['6','5']