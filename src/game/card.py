
class Card(object):

    """
        Represent a card object, that can be seen 
        as a tuple (value, color)
        This class also implements comparison methods
        between cards (considering trump or not)

    """

    # List of possible values for a card, sorted 
    values = ['7', '8', '9', 'J', 'Q', 'K', 'T', 'A']
    # List of possible values for a card, sorted with trump ranking
    values_trump = ['7', '8', 'Q', 'K', 'T', 'A', '9', 'J']
    # Colors of cards
    colors = ['S', 'H', 'C', 'D']

    
    def __init__(self, val, col):
        """
            Creation of a new card with value val 
            and color col

        """
        self.val = val
        self.col = col


    def __getitem__(self, idx):
        """
            Cards behave like two element tuples, 
            the first item begin its value and the second
            its color

        """
        if idx == 0:
            return self.val
        elif idx == 1:
            return self.col
        else:
            raise IndexError


    def __str__(self):
        return str(self.val) + str(self.col)


    def __cmp__(self, card):
        """
            Compare two cards, no trump consideration
            Function used to sort a hand for example

        """
        if self is None:
            if card is None:
                return True
            else: 
                return False
        elif card is None:
            return False

        # If the two cards have same color
        if self[1] == card[1]:
            # We compare the values 
            return cmp(Card.values.index(self[0]), Card.values.index(card[0]))
        else:
            # Else we sort by color with a custom order
            return cmp(Card.colors.index(self[1]), Card.colors.index(card[1]))

    
    def __hash__(self):
        return str(self)


    def higher(self, card, trump = None):
        """
            Compare two cards with trump consideration
            Return true iif self is higher than card

        """
        # If no trump, or no card is trump,
        # it is a basic comparison
        if trump is None or (self[1] != trump and card[1] != trump):
            return max(self, card) == self
        else:
            # If one is trump and the other is not, the trump
            # is higher
            if self[1] == trump and card[1] != trump:
                return True
            elif self[1] != trump and card[1] == trump:
                return False
            # Else if the two cards are trumps, comparison 
            # with trump order
            else:
                if self.values_trump.index(self[0]) > self.values_trump.index(card[0]):
                    return True
                else:
                    return False


    @staticmethod
    def highest(cards, asked, trump = None):
        """
            Static method to find the highest card in a set of cards, 
            with trump consideration, given the asked color. 

        """
        # Are there trumps ?
        tr = [c for c in cards if c[1] == trump]
        # If there is no trump
        if trump == None or len(tr) == 0:
            # Return the highest card in the asked color
            return max([c for c in cards if c[1] == asked])
        # If there are trumps
        else:
            # The highest card is the highest trump
            high = tr[0]
            for c in tr:
                if self.values_trump.index(c[0]) > self.values_trump.index(high[0]):
                    high = c
            return c


