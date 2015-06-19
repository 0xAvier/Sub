# General architecture of Sub

## Main elements

* `Game Engine`: This entity is the main class of the program. It handles the game (its rules, its proceedings, etc.). 
* `Event Engine`: Gets notifications from the `Game Engine` at each event, and dispatches them to other entities.
                    *Must be only one `Event Engine` for each `Game Engine`.*
* `UI Engine` : Manage an interface of any kind (can be a graphical interface, a console interface, etc.). An interface is notified of game events
                    by the `Event Engine`. *There can be as many interfaces as wanted.*
* `Player` : Represents either a human player or an AI. Players are notified by the game for each game-related event (`card played`, `bidded`, etc.)
                and will we asked to play cards and to bid. A player can also asynchronously communicate to the `Game Engine` for events like `coinche`.
                *There may be up to four players per `Game Engine`.*


## `Game Engine` and `Event Engine`

The `Game Engine` is the first thing that must be instantiated. Then we can create an `Event Engine` and register it to the `Game Engine`:
```
game = GameEngine()
evt = EventEngine()
game.connect_event_manager(evt)
```

After that, during a game, each event will be notified to the event manager. For instance, at each card which is played, 
the event `EVT_CARD_PLAYED` will be sent with extra parameters (here the card that has just been played and the owner
of this card) to the `Event Engine`. The `Event Engine` will then dispatch the event to all `UI Engine` objects that 
are concerned.

## `Event Engine` and `UI Engine`

## `Game Engine` and `Player`

## `Player` and `UI Engine`
