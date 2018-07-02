from random import randint


def grandmaw_input():
    print('AYE SONNY BOY!')
    while True:
        response = input('>>>')
        if response != response.upper():
            print('SPEAK UP SONNY BOY!')

        elif response == 'BYE':
            print('OH LEAVING SO SOON SONNY!')
            break

        elif response == response.upper():
            print('NOT SINCE,', str(randint(1940, 1988)) + '!')


def main():
    grandmaw_input()


if __name__ == "__main__":
    main()
