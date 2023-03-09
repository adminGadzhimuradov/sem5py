# Задача 30:  Заполните массив элементами арифметической прогрессии. Её
# первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.



# a1 = int(input())
# b = int(input())
# n = int(input())
# for i in range(n):
#    print(a1 + i * b)

   
a1, d, n = int(input()), int(input()), int(input())
progressive = [a1 + (i - 1) * d for i in range(1, n + 1)]
print(*progressive)