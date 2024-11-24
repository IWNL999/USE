s = "1" * 101
while "1111" in s:
    if "1111" in s:
        s.replace("1111", "22", 1)
    if "222" in s:
        s.replace("222", "1", 1)
print(s)
