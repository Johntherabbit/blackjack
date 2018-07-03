from random import shuffle


def deal():
    cards = [
        13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 13, 12, 11, 10, 9, 8, 7, 6, 5,
        4, 3, 2, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 13, 12, 11, 10, 9, 8,
        7, 6, 5, 4, 3, 2
    ]
    shuffle(cards)
    deck_1 = cards[26:]
    pile_1 = []
    deck_2 = cards[:26]
    pile_2 = []

    while True:
        if len(deck_1) == 0:
            shuffle(pile_1)
            deck_1 = pile_1.copy()
            pile_1 = []

        if len(deck_1) == 0:
            print('Player two wins!')
            break

        if len(deck_2) == 0:
            shuffle(pile_2)
            deck_2 = pile_2.copy()
            pile_2 = []

        if len(deck_2) == 0:
            print('Player one wins!')
            break

        x = deck_1.pop()
        y = deck_2.pop()

        print(
            "Player 1: Drew {}\nLength of Hand: {}\nvs\nPlayer 2: Drew {}\nLength of Hand: {}".
            format(x, len(deck_1), y, len(deck_2)))
        print()
        #input()

        if x > y:
            pile_1.extend([x, y])
        elif x < y:
            pile_2.extend([x, y])


def main():

    deal()


if __name__ == '__main__':
    main()
