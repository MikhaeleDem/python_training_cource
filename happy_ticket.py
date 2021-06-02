"""Проверка счастливого билета"""
a = (input())
A=int(a[0])
B=int(a[1])
C=int(a[2])
D=int(a[3])
E=int(a[4])
F=int(a[5])
SUM1 = A+B+C
SUM2 = D+E+F
if SUM1==SUM2:
    print('Счастливый')
else:
    print('Обычный')