class array:
    def __init__(self,N:int):
        if type(N) is not int:
            raise TypeError
        if N < 0:
            raise ValueError
        self.L = [0 for i in range(N)]

    def __setitem__(self,index,rhs_object) -> None:
        if type(index) is int :
            if index < -len(self.L) or index >= len(self.L):
                raise IndexError
            self.L[index] = rhs_object
        elif type(index) is slice:
            try :
                self.L[index] =  rhs_object
            except :
                from sys import exc_info
                exc_name, exc_data,_= exc_info()
                print(exc_name.__name__,exc_data)
                raise 

    def __getitem__(self,index):
        if type(index) is int :
            if index < -len(self.L) or index >= len(self.L):
                raise IndexError
            return self.L[index]
        elif type(index) is slice :
            return self.L[index]
        else :
            raise TypeError('bad index data within subscript operator')

    def __len__(self):    
        return len(self.L)

    def __str__(self):
        return str(self.L)


a = array(8)
print("printing array 'a' immediately after creation : ",a)

print("setting each index of array to (index+1 )*100")

for i in range(len(a)):
    a[i] = (i + 1) * 100

print('a:',a)
print('printing array indexwise')

for i in range(len(a)):
    n = a[i]
    print(f'a[{i}]:{n}')

print('a[2:5] :',a[2:5])
print('a[1:9:2]',a[1:9:2])
print('a[::-1]',a[::-1])
a[2:8:2] = [-1,-1,-1]
print('a[2:8:2]',a)