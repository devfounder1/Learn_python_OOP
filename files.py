import csv

with open('data2.csv', 'r', encoding= 'utf-8') as g:
    # слова как словарь
    reader2 = csv.DictReader(g)

    # Читаем данные
    for row in reader2:
        print(row['name'], row['age'])

data = [{'name':'Alex', 'age': 25, 'salary': 50000},
        {'name': 'Bob','age': 27, 'salary': 50324},
        ]

with open('otput.csv', 'w', encoding ='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames = ['name', 'age', 'salary'])
    writer.writeheader()
    writer.writerows(data)
    print(data)



# чтение 'r'
with open('data.txt', 'r', encoding='utf-8') as f:
    # Способ 1: Читать весь файл сразу
    content = f.read()
    
    # Способ 2: Читать по строкам (список)
    lines = f.readlines()
    
    # Способ 3: Читать по одной строке (итератор)
    for line in f:
        print(line.strip())  # strip() убирает \n

# запись 'w'
with open('output.txt', 'w', encoding = 'utf-8') as f:

    f.write('first line\n')
    f.write('second line\n')


# добавление 'a'
with open('output.txt', 'a', encoding='utf-8') as f:
    f.write('Третья строка\n')

