class Colour():
    def __init__(self,r=0,g=0,b=0):
        self.__red = r
        self.__green = g
        self.__blue = b

    @property
    def r(self):
        return self.__red
    
    @property
    def g(self):
        return self.__green

    @property
    def b(self):
        return self.__blue

    def __add__(self,other):
        self.__red += other.r
        self.__green += other.g
        self.__blue += other.b 
        return Colour(self.__red,self.__green, self.__blue)

    def show(self):
        print(self.__red, self.__green, self.__blue)


c1 = Colour(100,100,100)
c2 = Colour(100,100,100)
c3 = c1 + c2 

c3.show()