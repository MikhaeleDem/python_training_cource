# a, b = (int(i) for i in input().split())
# ниже ввод двух чисел через eter двумя строками. Сверху то же самое, но в одну
a = int(input())
b = int(input())

s = 0
x = 0
while a % 3 != 0:
    a += 1
for i in range(a, b+1, 3):
    s += i
    x += 1
print(s/x)