def to_base3(n):
    """Преобразование числа в троичную систему"""
    base3 = ''
    while n > 0:
        base3 = str(n % 3) + base3
        n //= 3
    return base3

def find_min_r():
    """Поиск минимального R > 100"""
    for n in range(11, 1000):  # Проверяем числа N > 10
        base3 = to_base3(n)  # Троичная запись числа
        even_count = base3.count('2')  # Чётные цифры (только '2')
        odd_count = base3.count('0') + base3.count('1')  # Нечётные цифры
        if even_count > odd_count:
            new_base3 = '22' + base3
        else:
            new_base3 = '11' + base3
        r = int(new_base3, 3)  # Преобразуем обратно в десятичное
        if r > 100:
            return r

# Запуск функции
result = find_min_r()
print("Минимальное значение R >", 100, ":", result)
