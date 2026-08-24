class array: 
    def __init__(self, N:int): 
        if type(N) is not int: 
            raise TypeError 
        if N < 0: 
            raise ValueError 
        self.L = [0 for i in range(N)]
        self.N = N 


    def __setitem__(self, index, rhs_object) -> None: 
        if type(index) is int: 
            if index < -self.N or index >= self.N: 
                raise IndexError 
            self.L[index] = rhs_object 
        elif type(index) is slice: 
            try: 
                self.L[index] = rhs_object 
            except: 
                from sys import exc_info
                exc_name, exc_data, _ = exc_info() 
                print(exc_name.__name__, exc_data)
                raise


    def __getitem__(self, index): 
        if type(index) is int: 
            # Index operator has been applied 
            if index < -self.N or index >= self.N: 
                raise IndexError 
            return self.L[index]
        elif type(index) is slice: 
            # range or slice operator has been applied 
            return self.L[index]
        else: 
            raise TypeError('bad index data within subscript operator')


    def __len__(self): 
        return len(self.L)


    def __str__(self): 
        return str(self.L)

a = array(8)
print("Printing array 'a' immediately after creation:", a)

print("Setting each index of array to (index + 1) * 100")
for i in range(len(a)): 
    a[i] = (i+1) * 100  # a.__setitem__(i, (i+1) * 100)
                        # array.__setitem__(a, i, (i+1) * 100)

print('a:', a)  

print('Printing array indexwise')
for i in range(len(a)):
    n = a[i] 
    print(f'a[{i}]:{n}')

print('a[2 : 5]:', a[2 : 5])
print('a[1 : 9 : 2]:', a[1 : 9 : 2])
print('a[::-1]:', a[::-1])

a[2 : 5] = [1000, 2000, 3000, 4000, 5000, 6000]
print('array after assigning to a[2:5]:', a)

a[2 : 8 : 2] = [-1, -2, -3]
print('array after assigning to a[2:8:2]:', a) 

a[2 : 8 : 2] = [100, 200, 300, 400, 500]