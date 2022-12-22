winner = True
counter = 0
number_1_1 = ' '
number_1_2 = ' '
number_1_3 = ' '
number_2_1 = ' '
number_2_2 = ' '
number_2_3 = ' '
number_3_1 = ' '
number_3_2 = ' '
number_3_3 = ' '
while winner:
    counter += 1
    if counter % 2 == 0:
        XO = 'X'
    else:
        XO = 'O'
    print(f'Turn: {XO}')
    line = int(input())
    column = int(input())
    if line == 1:
        if column == 1:
            number_1_1 = XO
        elif column == 2:
            number_1_2 = XO
        elif column == 3:
            number_1_3 = XO
        if number_1_1 == XO and number_1_2 == XO and number_1_3 == XO:
            print(f'Winner is {XO}!!! ')
            winner = False
    elif line == 2:
        if column == 1:
            number_2_1 = XO
        elif column == 2:
            number_2_2 = XO
        elif column == 3:
            number_2_3 = XO
        if number_2_1 == XO and number_2_2 == XO and number_2_3 == XO:
            print(f'Winner is {XO}!!! ')
            winner = False
    elif line == 3:
        if column == 1:
            number_3_1 = XO
        elif column == 2:
            number_3_2 = XO
        elif column == 3:
            number_3_3 = XO
        if number_3_1 == XO and number_3_2 == XO and number_3_3 == XO:
            print(f'Winner is {XO}!!! ')
            winner = False
    if number_1_1 == XO and number_2_1 == XO and number_3_1 == XO:
        print(f'Winner is {XO}!!! ')
        winner = False
    elif number_1_2 == XO and number_2_2 == XO and number_3_2 == XO:
        print(f'Winner is {XO}!!! ')
        winner = False
    elif number_1_3 == XO and number_2_3 == XO and number_3_3 == XO:
        print(f'Winner is {XO}!!! ')
        winner = False
    elif number_1_1 == XO and number_2_2 == XO and number_3_3 == XO:
        print(f'Winner is {XO}!!! ')
        winner = False
    elif number_1_3 == XO and number_2_2 == XO and number_3_1 == XO:
        print(f'Winner is {XO}!!! ')
        winner = False

    print(f'_______')
    print(f'|{number_1_1}|{number_1_2}|{number_1_3}|')
    print(f'_______')
    print(f'|{number_2_1}|{number_2_2}|{number_2_3}|')
    print(f'_______')
    print(f'|{number_3_1}|{number_3_2}|{number_3_3}|')
    print(f'_______')
