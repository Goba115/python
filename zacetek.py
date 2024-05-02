while True:
    x = input('Vpiši številko: ')
    if len(x) == 0:
        continue
        
    x = int(x)

    if x == 5:
        print(f'Število {x} JE enako 5')
    else:
        print(f'Število {x} NI enako 5')

    print()
