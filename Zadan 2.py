#непонятно о каком массиве идёт речь, так что использую в качестве массива массив из примера в презентации: https://gbcdn.mrgcdn.ru/uploads/asset/4931164/attachment/0fab242e0454a9ae34d101d07c4615a5.pdf
#так же не ясно какие именно числа являются минимальным и максимальным, так что ввод минимума и максимума с клавиатуры

numbers_array = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
index_array = []
result_numbers = []
min_num = int(input("Введите минимальное значение: "))
max_num = int(input("Введите максимальное значение: "))

if min_num > max_num:
    print("В указанном диапазоне невозможно найти числа.")
else:
    for step in range(0, len(numbers_array)):
        if numbers_array[step] >= min_num and numbers_array[step] <= max_num:
            index_array.append(step)

    for step in range(0, len(index_array)):
        result_numbers.append(numbers_array[index_array[step]])

    print(f"Индексы: {index_array}")
    print(f"Числа: {result_numbers}")