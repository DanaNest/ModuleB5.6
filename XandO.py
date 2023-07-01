print('Игра крестики-нолики против компьютера')
#Игровое поле
playing_field = [1, 2, 3,
                 4, 5, 6,
                 7, 8, 9]

#Функция для вывода игрового поля на экран
def print_playing_field():
    print(playing_field[0], ' ', playing_field[1], ' ', playing_field[2])
    print(playing_field[3], ' ', playing_field[4], ' ', playing_field[5])
    print(playing_field[6], ' ', playing_field[7], ' ', playing_field[8])

#Вариации побед
wins = [[0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6], [0, 1, 2], [3, 4, 5], [6, 7, 8]]

#Ход в ячейку
def step_field(step,symbol):
    ind = playing_field.index(step)
    playing_field[ind] = symbol



#Текущий результат
def get_result():
    win = ''
    for i in wins:
        if playing_field[i[0]] == 'X' and playing_field[i[1]] == 'X' and playing_field[i[2]] == 'X':
            win = 'Человек'
        if playing_field[i[0]] == 'O' and playing_field[i[1]] == 'O' and playing_field[i[2]] == 'O':
            win = 'Компьютер'
    return win

#для компьютера: поиск правильного хода
def check_step(sum_O, sum_X):
    step= ''
    for i in wins:
        o = 0
        x = 0
        for j in range(0, 3):
            if playing_field[i[j]] == 'O':
                o += 1
            if playing_field[i[j]] == 'X':
                x += 1
        if o == sum_O and x == sum_X:
            for j in range(0, 3):
                if playing_field[i[j]] != 'O' and playing_field[i[j]] != 'X':
                    step = playing_field[i[j]]
    return step

#выбор хода для компьютера
def computer():
    step = ''

#вариант 1: если есть 2 своих в победной линии - ставим в эту линию
    step = check_step(2, 0)

#вариант 2: если 2 чужих в победной линии = ставим в эту линию
    if step == '':
        step = check_step(0, 2)

#вариант 3: если 1 своя и нет чужих = ставим в линию
    if step == '':
        step = check_step(1, 0)

# вариант 4: занимаем центр, если пустой
    if step == '':
        if playing_field[4] != 'X' and playing_field[4] !='O':
            step = 5

#вариант 5: если центр занят, ставим в 0 ячейку
    if step == '':
        if playing_field[0] != 'X' and playing_field[0] != 'O':
            step = 1

    return step

#игра
game_over = False
human = True

while game_over ==False:
#показываем поле
    print_playing_field()
#ход человека
    if human == True:
        symbol = 'X'
        step = int(input('Выберите число: '))

#ход компьютера
    else:
        print('Компьютер сделал ход')
        symbol = 'O'
        step = computer()
#если есть куда делать ход, то игра продолжается, иначе - ничья
    if step != '':
        step_field(step, symbol) #ход в указанную ячейку
        win = get_result()       #проверка победителя
        if win != '':
            game_over = True
        else:
            game_over = False
    else:
        print('Ничья')
        game_over = True
        win = 'Дружба'

    human = not (human)

print_playing_field()
print(f'Победитель {win}')