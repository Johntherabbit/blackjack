from random import shuffle


def deal():
    cards = [
        13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 13, 12, 11, 10, 9, 8, 7, 6, 5,
        4, 3, 2, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 13, 12, 11, 10, 9, 8,
        7, 6, 5, 4, 3, 2
    ]
    shuffle(cards)
    deck_1 = cards[26:]
    new_deck_1 = []
    deck_2 = cards[:26]
    new_deck_2 = []

    while True:

        x = deck_1.pop()
        y = deck_2.pop()

        print("Player 1: Drew {}\nvs\nPlayer 2: Drew {}".format(x, y))
        print()
        #input()

        if x > y:
            new_deck_1.extend([x, y])
        elif x < y:
            new_deck_2.extend([x, y])

        if deck_1 == []:
            shuffle(new_deck_1)
            x = new_deck_1.pop()
            y = new_deck_2.pop()
            if x > y:
                deck_1.extend([x, y])
            elif new_deck_1 == []:
                print('$$$$$$$$')
                print('Player 2 Wins!')
                print('$$$$$$$$')
                print()
            return

        if deck_2 == []:
            shuffle(new_deck_2)
            x = new_deck_1.pop()
            y = new_deck_2.pop()
            if x < y:
                deck_2.extend([x, y])
            elif new_deck_2 == []:
                print('$$$$$$$$')
                print('Player 1 Wins!')
                print('$$$$$$$$')
                print()
            return


def main():

    deal()


if __name__ == '__main__':
    main()
