class student:

    def __init__(self,name='unknown',age=0):
        if(type(name) is not str):
            raise TypeError("name must be string object")
        if(type(age) is not int):
            raise TypeError("age must be integer")

        self.name = name
        self.age = age

    def get_name(self)->str:
        return self.name

    def get_age(self)->int:
        return self.age

    def set_name(self,new_name :str) -> None:
        if(type(new_name) is not str):
            raise TypeError("name is not type of str")
        self.name = new_name

    def set_age(self,new_age :int)->None:
        if(type(new_age) is not int):
            raise TypeError("age must be of type int")
        self.age = new_age
    def show(self) -> None:
        print(f'Name:{self.name}\n Age: {self.age}')


s = student("sagar",11)
s.show()