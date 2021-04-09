luna=int(input('Introduceti luna'))
an=int(input('Introduceti anul'))
#afisat numarul de zile din luna
if luna in [1,3,5,7,8,10,12]:
    print('31 zile')
elif luna in [4,6,9,11]:
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
