import numpy as np
print("№1. Создание векторов и матриц")

hours = np.arrange(0, 22, 3)
line = np.linspace(0, 1 ,5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)
print(f'hours: {hours}') 
print(f'shape: {hours.shape}', f'ndim: {hours.ndim}', f'size: {hours.size}', f'dtype: {hours.dtype}')

print("№2. Индексы и срезы в векторе")
print(f'Третий элемент: {hours[2]}')
print(f'Последний элемент: {hours[-1]}')
print(f'Элементы с индексами 2-5: {hours[2:6]}')
print(f'Каждый второй элемент: {hours[::2]}')
print(f'Массив в обратном порядке: {hours[::-1]}')

print("№3. Строки и столбцы таблицы")
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])
print(f'Форма: {temperatures.shape}')
print(f'Число измерений: {temperatures.ndim}')
print(f'Число элементов: {temperatures.size}')
print(f'Значение из второй строки и третьего столбца: {temperatures[1, 2]}')
print(f'Первая строка: {temperatures[0, :]})
print(f'Последний столбец: {temperatures[:, -1]}')
print(f'Первые две строки без первого столбца: {temperatures[:2, 1:]}')
print(f'Центральный фрагмент 2х2: {temperatures[:2, 1:3]}')


print("№4. Прямоугольные срезы")
matrix = np.arrange(1, 26).reshape(5,5)
print(f'Первые три строки: {matrix[:3]}\n{matrix[:3].shape})
print(f'Последние две строки: {matrix[-2:]}\n{matrix[-2:].shape}')
print(f'Фрагмент из строк 1-3 и столбцов 2-4: {matrix[1:4, 2:5]}\n{matrix[1:4, 2:5].shape}')
print(f'Угловой блок в правом нижнем углу: {matrix[-2:, -2:]}\n{matrix[-2:, -2:]}')


print("№5. Изменение массива с помощью срезов")
vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9

changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2] = -1

print(f'Измененный массив: {changed_hours}')
print(f'Исходный массив: {hours}')
# .copy() нужен для создания независимой копии массива. Если бы мы не использовали этот метод, то обе переменные ссылались бы на один обьект в памяти.
# также мы бы необратимо меняли исходный массив hours

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100
print(f'Итоговая матрица: {changed_matrix}')
print(f'Исходная матрица: {matrix}')


print("№6. Изменение формы")
numbers = np.arrange(12)
table = numbers.reshape(3,4)
transponsed = table.T

print(f'Форма numbers: {numbers.shape}')
print(f'Форма table: {table.shape}')
print(f'Форма transponsed: {transponsed.shape}')
# Вызов reshape(3,4) работает, потому что в массиве numbers ровно 12 элементов
# Вызов reshape(5,3) вызовет ошибку, потому что в для создания такой матрицы понадобится 15 элементов, а у нас 12

