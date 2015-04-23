
class Bidding(object):

    color = [
                'SA', 
                'S', 
                'H', 
                'C', 
                'D', 
                'TA',
            ]

    def __init__(self, taker, val, col):
        assert col in self.color
        self.__val = val
        self.__col = col
        self.__coef = 1
        self.__taker = taker
        self.__is_coinched = False
        self.__is_surcoinched = False


    def __getitem__(self, idx):
        assert 0 <= idx <= 3
        if idx == 0:
            return self.__taker
        elif idx == 1:
            return self.__val
        elif idx == 2:
            return self.__col
        else:
            return self.__coef

    
    @property
    def val(self):
        return self.__val


    @property
    def col(self):
        return self.__col


    @property
    def taker(self):
        return self.__taker


    @property
    def coef(self):
        return self.__coef

    def coinche(self):
        assert not self.is_coinched() and not self.__is_surcoinched
        self.coef *= 2
        self__is_coinched = True


    def __surcoinche__(self):
        assert self.is_coinched() and not self.__is_surcoinched
        self.coef *= 2


    def is_coinched(self):
        return self.__is_coinched
