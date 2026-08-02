
#implement global function to validate string 

def is_date_valid(day : int,month :int,year:int):
    #todo : complete the def 
    return True;

class Date :
    def __init__(self,init_day:int,init_month:int,init_year:int):
        if type(init_day) is not int:
            raise TypeError('Bad type for day')
        if(type(init_month) is not int) :
            raise TypeError('Bad type for month')
        if(type(init_year) is not int):
            raise TypeError('bad type for year')
        if is_date_valid(init_day,init_month,init_year) is False:
            raise ValueError(f'{init_day}/{init_month}/{init_year} do no form valid date')
        self.day = init_day
        self.month = init_month
        self.year = init_year

    def get_day(self) -> int:
        return self.day;

    def get_month(self) -> int :
        return self.month

    def get_year(self) -> int:
        return self.year;

    def set_day(self,new_day:int) -> None:
        if(type(new_day) is not int):
            raise TypeError("expcted type for new_day is int")
        if is_date_valid(self.day,self.month,self.year) is False:
            raise ValueError("new date is not compatible with exstinng month and year")
        self.day = new_day

    def set_month(self,new_month:int) -> None :
        if(type(new_month) is not int):
                raise TypeError("expcted type for new_month is int")
        if is_date_valid(self.day,new_month,self.year) is False:
            raise ValueError("new month is not compatible with existing day and year");
        self.month = new_month

    def set_year(self,new_year_val:int) -> None:
        if(type(new_year_val) is not int):
            raise TypeError("expcted type of year is not int")
        self.year = new_year_val

    def show(self) -> None:
        print(f'{self.day}/{self.month}/{self.year}')

D1 = Date(1,1,1970)  # Date.__init__(D1)
print("showing date d1")
D1.show()

d1_day = D1.get_day()
d1_month = D1.get_month()
d1_year = D1.get_year()

print("testing getters :",d1_day,d1_month,d1_year)

D1.set_day(2)
D1.set_month(8)
D1.set_year(2026)

D1.show()



