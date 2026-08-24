class array:
    def __init__(self,N:int):
        if type(N) is not int:
            raise TypeError
        if N <0:
            raise ValueError
        self.L = [0 for i in range(N)]
        self.N = N

    def __setitem__(self,index:int,rhs_object) -> None:
        if type(index) is not int:
            raise TypeError
        if index < -self.N or index >= self.N:
            raise IndexError('Index out of range')
        self.L[index] = rhs_object

    def __getitem__(self,index:int) -> int:
        if(type(index) is not int):
            raise TypeError
        if index < -self.N or index >= self.N:
            raise IndexError('Index out of range')
        return self.L[index]

    def __len__(self):
        return len(self.L)

    def __str__(self):
        return str(self.L)

a = array(8)
print("printign array 'a' immidietly after creation : ",a)
print("setting each index of array to (index + 1) * 100")

for i in range(len(a)):
    a[i] = (i + 1) * 100
print("'a'",a)


for i in range(len(a)):
    a[i] = (i + 1) * 100;


print('printing array indexwise')

for i in range(len(a)):
    n = a[i]
    print(f'a[{i}]:{n}')