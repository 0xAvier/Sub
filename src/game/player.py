
from src.game.hand import Hand

class Player(object):
    
    def __init__(self, pos):
        self.pos = pos
        self.nick = ""
        self.hand = Hand()
