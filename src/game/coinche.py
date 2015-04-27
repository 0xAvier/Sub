
COINCHE_CODE = "coinche"

class CoincheException(Exception):

    def __init__(self, bid, by):
        self.bid = bid
        self.by = by
        super(CoincheException, self).__init__()

