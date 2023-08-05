num_a = int(input("Введите первый элемент: "))
difference = int(input("Введите разность элементов: "))
elements_count = int(input("Введите количество элементов: "))
list_result = []

for step in range(elements_count):
    current_element = num_a + step * difference
    list_result.append(current_element)

print(list_result)