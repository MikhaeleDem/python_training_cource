"""a = str(input()) # Вводим строку
g = a.upper().count('G') # Приводим регистр к заглавным, считаем символы в строке
c = a.upper().count('C')
b = len(a) # Считаем длину всей строки
s = ((g+c)/b)*100
print(s)"""

"""Кодирование осуществляется следующим образом:
s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются на этот символ и количество его повторений в этой позиции строки."""

#ggtyg
a = str(input())
i = 0
q = 1
l = len(a)
while i <= l:
    for j in a:
        if a.find(a[i+1]):
            c = a[i+1]
            if j == c:
                i += 1
                q += i
            elif j != c:
                print(j + str(q))
                q = 1
                i += 1
        else:
            c = a[-1]
            if j == c:
                i = 0
                i += 1
                q += i
            elif j != c:
                print(j + str(q))
    else:
        break

