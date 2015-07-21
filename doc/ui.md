# Architecture of the user interface

The `UIEngine` and its entities are dedicated to display a graphical user
interface for one or more player (both IA or human). It is in charge of:

* Loading graphical resources (see image_loader) ;
* Render game and general events (such as `new message`) in a graphical way ;
* Get information from the user such as card or bidding and also messages.

## `UIEngine`

Command
multiple graphical interface

### Constructor

architecture (main, side pannel)
gestion des joueurs (cachés / pas cachés, joueur principale)
To create a new user interface

#### Game purpose methods

#### Informative methods


event possible pour lui



    utils.py

image processing
    image_loader.py     

side pannel related
    ui_side_pannel.py  

    ui_controllers.py 
    ui_console.py

table related
    ui_table.py     

    ui_bidding.py  
    ui_card.py  
    ui_hand.py  
    ui_heap.py 
    ui_scoreboard.py    

entry point
    ui_engine.py    
