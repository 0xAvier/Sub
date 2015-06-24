# General architecture of Sub


## Source organisation

All source code of this project can be found in `src`. This folder is organised
as follows:
* `src/adapter`: All adapters for any element of the project are implemented
here, including interfaces and concrete implementations of adapters. For
instance, `src/adapter/i_player_adapter.py` contains the interface that a player
adapter should implement, and `src/adapter/local_player_adapter.py` implements a
concrete adapter for a local player.
* `src/console`: Contains console-relative code, and in particular the
interaface that a console class must implement.
* `src/event`: Contains the code relative to the game events, and in particular
the event manager and the definition of all event codes. More information about
events [here](event.md).
* `src/game`: All the game-relative implementation is there. This is the core of
the project, as it implements the coinche game including the biddings, the
playing, the score computing, etc. More information about the game
implementation [here](game.md).
* `src/ia`: Different implementations of ia players are in this folder. *To be
clarified.*
* `src/player`: *To be clarified.* 
* `src/ui`: This folder contains all classes relative to user interface
* rendering of the game. It includes the display of the table, the menus, the
bidding interface, etc. More information about it [here](ui.md).
* `src/utils`: Several general-purpose implementations. 

## Main elements

* `GameEngine`: This entity is the main class of the program. It handles the
* game (its rules, its proceedings, etc.). Located in `src/game/game_engine.py`. 
* `EventEngine`: Gets notifications from the `GameEngine` at each event, and dispatches them to other entities.
                    *Must be only one `EventEngine` for each `GameEngine`.*
                    Located in `src/event/event_engine.py`.
* `UIEngine` : Manage an interface of any kind (can be a graphical interface, a console interface, etc.). An interface is notified of game events
                    by the `EventEngine`. *There can be as many interfaces as wanted.*
* `Player` : Represents either a human player or an AI. Players are notified by the game for each game-related event (`card played`, `bidded`, etc.)
                and will be asked to play cards and to bid. A player can also asynchronously communicate to the `GameEngine` for events like `coinche`.
                *There may be up to four players per `GameEngine`.*


## `GameEngine` and `EventEngine`

The `GameEngine` is the first thing that must be instantiated. Then we can create an `EventEngine` and register it to the `GameEngine`:
```
game = GameEngine()
evt = EventEngine()
game.connect_event_manager(evt)
```

After that, during a game, each event will be notified to the event manager. For instance, at each card which is played, 
the event `EVT_CARD_PLAYED` will be sent with extra parameters (here the card that has just been played and the owner
of this card) to the `EventEngine`. The `EventEngine` will then dispatch the event to all `UIEngine` objects that 
are concerned.

## `EventEngine` and `UIEngine`

## `GameEngine` and `Player`

Once a `GameEngine`object is created, one may want to add players to the game (note that by default, if we start a round 
with less than four players, the `GameEngine`will automatically create AI players to fill empty seats).
The `GameEngine` needs to interact (synchronously and asynchronously) with each player (to get a card for instance). 
To make this communication as generic as possible, and non-depending on the type of player (local or remote player, AI or UI player, etc.), 
there is an adapter between the `GameEngine` object and each `Player` instance. This is the point of view of the `GameEngine`:

```
[GameEngine] --> [PlayerAdapter]
```

Where a `Player Adapter` is specific to the type of the relative `Player`, but must implement `IPlayerAdapter` interface.
The gain of this layout can be seen by looking at two cases: local player and a remote player.

### Local player
In this case, the `GameEngine` and the `Player` are running in the same computer, and by the same instance of `Sub`.
The corresponding adapter is `LocalPlayerAdapter`, and the pattern is like this:

```
[GameEngine] --> [LocalPlayerAdapter] --> [Player]
```

Where `Player` can be either a `UIPlayer` or a `AIPlayer`. The code to instantiate this would be:
```
game = GameEngine()
player = AIPlayer(0) 
padapt = LocalPlayerAdapter(player) 
game.add_player(padapt)
```

### Remote player
In this case, the `GameEngine` and the `Player` are not running on the same computer, so they need to communicate through sockets.
The corresponding adapter is `RemotePlayerAdapter`, and the pattern is this one:

```
[GameEngine] --> [RemotePlayerAdapter] --> [Server] ---------> [Client] --> [Player]
```
Here again, `Player` can be an instance of `UIPlayer` or `AIPlayer`.


### In both cases ...
As `LocalPlayerAdapter` and `RemotePlayerAdapter` both implement the same interface `IPlayerAdapter`, there is no differenciation
between those two scenarii from the `GameEngine` point of view.

## `Player` and `UIEngine`
