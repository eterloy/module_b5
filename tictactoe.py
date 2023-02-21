#Игра крестики-нолики

def greeting():#приветствие в игре
    print("------------------------")
    print("Приветсвуем Вас в игре")
    print(" Крестики - Нолики")
    print("Формат ввода: х, у")
    print("------------------------")
    print(" х - номер строки")
    print(" у - номер столбца")
    print("------------------------")

def game_board():
    # Игровое поле
    print(f"    0 | 1 | 2 |")
    for i in range(3):
        print(f"{i} | {champ[i][0]} | {champ[i][1]} | {champ[i][2]} |")
        print("---------------")

def pas():
    #Игроки вводят координаты хода
    while True:
        cords = input("ваш ход: ").split()
        if len(cords) != 2:
            print("Введите координаты через пробел.")
            continue

        x, y = cords
        if not (x.isdigit() and y.isdigit()):
            print("Введите числа: ")
            continue

        x, y = int(x), int(y)
        if not (0 <= x <= 2 and 0 <= y <= 2):
            print("Некорректные координаты")
            continue

        if champ[x][y] != " ":
            print("Клетка занята!")
            continue

        return x, y

def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for i in cord:
            symbols.append(champ[i[0]][i[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!")
            return True

greeting()
champ = [[" "] * 3 for i in range(3)]
count = 0

while True:
    count += 1
    game_board()
    if count % 2 == 0:
        print("Ходит крестик")
    else:
        print("Ходит нолик")

    x, y = pas()

    if count % 2 == 0:
        champ[x][y] = 'Х'
    else:
        champ[x][y] = '0'

    if check_win():
        break

    if count == 9:
        print("Ничья!")
        break