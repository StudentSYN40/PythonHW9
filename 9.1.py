# Ввод числа N
n = int(input("Введите количество чисел: "))

# Ввод N чисел и создание множества
numbers = set(map(int, input(f"Введите {n} чисел через пробел: ").split()))

# Вывод количества различных чисел
unique_count = len(numbers)
print(unique_count)
