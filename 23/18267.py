def f(a, b):
    if a == b:
        return(1)
    elif a > b:
        return(0)
    else:
        if a!=6:
            return f(a+2, b) + f(a+5, b) + f(a*a, b)
        else:
            return f(a+2, b) + f(a+5, b) 
print(f(4, 36))