# Ввод чисел для первого и второго списка
list1 = set(map(int, input("Введите числа первого списка через пробел: ").split()))
list2 = set(map(int, input("Введите числа второго списка через пробел: ").split()))

# Находим пересечение множеств
common_numbers = list1 & list2

# Вывод количества общих чисел
count_common = len(common_numbers)
print(count_common)
