def x_move(board):
    while True:
        response = input('It is your move X >>> ')

        if response == '1':
            board[0].insert(1, 'X')
            board[0].remove('1')
            return board
        elif response == '2':
            board[0].insert(2, 'X')
            board[0].remove('2')
            return board
        elif response == '3':
            board[0].insert(3, 'X')
            board[0].remove('3')
            return board
        elif response == '4':
            board[1].insert(1, 'X')
            board[1].remove('4')
            return board
        elif response == '5':
            board[1].insert(2, 'X')
            board[1].remove('5')
            return board
        elif response == '6':
            board[1].insert(3, 'X')
            board[1].remove('6')
            return board
        elif response == '7':
            board[2].insert(1, 'X')
            board[2].remove('7')
            return board
        elif response == '8':
            board[2].insert(2, 'X')
            board[2].remove('8')
            return board
        elif response == '9':
            board[2].insert(3, 'X')
            board[2].remove('9')
            return board
        else:
            print('Please input a valid number.')

        print(board[0])
        print(board[1])
        print(board[2])


def o_move(board):
    while True:
        response = input('It is your move O >>> ')

        if response == '1':
            board[0].insert(1, 'O')
            board[0].remove('1')
            return board
        elif response == '2':
            board[0].insert(2, 'O')
            board[0].remove('2')
            return board
        elif response == '3':
            board[0].insert(3, 'O')
            board[0].remove('3')
            return board
        elif response == '4':
            board[1].insert(1, 'O')
            board[1].remove('4')
            return board
        elif response == '5':
            board[1].insert(2, 'O')
            board[1].remove('5')
            return board
        elif response == '6':
            board[1].insert(3, 'O')
            board[1].remove('6')
            return board
        elif response == '7':
            board[2].insert(1, 'O')
            board[2].remove('7')
            return board
        elif response == '8':
            board[2].insert(2, 'O')
            board[2].remove('8')
            return board
        elif response == '9':
            board[2].insert(3, 'O')
            board[2].remove('9')
            return
        else:
            print('Please input a valid number.')

        print(board[0])
        print(board[1])
        print(board[2])


#def winner(board):
#    if board[0][1]
#elif response


def main():
    board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    for key in board:
        print(key)
    while True:
        x_move(board)
        o_move(board)


if __name__ == '__main__':
    main()
