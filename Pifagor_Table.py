"""a = int(input())
b = int(input())
c = int(input())
d = int(input())
for j in range(c, (d + 1)):
    print('\t', j, end='')
for i in range(a, (b+1)):
    print('\n', i, end='')
for j in range(c, d+1):
    for i in range(a, b+1):
        # Extra space?
        if i * j < 10:
            print(" ", end="")

        print('\n', i * j, end=" ")

    # Move down to the next row
    print()"""

a = int(input())
b = int(input())
c = int(input())
d = int(input())
for j in range(c, (d + 1)): # ранжируем столбцы
        print('\t', j, end='') # говорим, что хотим в строку с пробелом в конце расписать все символы из j
for i in range(a, (b+1)): # ранжируем строки
        print('\n', i, end='') # говорим, что хотим в столбец с пробелом внизу расписать все символы из j
        for j in range(c, d+1): # Встраиваем цикл перемножения
                print('\t', i * j, end="")
