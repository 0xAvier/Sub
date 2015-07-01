# Architecture of the game

(Work in progress)

The `GameEngine` and its entities are the main core of the application. It is 
in charge of:

* Handling the game proceeding. This part is mainly handled by the `Round` object (see 
corresponding section).
* Notify the `EventManager` of each game-relative event (for instance `EVT_CARD_PLAYED`, 
`EVT_COINCHE`, etc.).
* Manage players, and in particular: ask them for cards and bids ; notify them of any
game-relative event.

## `GameEngine`

To create a new game, one just have to create an instance of `GameEngine`:
```
from src.game.game_engine import GameEngine
game = GameEngine()
```

### Constructor

The constructor of the `GameEngine` performs the following actions:

* Construction of a deck of cards (more about it in the corresponding section)
* Creation of four basic AI players to be able to play without any more player. Note that
each of those players is removable, it means that if another player joins the game, 
a removable player will be ejected. More about it in the next section.

### Management of (removable) players



## `Deck`
The `GameEngine` handles a `Deck` object, which is composed of 32 cards. The deck is 
shuffled at its creation, but then it is managed as would be a deck in a real game.
In particular:

1. Before each deal, the deck is cut at a random point.
1. The distribution of cards is performed according to the rules. A sequence 
of distribution is randomly choosen among [2, 3, 3], [3, 2, 2] and [3, 3, 2].
Then the players are given cards according to this sequence. For instance, if
the sequence [2, 3, 3] has been choosen, Each player is given 2 cards, then 3 cards
and then 3 other cards. At each point, the cards given are the one at the top of the deck. 
1. After each trick, the four cards that has been played are put on the top of the
deck of the team that won it.
1. At the end of each deal, we reconstruct the whole deck by either putting the defense
deck above of the attack deck or the opposite (this choice is random).

Note that during a game, the deck of cards is **never** shuffled.

## Players

## `Round`

### Bidding

### Deal

### Trick

## Score

