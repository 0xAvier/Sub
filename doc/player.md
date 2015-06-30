
# Architecture of players

This document presents the management of `Player` objects, and in particular:

1. the interface between a `GameEngine` and a `Player`
1. the distinction we make between the control and the render of a player
1. how to write your own IA player.

## Interface of a `Player`

### The `PlayerAdapter`

### Synchronous interaction with `GameEngine`

### Asynchronous events


## Construction of a `Player`

A `Player` object is composed into two logical parts:

* `PlayerMind`: this part implements the behavior of a `Player` during 
a game
* `PlayerRender`: this part is in charge of displaying information about
the `Player` during the game (and in particular, its hand). 

Those two parts are described in details in the next sections.

The general architecture of a `Player` is the following: 

```
       -----> [PlayerMind]
      |
[Player] 
      |
       -----> [PlayerRender]
```

When one instanciates a `Player` object, it has by default no render and the basic IA mind (`BasicIAPlayerMind` in 
`src/player/mind/ia/`). A `Player` object has to methods to set its reder or mind:

* `Player.set_mind`: this method allows to replace the player mind by any `PlayerMind` object (must implements
the `IPlayerMind` interface). **A `Player` instance can only have one mind, so this method erases the previous
mind of the `Player`.**
* `Player.add_render`: this method allows to add a render object to the `Player`. A `Player` instance can have
as many renders as desired. More about renders in the corresponding section. 

Here is an example of how to create a `Player` for a graphical render and a IA mind: (#TODO en discuter)

```
# By default, the player is created with no render and a basic IA mind
player = Player()                           
# Create a GUI to render the player
ui = UIEngine()                             
# Create a GUI render for the player
player_render = UIPlayerRender()            
# Connect the player render to the GUI
ui.connect_player_render(player_render)     
# Register the render to the player object
player.add_render(player_render)            
# Create the IA mind
ia = GodIAPlayerMind()                      
# Replace the player mind
player.set_mind(ia)                         

```

The next sections describe in details the two components of a `Player`.


### `PlayerMind`

* The different minds implemented can be found in `src/player/mind`.

A `PlayerMind` contains all the logicl of a player. There are two main categories of `PlayerMind` implemented:

* GUI-controlled mind (`UIPlayerMind`): this mind allows one to control the player through the GUI. It allows a
real (physical) player to be part of a game.
* Artificial-Intelligence minds : these minds implement different kind of IA players that will play automatically, 
with more or less efficiency.

### `PlayerRender`

*The renders implemented can be found in `src/player/render`.*

A `PlayerRender` is in charge of handling the display of information relative to the `Player` it is attached to.

The problematic it answers is the following: only the `GameEngine` knows the hands of all players. For anti-cheating 
reasons, a `UIEngine` is not aware of the hands of all players. However, we may want to display one player's hand (for 
instance a player being controlled by the user through GUI). Since it is not the purpose of the `GameEngine` to manage
interface-relative functionnalities, another entity should notify the `UIEngine` of a player's hand. This is the role of 
the `PlayerRender`: notify the `Player` hand to some interface for display purposes. 


## Write your own IA

More about it here: (#TODO document "Getting started" to write an IA)
