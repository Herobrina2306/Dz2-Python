# 3. Задайте список из n чисел последовательности (1 + 1/n)**n и выведите на экран их сумму.
    
#     *Пример:*
    
#     - Для n=4 [2, 2.25, 2.37, 2.44]
#     Сумма 9.06

n = int(input(f'Введите число: '))
lst = []
c = 0

for i in range(n):
    b = round((1 + 1 / (i + 1)) ** (i + 1), 2)
    c = c + b
    lst.append(b)
print(lst)

print('Сумма = ', c)   