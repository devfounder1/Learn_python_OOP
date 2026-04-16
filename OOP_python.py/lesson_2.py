# def chetnii_chisla(arr,arr_new):
#     index = 0
#     for index in range(len(arr)):
#         if arr[index] % 2 == 0:
#            arr_new[index] = arr[index]
#         else : 
#             arr_new[index] = 0 
#     return arr_new

# arr_new = [0,0,0,0,0]
# arr = [1,2,3,4,5]

# print('старый массив:', arr)

# res = []
# res = [num for num in arr if num % 2 == 0]

# res1 = [num**2 for num in arr if num % 2 != 0]

# arr_new1 = []
# for i in range(len(arr_new)):
    
#     if arr_new[i] != 0:
#         arr_new1.append(arr_new[i])


# print('квадраты нечетных чисел:', res1)

###############################################################################################################################

def find(arr,arr_new0, arr_new1):
    arr_new0 = [num for num in arr if num % 2 == 0 ]

    arr_new1 = [num**2 for num in arr if num % 2 != 0]
    return arr_new0, arr_new1


arr = [12,3,34,65,73,23,5,76,782,3,6,43,2]

# распаковка в две переменные 
even_list, odd_squares = find(arr, [], []) 

print('Четные числа:', even_list)
print('Квадраты нечетных:', odd_squares)

# ВАРИАНТ 2: Доступ по индексу (как кортеж)
result = find(arr, [], [])
print('Четные:', result[0])
print('Нечетные квадраты:', result[1])

# ВАРИАНТ 3: Сразу в print
print('Четные:', find(arr, [], [])[0])
print('Нечетные квадраты:', find(arr, [], [])[1])



###############################################################################################################################


persons = {'name': 'Alex', 'age' : 100, 'city': 'Moscow',
           'name': 'Misha', 'age' : 23, 'city': 'SP'}


for name1, age1 in persons.items():
    print(f'{name1}: {age1}')

def get_stats(numbers):
    even = [n for n in numbers if n % 2 == 0]
    odd = [n for n in numbers if n % 2 != 0]
    return even, odd  # Возврат кортежа

evens, odds = get_stats([1, 2, 3, 4, 5])
print(evens, odds)

###############################################################################################################################


def les2 (arr):
    res = {'count': len(arr), 'sum': sum(arr), 'avg': sum(arr) / len(arr)}
    return res

arr = [11,2,3,4,5,67,7,3,42,3,5,645,23]

new = les2(arr)

# Правильный вывод:
for key, value in new.items():
    print(f'{key}: {value}')

# Или по отдельности:
print(f"Count: {new['count']}")
print(f"Sum: {new['sum']}")
print(f"Avg: {new['avg']}")
