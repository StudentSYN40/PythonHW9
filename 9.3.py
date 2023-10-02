# Ввод последовательности чисел
numbers = input("Введите последовательность чисел через пробел: ").split()

# Инициализация множества для хранения встреченных чисел
seen_numbers = set()

# Перебор чисел и проверка на встреченность
for num in numbers:
    if num in seen_numbers:
        print("YES")
    else:
        print("NO")
        seen_numbers.add(num)
