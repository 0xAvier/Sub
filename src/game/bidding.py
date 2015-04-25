
class Bidding(object):

    values = [
                0,
                80,
                90,
                100,
                110,
                120,
                130,
                140,
                150,
                160,
                170,
                180,
                250,
            ]

    colors = [
                'SA', 
                'S', 
                'H', 
                'C', 
                'D', 
                'TA',
                'N',
            ]

    def __init__(self, taker, val=0, col='N'):
        assert col in self.colors
        assert val in self.values
        self.__val = val
        self.__col = col
        self.__coef = 1
        self.__taker = taker
        self.__is_coinched = False
        self.__is_surcoinched = False
        self.__done = False


    def __str__(self):
        if self.is_pass():
            return "pass"
        else:
            return str(self.val) + str(self.col)
    

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


    def is_done(self, done = None):
        if done == None:
            return self.__done
        else:
            self.__done = done


    def __cmp__(self, bid):
        if self is None:
            return -1
        elif bid is None:
            return self.val
        else:
            return self.val.__cmp__(bid.val)


    def is_pass(self):
        return self.val == 0

