def is_date_valid(dd,mm,yy):
    return False

class Date :
    def __init__(self,init_day,init_month,init_year):
        if(type(init_day)!=int):
            raise TypeError("bad type for day value")
        if(type(init_month)!= int):
            raise TypeError("bad type for month value")
        if(type(init_year)!= int):
            raise TypeError("bad type for year value")
        self.day = init_day
        self.month = init_month
        self.year = init_year

D1 = Date(30,7,2026)
D2 = Date(30,7,1992)
D3 = Date(30,7,2000)
print('D1.__dict__',D1.__dict__)
print('D2.__dict__',D2.__dict__)
print('D3.__dict__',D3.__dict__)

class Date:
    def __init__(self,init_day,init_month,init_year):
        self.day = init_day
        self.month = init_month
        self.year = init_year
    def get_day(self):
        return self.day
    def set_day(self,new_day):
        if(type(new_day) != int):
            raise TypeError('Bad type for new day')
        self.day = new_day