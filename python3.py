password="cybersquare"
guess=""
while password!=guess:
    guess=input('enter password: ')
    if password==guess:
        print('login success')
    else:
        print('incorrect password ...Try again')