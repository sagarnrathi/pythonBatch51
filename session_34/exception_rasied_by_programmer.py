def sqrt(n):
    if type(n) != int and type(n) != float :
        raise TypeError(f'input must be float or int but recevied {type().__name__}')
    if n <0:
        raise ValueError(f'expcted non negative integer or float')
    
    return n ** 0.5

r = sqrt(100)
print(r)
sqrt(-4)
sqrt(5.4)
sqrt(True)
sqrt('hello')