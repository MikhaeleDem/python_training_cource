'''Напишите функцию f(x), которая возвращает значение следующей функции, определённой на всей числовой прямой:'''

'''def f(x):

    if x <= -2:
        return 1-(x+2)**2
    if -2<x<=2:
        return -(x/2)
    if x>2:
        return ((x-2)**2)+1'''

'''Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все
нечётные значения, а чётные нацело делит на два. Функция не должна ничего возвращать, требуется
только изменение переданного списка, например:
lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]'''


'''l = [int(i) for i in input().split()]
def modify_list(l):
    l[:] = [i // 2 for i in l if i % 2 == 0]
print(modify_list(l))
print(l)'''



