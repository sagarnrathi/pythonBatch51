class Array :
    def __init__(self,N:int):
        if type(N) is not int:
            raise TypeError
        if N < 0 :
            raise ValueError
        self.N = N
        self.L = [0 for x in range(N)]

    def get(self,i:int) -> int:
        if type(i) is not int :
            raise TypeError
        if i < -self.N or i>= self.N:
            raise IndexError
        return self.L[i]
    def set(self,i:int,element:int)->int:
        if type(i) is not int or type(element) is not int:
            raise TypeError
        if i < -self.N or i >= self.N:
            raise IndexError
        self.L[i] = element

    def length(self) -> int:
        return self.N

    def __str__(self) -> str:
        return str(self.L)

A = Array(8)


for i in range(8): 
    A.set(i, (i+1) * 10) # 0->10, 1->20, 2->30, 3->40, 4->50, 5->60, 6->70, 7->80

for i in range(8): 
    n = A.get(i) 
    print(f'i:{i}, n:{n}') #  # 0->10, 1->20, 2->30, 3->40, 4->50, 5->60, 6->70, 7->80

print(A) # [10, 20, 30, 40, 50, 60, 70, 80]

size = A.length() 
print(f'Length of array is:{size}')

