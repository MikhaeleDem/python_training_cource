'''Вводим цифры, пока не введем 0. Всё введенное суммируется'''
'''a = int(input())
s = 0
while a != 0:
    s += a
    a = int(input())
print(s)'''

"""while True:
        a = int(input())
        if 100 >= a >= 10:
            print(a)
        if a < 10:
            continue
        if a > 100:
            break"""

"""for i in range(10):
    print(i*i)"""

"""n = int(input())
for i in range(n):
    for j in range(n):
        print('*',end='  ')
    print()"""


a = int(input())
b = int(input())
c = int(input())
d = int(input())
for j in range(c, (d + 1)):
    print('\t', j, end='')
for i in range(a, (b+1)):
    print('\n', i, end='')






    """for j in range(c, (d+1)):
        print('\n', j, end='')
        #print('\t', c*d, end='')
    print('\n', a * b, end='')"""


