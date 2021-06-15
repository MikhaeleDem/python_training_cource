'''Напишите функцию update_dictionary(d, key, value), которая принимает на вход словарь d и два числа:
keykey и valuevalue.
Если ключ keykey есть в словаре dd, то добавьте значение valuevalue в список, который хранится по этому ключу.
Если ключа keykey нет в словаре, то нужно добавить значение в список по ключу 2 * key2∗key. Если и ключа 2 * key2∗key
нет, то нужно добавить ключ 2 * key2∗key в словарь и сопоставить ему список из переданного элемента [value][value].
Требуется реализовать только эту функцию, кода вне её не должно быть.
Функция не должна вызывать внутри себя функции input и print.'''

d = {1:1}
def update_dictionary(d, key, value):
    if key in d:
        d[key] = [value]
    else:
        if key * 2 in d:
            d[key * 2] = value
        else:
            d[key * 2].append(value)
            d[key*2] = value

#print(d)
print(update_dictionary(d, 1, -1))
