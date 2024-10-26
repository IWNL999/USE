# Функция для выполнения заданных условий
def process_number(n):
    # Разбиваем число на отдельные цифры
    a = n // 1000          # Первая цифра
    b = (n // 100) % 10    # Вторая цифра
    c = (n // 10) % 10     # Третья цифра
    d = n % 10             # Четвёртая цифра
    # Считаем суммы
    sums = [a + b, b + c, c + d]
    # Удаляем наименьшую сумму
    sums.remove(min(sums))    
    # Остальные суммы сортируем в порядке неубывания
    sums.sort()   
    # Формируем результат (объединяем две суммы)
    result = int(str(sums[0]) + str(sums[1]))    
    return result
# Перебор всех четырёхзначных чисел
for i in range(1000, 10000):
    if process_number(i) == 1315:
        print(i)  # Выводим число, которое даёт результат 1315



for i in range(9999, 1001, -1):
    s = str(i)
    k1 = int(s[0]) + int(s[1])
    k2 = int(s[1]) + int(s[2])
    k3 = int(s[2]) + int(s[3])
    first = str(k1 + k2 + k3 - max(k1, k2, k3) - min(k1, k2, k3))
    second = str(max(k1, k2, k3))
    s1 = first + second
    if s1 == '1315':
        print(i)
        break