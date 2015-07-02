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
As mentionned in the previous section, a `GameEngine` creates automatically four basic 
AI players to allow the beginning of the game. Each of these players is constructed with
the parameter `is_removable` set to `True` (see `src/game/game_engine.py:GameEngine:__init__)`:

```
from src.player.player import Player
from src.adapter.local_player_adapter import LocalPlayerAdapter

p = Player(0, is_removable=True)
padapt = LocalPlayerAdapter(p)
self.add_player(padapt)
```

The `is_removable` flag tells the `GameEngine` that a player can be evicted if another
player wants to join the game. More precisely, when a new player wants to join a game, 
it must perform the following action (from outside the `GameEngine`, e.g. in `main.my`):

```
game = GameEngine()
p = Player(pid, is_removable=False)     # Creation of a non-removable player with a pid
padapt = LocalPlayerAdapter(padapt)     # Creation of the local adapter
game.add_player(padapt)                 # Join the existing game
```

**Note.** The `pid` is the player id in the game. It must be in [0..3], and two 
players playing in the same game cannot have the same `pid`.

When the method `add_player` is called, the `GameEngine` will check if the 
player with the id `pid` is removable or not. If not, the new player will not
be able to join the game. Otherwise, the current player will be evicted and replaced
by the new player. In our example, because the new player has the flag `is_removable` 
to `False`, it will not be possible for another player to join the game with 
the same pid.


## `Deck`
The `GameEngine` handles a `Deck` object, which is composed of 32 cards. The deck is 
shuffled at its creation, but then it is managed as would be a deck in a real game.
In particular:

1. Before each deal, the deck is cut at a random point.
1. The distribution of cards is performed according to the rules. A sequence 
of distribution is randomly choosen among [2, 3, 3], [3, 2, 2] and [3, 3, 2].
Then the players are given cards according to this sequence. For instance, if
the sequence [2, 3, 3] has been choosen, each player is given 2 cards, then 3 cards
and then 3 other cards. At each point, the cards given are the one at the top of the deck. 
1. After each trick, the four cards that has been played are put on the top of the
deck of the team that won it.
1. At the end of each deal, we reconstruct the whole deck by either putting the defense
deck above of the attack deck or the opposite (this choice is random).

Note that during a game, the deck of cards is **never** shuffled.


## Communication with players

The `GameEngine` has two main ways to communicate with its players: a synchronous
way (by calling `Player` methods), and a synchronous way for the coinche.

### Synchronous communication

The `GameEngine` deals with player adapters, and not directly with players.
Each player adapter implements the interface defined by `IPlayerAdapter` 
(`src/adapter/i_player_adapter.py`). This interface defines the methods 
used by the `GameEngine` to communicate synchronously with players. 
There are two kind of methods: the ones that are needed for game
purposes, and the ones that are purely informative. 

#### Game purpose methods

This category groups the methods that are called by the `GameEngine`
when it needs to get an action from the player. For these methods, 
the `GameEngine` expects a return value that is correct relatively to 
the game context.

* `get_card(self, played, playable)`: The `GameEngine` calls this method
when it is the player turn to play a card. `played` contains the card
played so far in this trick, and `playable` is the subset of playable
cards (computed from the player's hand). The `GameEngine` expects a card 
that is in `playable`. While the return value is not valid, the `GameEngine`
will call this method.
* `get_bid(self, bidded, biddable)`: The `GameEngine` calls this method 
when it is the player turn to bid. `bidded` contains the bids (from any player)
so far, and `biddable` is the list of possible bids for the player (so the 
list of bids that are higher than the highest bid so far, with some more 
rules-relative restrictions - see [rules](coinche_rules.md) for more information).
The `GameEngine` expects a valid bid (ie a bid that is in `biddable`). While 
the return value is not valid, the `GameEngine` will call this method.

#### Informative methods

* `played(self, pid, card)`:
* `give_cards(self, cards)`:  
* `reset_hand(self)`:
* `bidded(self, bid)`

### Asynchronous communication

#### Coinche


## `Round`

### Bidding

### Deal

### Trick

## Score

