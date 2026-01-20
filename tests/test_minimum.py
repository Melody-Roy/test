from minimum import minimum_de_trois

def test_minimum_simple():
    assert minimum_de_trois(3, 7, 2) == 2

def test_minimum_negatif():
    assert minimum_de_trois(-5, 10, 0) == -5

def test_minimum_egalite():
    assert minimum_de_trois(4, 4, 4) == 4

def test_minimum_flottants():
    assert minimum_de_trois(3.2, 1.1, 1.5) == 1.1

def test_minimum_deux_egaux():
    assert minimum_de_trois(8, 8, 2) == 2