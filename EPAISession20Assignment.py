class Person:
    def __init__(self, firstname, lastname, birthyear):  
        self._firstname = firstname
        self._lastname  = lastname
        self._birthyear = birthyear
        self._age = None
        self._basesalary = 50000 
        self._bonus = 10
    
    @property
    def currentyear(self):
        self._currentyear = 2024 
        return self._currentyear 
    
    @property
    def birthyear(self):
        return self._birthyear
    
    @birthyear.setter
    def birthyear(self, value):
        self._age = None
        self._birthyear = value
    
    @property
    def age(self):
        if self._age is None:
            self._age = self.currentyear - self._birthyear 
        return self._age
    
    @property
    def full_name(self):
        self._fullname = self._firstname + " " + self._lastname
        return self._fullname
    
    @full_name.setter
    def full_name(self, value):
        splitvalue = value.split()
        self._firstname = splitvalue[0]
        self._lastname = splitvalue[1]
        return (self._firstname , self._lastname)
    
    @property
    def salary(self):
        sal = (self._basesalary + (self._bonus * self._basesalary)/100)
        return sal 

class Circle:
    def __init__(self, radius):
        self._radius = radius
        self._flag = 0
    
    @property
    def area(self):
        return 3.14 * self._radius * self._radius

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        self._radius = value
        self.area
        
    @property
    def diameter(self):
        return self._radius * 2
           
