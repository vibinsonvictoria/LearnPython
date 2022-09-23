'''
    Read input from the user.
    if the number is matched with secret number then print 'Won the game'
    otherwise continue the process.

'''

if __name__ == '__main__':
    secret_number = 12
    while True:
        try:

            user_response = int(input('Enter a Number :'))
        except:
            print('oops.. Required Integer Type')
            continue
        else:
            if user_response == secret_number:
                print('You Won the game :)')
                break
            else:
                print('Not matched.. Try again..')
                continue
