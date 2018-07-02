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
            print('NOT SINCE THE GOOD OLE DAYS!')


def main():
    grandmaw_input()


if __name__ == "__main__":
    main()
