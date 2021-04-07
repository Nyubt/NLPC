luna=int(input('Introduceti luna'))
an=int(input('Introduceti anul'))
#afisat numarul de zile din luna
if luna == 1 or luna == 3 or luna == 5 or luna == 7 or luna == 8 or luna == 10 or luna == 12:
    print('31 zile')
elif luna == 4 or luna == 6 or luna == 9 or luna == 11:
    print('30 zile')
elif luna == 2:
    if an%4 == 0 and an%100 != 0:
        print('29 zile')
    elif an%400 == 0:
        print('29 zile')
    else:
        print('28 zile')
else:
    print('Eroare')
