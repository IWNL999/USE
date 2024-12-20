import itertools
# Определяем алфавит и длину слова
alphabet = ['Е', 'Л', 'М', 'У', 'Р']
length = 4
# Генерируем все комбинации длиной 4
words = itertools.product(alphabet, repeat=length)
# Преобразуем комбинации в строки и находим нужное слово
for index, word in enumerate(words, start=1):
    print(index, word)
    if word[0] == 'Л':  # Проверяем, начинается ли слово с буквы 'Л'
        print(index, ''.join(word))
        break
