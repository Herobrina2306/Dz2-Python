# 5. Реализуйте алгоритм перемешивания списка.

import random

lst = [1, 2, 3, 4, 5, 6, 7, 8]

for i in range(len(lst)):
    a = random.randint(0, 7)
    b = lst[i]
    lst[i] = lst[a]
    lst[a] = b
print(lst)
