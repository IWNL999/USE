from fnmatch import fnmatch
mask = "????.*&????.*"
max_length = 0
f = open("24/24_18619.txt").readline()
f = f.replace("-", " ")
f = f.replace("*", " ")
f = f.replace("A", " ")
f = f.replace("B", " ")
f = f.replace("C", " ")
f = f.replace("D", " ")
f = f.replace("E", " ")
f = f.replace("F", " ")
max_length = 0

for start in range(len(f)):
    for end in range(start + 1, len(f) + 1):
        substring = f[start:end]
        if fnmatch(substring, mask):
            max_length = max(max_length, len(substring))

# Вывод первых 100 символов файла и максимальной длины
print(f[:100])
print("Максимальная длина последовательности:", max_length)