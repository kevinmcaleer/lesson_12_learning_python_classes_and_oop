class Diesel():
    __engine_size = 1000

    @property
    def cc(self):
        return self.__engine_size

    @cc.setter
    def cc(self,size):
        self.__engine_size = size
    
        