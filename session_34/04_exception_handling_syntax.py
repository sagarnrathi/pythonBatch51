def my_sqrt(n):
    if type(n) != int and type(n) != float:
        raise TypeError(f'input must be int or float but received {type(n).__name__}')
    if(n<0):
        raise ValueError(f'expcted non negative integer or float')
    return n ** 0.5

try :
    print("start of try block")
    my_sqrt('Hello')
    print('end of try block')

except TypeError:
    print('start of execpt of block')
    print('sorry wrong argument ')
    print('end of except bloack')
print('Maze pudhil ayush')