from bcca.test import should_print, with_inputs
from blackjack import *

deck = [
    'Ace', 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 'Ace', 10, 10, 10, 9, 8, 7, 6,
    5, 4, 3, 2, 'Ace', 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 'Ace', 10, 10, 10,
    9, 8, 7, 6, 5, 4, 3, 2
]


def test_card_total():
    assert card_total([3, 2, 1]) == 6
    assert card_total([10, 5, 6]) == 21


def test_card_total_1():
    assert card_total(['Ace', 5, 5]) == 21
    assert card_total(['Ace', 2, 1]) == 14
    assert card_total(['Ace', 10, 10]) == 21


def test_card_total_2():
    assert card_total(['Ace', 'Ace', 6, 3]) == 21
    assert card_total(['Ace', 'Ace', 3, 3]) == 18
    assert card_total(['Ace', 'Ace', 10, 9]) == 21


def test_card_total_3():
    assert card_total(['Ace', 'Ace', 'Ace', 8]) == 21
    assert card_total(['Ace', 'Ace', 'Ace', 2, 3]) == 18
    assert card_total(['Ace', 'Ace', 'Ace', 10, 8]) == 21


def test_card_total_4():
    assert card_total(['Ace', 'Ace', 'Ace', 'Ace', 7]) == 21
    assert card_total(['Ace', 'Ace', 'Ace', 'Ace', 5]) == 19
    assert card_total(['Ace', 'Ace', 'Ace', 'Ace', 10, 7]) == 21
