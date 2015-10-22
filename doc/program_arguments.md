# -p: play
    Launch a game with 3 basic IA & 1 human gui player.

# -u | --unit-test: unit test
    Launch the unit tests.

# -f | --full-game-test: test full game
    Read one the command line the test configuration (see spec below).
    Launch a test parser + execute the test.

### Spec for full game test configuration
    4 first line: define the players (p for player, X for IA where X is the 
    id of the ia used)
    4 others the content of their hands (\#toDefine)
    #toDefine: more parameters (who's first, initial score)
    #toImplement: console_player_mind reading on stdin next play 

