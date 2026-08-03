class Rectangle :
    def __init__(self,height:int,width:int):
        acceptable_type =[int,float]
        if type(width) not in acceptable_type:
            raise TypeError("width must be int or float")
        if type(height) not in acceptable_type:
            raise TypeError("height must be int or float")
        if(width < 0 or height < 0):
            raise ValueError("height or width can not be negative")

        self.width = width
        self.height = height


    def get_width(self) -> float | int:
        return self.width

    def get_height(self) -> float | int :
        return self.height

    def set_width(self, new_width:float) -> None:
        acceptable_type =[int,float]
        if(type(new_width) not in acceptable_type):
            raise TypeError("new width must be int or float")
        if(new_width <=0.0):
            raise ValueError("new width can not be negative")
        self.width = new_width

    def set_height(self,new_height:float) -> None:
        acceptable_height = [int,float]
        if(type(new_height) not in acceptable_height):
            raise TypeError("new height must be int or float ")
        if(new_height <=0.0):
            raise ValueError("new height can not be negative")
        self.height = new_height

    def area(self)->int|float:
        return self.width * self.height

    def perimeter(self)->int|float:
        return 2*(self.width+self.height)


R = Rectangle(5.0, 3.5)

w = R.get_width() 
H = R.get_height() 

R.set_width(6.7)
R.set_height(2.1)

A = R.area() 
P = R.perimeter() 
