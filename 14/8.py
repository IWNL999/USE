i = 2*729**2022 + 2*243**2024 - 2*81**2025 + 27**2020 - 2*3**2023 - 2024
c=0
while i > 0:
    if i%27>6:
        c+=1
    i//=27
print(c)