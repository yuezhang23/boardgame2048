# Board 2048 Program
This is a one-player board game with the same rules and features as shown in the 2048 board game from Apple Store. 

### How to Play

#### 1. Start a New Game
On running the program, only the menu is shown on the Turtle screen. The user can choose from menu options such as 1, 2, 3 to initialize the board.
- Press 1 to start a 4x4 size game any time.
- Press 2 to quit the game any time.
- Press 3 to challenge a bigger board.

#### 2. Game On
During the game, all menu options and arrow keys are available.
- Press 1 to start a 4x4 size game any time.
- Press 2 to quit the game any time.
- Press 3 to challenge a bigger size game any time.
- Press 'Up' for up slide.
- Press 'Down' for down slide.
- Press 'Left' for left slide.
- Press 'Right' for right slide.

#### 3. Game Over or Win
When the related message prints out, only menu options are available.

### Features
This program consists of three files.

#### Board_2048.py
This file contains the design of class `Board` that includes basic attributes and methods for running the game.

##### Constructor:
- `__init__(board, size, score)`:
  - `board`: a dictionary that will be displayed in the form of a 4x4 sized board on screen by Python Turtle.
  - `size`: edge length of the grid, namely the number of tiles on each side.
  - `score`: accumulated value of merged numbers.

##### Methods:
- `new_board(num_list)`: assigns key-value pairs to the board dictionary with a length of size*size. All values are 0 except two values randomly chosen and replaced by random numbers from `num_list` (default: `[2, 4]`).
- `challenge(bigger_size)`: asks user to input larger board size and initialize a new board game. `bigger_size` should be a number greater than 4.
- `up_down_move(option)`: moves the tiles in the given vertical direction by pressing arrow keys on the screen (`option = 0` for 'Up' arrow, `option = 1` for 'Down' arrow).
- `left_right_move(option)`: moves the tiles in the given horizontal direction by pressing arrow keys on the screen (`option = 0` for 'Left' arrow, `option = 1` for 'Right' arrow).
- `up_down_merge(dir)`: merges neighboring tiles of the same number in the given vertical direction by substituting one of the numbers with its doubled value and the other with 0 (`dir = 1` for 'Up' arrow, `dir = -1` for 'Down' arrow).
- `left_right_merge(dir)`: merges neighboring tiles of the same number in the given horizontal direction by substituting one of the numbers with its doubled value and the other with 0 (`dir = 1` for 'Left' arrow, `dir = -1` for 'Right' arrow).
- `add_number`: randomly selects a key-value pair in the board dictionary where the value is 0 and re-assigns the value 2 or 4.
- `copy_board`: returns a shadow copy of the current object.
- `shift_up`: a collective of four steps to accomplish an 'Up' shift from the user. The outcome combines move, merge, and add if all rules are met.
- `shift_down`: a collective of four steps to accomplish a 'Down' shift from the user. The outcome combines move, merge, and add if all rules are met.
- `shift_left`: a collective of four steps to accomplish a 'Left' shift from the user. The outcome combines move, merge, and add if all rules are met.
- `shift_right`: a collective of four steps to accomplish a 'Right' shift from the user. The outcome combines move, merge, and add if all rules are met.
- `__str__`: prints out the board dictionary in specific forms, namely a 4x4 array in the terminal.
- `__eq__(other)`: compares the current `Board` instance with another and returns `True` if all attributes are the same.
- `is_win`: prints out a win message if a tile numbered 2048 appears on the board.
- `is_lose`: prints out 'game over' message if the board is full, no merge could be achieved, and no 2048 appears on the board.

#### main.py
- `main`: initializes the game and interacts with the user during the game.
- `quit_game`: quits the Turtle window any time during the game.
- `draw_board_bg`: presents background settings including a menu and a tile.
- `draw_board`: updates the board on the screen after interactions with the user each time during the game.
- `draw_lose`: prints out 'game over' on the Turtle screen.
- `draw_win`: prints out a win message on the Turtle screen.

#### test_Board.py
Tests the constructor, all the methods, and error cases in `Board_2048.py`.


### Credits

- **Feature 1**: Tiles change filled color in accordance with the number on the tile.
- **Feature 2**: Users may use the challenge option on the menu to play a more difficult game.
