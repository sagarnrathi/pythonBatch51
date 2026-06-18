def myfunc(s):
    if type(s) != str:
        raise TypeError(f'expcted string but received {type(s).__name__}')
    
    if len(s) != 10:
        raise ValueError(f'Length of input string must be 10,but received string of {len(s)}')
    print('logic on string of length 10')

myfunc('HelloHello')

def myFunc(s:str) -> int:
    print(s)

myFunc(100)