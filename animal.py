class Animal():

    def __init__(self,name = None):
        self.__name = name
        self.__legs = [] 

    

    @property
    def legs(self):
        return self.__legs 

    @legs.setter
    def legs(self,legs):
        self.__legs = legs

    @property
    def name(self):
        '''
        Name Getter
        '''
        return self.__name
    
    @name.setter
    def name(self,name):
        '''
        Name setter
        '''
        self.__name = name 

    # def set_name(self, name):
    #     '''
    #        sets the name of the animal
    #     '''
    #     self.animal_name = name
    
    def show(self):
        '''
        Prints the name of the animal
        '''
        print("name")
        print(self.__name)
        if self.legs is not None:
            print("legs")
            for leg in self.legs:
                print(leg.name)

    def __secret(self):
        print("this is a secret method")


class Leg():
    def __init__(self, name=None):
        if name is None:
            self.name = "no name"
        self.__name = name 

    @property 
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name 

    