import random
import math
class Board:
    '''
    Class - Board         
    This class creates rules for a board game 2048. 
    By default, the board game is made up of 4x4 size board and begins with two randomly
    numbers( 2 or 4) on the board. The game is played by shifting all numbers in one of 
    four directions each time and merges two same numbers if they have become neighbors 
    along that direction and earns a score by the sum of merged numbers. If the board 
    is changed after each shift, a random 2 or 4 is added to the board. 
    The game is won when any number reaches 2048 on the board for the first time. 
    The game is lost when the board is filled with all numbers less than 2048 and cannot 
    shift anymore. Refer to README.TXT for more details.

    Attributes: board, size, score
    Methods: new_board, challenge, up_down_move, left_right_move, up_down_merge, left_right_merge,
            add_number, copy_board, shift_up, shift_down, shift_left, shift_right
            __str__,  __eq__, is_win, is_lose
  
    '''
    def __init__(self, board = {}, size = 4, score = 0):
        '''
        Constructor - initilaize the attributes of class Board:
            self - the current object that represents Board
            board - the initial board that is an empty dictionary
            size - the initial size of the board is set to 4x4
            score - the initial score of the game is 0
        
        Pre-conditions:

            valid values for board:

            1. an empty dictionary;

            2. a dictionary with the keys and values as non-negative integers. 
            The value of dict_keys ranges from 1 to the square of size and
            the value of dict_values is either 0 or the powers of 2;

            3. At the start of a board game, all dict_values are 0 except
                two positve values as 2, 4 or 2, 2 or 4, 4;

            4. In the middle of a board game, maximun dict_value is 2048.

            valid values for size:

            1. size is a positive integer and minimun value is 4;

            2. if user challenges for bigger board, size is at least 5.

            valid values for score:

            1. score is non-negative and a multiple of 4.

            2. if board is empty, score should be 0.

            If input parameters do not match pre-conditions, the 
            program will abort by raising a valuerror in each
            case.
        
        '''

        if not isinstance(board, dict) or not isinstance(size, int) or\
            not isinstance(score, int):
            raise ValueError('attribute of wrong type')
        
        if size < 4:
            raise ValueError('the minimum board size is 4')
        
        if score < 0 or (board == {} and score > 0):
            raise ValueError('score is non-negative and is 0 only if the board is empty')
             
        if board != {}:
            if score % 4 != 0: 
                raise ValueError('score must be a non-negative multiple of 4')
            
            if len(board) != size ** 2:
                raise ValueError('the number of dictionary items should be the square of the board size')
                     
            for key, value in list(board.items()): 
                if not isinstance(key, int) or key not in range(1, size ** 2 + 1):
                    raise ValueError('invalid board key')

                if not isinstance(value, int) or value < 0:
                    raise ValueError('invalid board number')
                
                if value != 0 and int(math.log2(value)) != math.log2(value):
                    raise ValueError('invalid board number: not a power of 2')
                
                if value !=0 and int(math.log2(value)) not in range(1, 12):  
                    raise ValueError('invalid board number: not between 2 and 2048')               

        self.score = score
        self.size = size   
        self.board = board

    def new_board(self, num_list = [2, 4]):
        '''
        Method - new_board
            this method assigns new key-value paires to the board dictionary
            or over-write the given length dictionary. 
            Dictionary length is the square of the board size
            Keys are consecutive integers from 1 to square of the board size, 
            Two values chosen randomly from [2, 4] and other values are all 0.
            Score is reset to 0.

        Parameters: num_list: list
            this num_list provide value options. 
            default setting for the game is [2,4].
        
        Pre-conditons:
            before calling the method, the given size of an object instance 
            should be no smaller than 4.

            If not, the program will abort by raising a valuerror.

        '''
        if not isinstance(self.size, int) or self.size < 4:
            raise ValueError('invalid board size')
        
        # create the new board by assigning key-value pairs to the dictionary
        for i in range(1, (self.size ** 2 + 1)):
            self.board[i] = 0  

        # two keys randomly chosen from the board and values randomly mapped to 2 or 4.   
        index_start = random.sample(range(1, self.size ** 2 + 1), k = 2)
        self.board[index_start[0]] = random.choice(num_list)
        self.board[index_start[1]] = random.choice(num_list)
        self.score = 0
    
    def challenge(self, bigger_size):
        '''
        Method - challenge
            this method assigns new board size to the object instance.
            by definition of challenge, input size should be bigger than 4.

        Parameters: bigger_size: integer
            bigger_size is the user-input size number to challenge
        
        Pre-conditons:
            bigger_size should be bigger than 4.   
            If not, the program will abort by raising a valuerror.

        '''
        if not isinstance(bigger_size, int):
            raise ValueError('board size should be a number')
               
        if bigger_size <= 4:
            raise ValueError('a challenge number should be bigger than 4')
        
        # change the board size and reset the board to empty dictionary
        self.size = bigger_size
        self.board = {}
        self.score = 0

    def up_down_move(self, option):
        '''
        Method - up_down_move
            this method moves every positive values vertically, in each column of the board.
        
        Parameters: option : int
            option is an integer input from user, either 0 or 1.

            if option = 0, board is updated after the positive numbers are moved toward 
            its top board edge in prior order, only jumping over 0s.
            
            if option = 1, board is updated after the positive numbers are moved toward 
            its down board edge in prior order, only jumping over 0s.

        Pre-conditons:
            the board calling this method should not be empty.
            If not, the program will abort by raising a valuerror.

        '''
        if self.board == {}:
            raise ValueError('no board to move')

        # from helper function board_list_key()
        # two nested lists of keys by column, one mapped positive numbers and the other mapped to to 0s 
        col_of_no_zero = self.board_list_key()[0]
        col_of_zero = self.board_list_key()[1]     
        
        new_dict = {}
        for i in range(self.size):
            for key in col_of_no_zero[i]:
                
                # keys mapped to positive values are added to new_dict as key-value pairs
                new_dict[i + 1 + self.size * (col_of_no_zero[i].index(key) + option * len(col_of_zero[i]))] = self.board[key]  

            for k in range(len(col_of_zero[i])):  

                # keys mapped to 0s are added to new_dict as key-value pairs, following the positive numbers in given column
                new_dict[i + 1 + self.size * (k + (1 - option) * len(col_of_no_zero[i]))] = 0      
        self.board = new_dict

    def left_right_move(self, option):
        '''
        Method - left_right_move
            this method moves every positive values horizontally, in each row of the board.

        Parameters: option : int
            option is an integer input from user, either 0 or 1.

            if option = 0, board is updated after the positive numbers are moved toward 
            its left board edge in prior order, only jumping over 0s.
            
            if option = 1, board is updated after the positive numbers are moved toward 
            its right board edge in prior order, only jumping over 0s.

        Pre-conditons:
            the board calling this method should not be empty.
            If not, the program will abort by raising a valuerror.

        '''
        if self.board == {}:
            raise ValueError('no board to move')
        
        # from helper function board_list_key()
        # two nested lists of keys by row, one mapped positive numbers and the other mapped to to 0s 
        row_of_no_zero = self.board_list_key()[2]    
        row_of_zero = self.board_list_key()[3] 
        
        new_dict = {}
        for i in range(self.size): 
            for key in row_of_no_zero[i]: 

                # keys mapped to positive values are added to new_dict as key-value pairs
                new_dict[1 + i * self.size + row_of_no_zero[i].index(key) + option * len(row_of_zero[i])] = self.board[key]
            
            for j in range(len(row_of_zero[i])): 

                # keys mapped to 0s are added to new_dict as key-value pairs, following the positive numbers in given row
                new_dict[1 + self.size * i + j + (1 - option) * len(row_of_no_zero[i])] = 0   
        self.board = new_dict

    def up_down_merge(self, dir):
        '''
        Method - up_down_merge
            this method looks for same neighbour numbers in each column of the board. 

        Parameters: dir : int
            dir is an integer input from user, either 1 or -1.

            If dir = 1, merge in the up direction. If the same number is found under the row, 
            the upper number will be doubled and the lower number will be set to 0;

            If dir = -1, merge in the down direction. If the same number is found above the row, 
            the lower number will be doubled and the upper number will be set to 0.
        
        Pre-conditons:
            the board calling this method should not be empty.
            If not, the program will abort by raising a valuerror.

        '''
        if self.board == {}:
            raise ValueError('no board to merge')

        for i in range(1, self.size + 1):

            # if dir == 1, keys are chosen from upper 3 numbers in size-4 column.
            # if dir == -1, keys are chosen from lower 3 numbers in size-4 column 
            for key in list(range(i, i + self.size * (self.size - 1) + 1, self.size))[::dir][:(self.size - 1)]:
                if self.board[key] == self.board[key + dir * self.size]:
                    self.board[key] = self.board[key] * 2
                    self.board[key + dir * self.size] = 0
    
                    # score is updated
                    self.score = self.score + self.board[key]
        
    def left_right_merge(self, dir):
        '''
        Method - left_right_merge
            this method looks for same neighbour numbers in each row of the board. 

        Parameters: dir : int
            dir is an integer input from user, either 1 or -1.

            dir = 1, merge in the left direction. If the same number is found at right of the column,
            the left number will be doubled and the right number will be set to 0.

            dir = -1, merge in the right direction. If the same number is found at left of the column,
            the right number will be doubled and the left number will be set to 0.
        
        Pre-conditons:
            the board calling this method should not be empty.
            If not, the program will abort by raising a valuerror.

        '''
        if self.board == {}:
            raise ValueError('no board to merge')
        
        for i in range(1, self.size * (self.size - 1) + 2, self.size):

            # if dir == 1, keys are chosen from leftside 3 numbers in size-4 row.
            # if dir == -1, keys are chosen from rightside 3 numbers in size-4 row. 
            for key in range(i, i + self.size)[::dir][:(self.size - 1)]:
                if self.board[key] == self.board[key + dir]:
                    self.board[key] = self.board[key] * 2
                    self.board[key + dir] = 0

                    # score is updated
                    self.score = self.score + self.board[key]
      
    def add_number(self):
        '''
        Method - add_number
            this method randomly add 2 or 4 to the existing board, which 
            means a value in the board dictionary is re-assigned to 2 or 4.
        
        Pre-conditons:
            the board calling this method should not be empty or full,
            which means the board can't be an empty dictionary nor a dictionary
            with all positive values.

            If not, the program will abort by raising a valuerror.

        '''
        if self.board == {}:
            raise ValueError('no board to add')
        
        if min(list(self.board.values())) != 0:
            raise ValueError('the board is full, no place to add')
        
        # creates a list of keys that are mapped to values of 0.
        # randomly add a value of 2 or 4 to one of the keys from the list
        key_list_of_zero = []
        for key, value in self.board.items():
            if value == 0:
                key_list_of_zero.append(key)
        self.board[random.choice(key_list_of_zero)] = random.choice([2, 4])
    
    def copy_board(self):
        '''
        Method - copy_board
            this method returns a shallow-copy of the prior object with 
            the attributes being the same.
        
        Return: copy_board : Board
        '''
        copy_board = Board()
        copy_board.board = self.board.copy()
        copy_board.size = self.size
        copy_board.score = self.score
        return copy_board
    
    def shift_up(self):
        '''
        Method - shift_up
            this method is a combine of methods to accomplish the change in the board dictionary 
            after shifting up in real game. 
            If the board is changed after up_move or up_merge, a 2 or 4 will be randomly added to the board.
   
        Pre-conditons:
            the board calling this method should not be empty.
            If not, the program will abort by raising a valuerror.
        '''
        if self.board == {}:
            raise ValueError('no board to shift')
        
        temp = self.copy_board()
        self.up_down_move(0)
        self.up_down_merge(1)
        self.up_down_move(0)
        if not self.__eq__(temp):
            self.add_number()
    
    def shift_down(self):
        '''
        Method - shift_down
            this method is a combine of methods to accomplish the change in the board dictionary 
            after shifting down in real game. 
            If the board is changed after down_move or down_merge, a 2 or 4 will be randomly added to the board.
   
        Pre-conditons:
            the board calling this method should not be empty.
            If not, the program will abort by raising a valuerror.
        '''
        if self.board == {}:
            raise ValueError('no board to shift')
        
        temp = self.copy_board()
        self.up_down_move(1)
        self.up_down_merge(-1)
        self.up_down_move(1)
        if not self.__eq__(temp):
            self.add_number()

    def shift_left(self):
        '''
        Method - shift_left
            this method is a combine of methods to accomplish the change in the board dictionary 
            after shifting left in real game. 
            If the board is changed after left_move or left_merge, a 2 or 4 will be randomly added to the board.
   
        Pre-conditons:
            the board calling this method should not be empty.
            If not, the program will abort by raising a valuerror.
        '''
        if self.board == {}:
            raise ValueError('no board to shift')
        
        temp = self.copy_board()
        self.left_right_move(0)
        self.left_right_merge(1)
        self.left_right_move(0)
        if not self.__eq__(temp):
            self.add_number()
    
    def shift_right(self):
        '''
        Method - shift_right
            this method is a combine of methods to accomplish the change in the board dictionary 
            after shifting right in real game. 
            If the board is changed after right_move or right_merge, 
            a 2 or 4 will be randomly added to the board.
   
        Pre-conditons:
            the board calling this method should not be empty.
            If not, the program will abort by raising a valuerror.
        '''
        if self.board == {}:
            raise ValueError('no board to shift')
        
        temp = self.copy_board()
        self.left_right_move(1)
        self.left_right_merge(-1)
        self.left_right_move(1)
        if not self.__eq__(temp):
            self.add_number()

    def __str__(self):
        '''
        Method - __str__
            this method prints out the board dictionary in specific forms.
        '''
        output = ''
        for key in range(1, self.size ** 2 + 1):
            if self.board == {}:
                output += ''
            elif key % self.size == 0 and key // self.size != 0:
                output += f"{self.board[key]}\n\n"
            else:
                output += f"{self.board[key]}  "
        return output 
      
    def __eq__(self, other):
        '''
        Method - __eq__
            this method compares two objects of the same class by their
            attributes and returns True if attributes are all the same.
        
        Pre-conditions:
            the user input object should be an instance of Board
            If not, the program will abort by raising a valuerror.

        Parameters: other: Board
            input class instance from the user.
        
        Return: Boolean values
        '''

        if not isinstance(other, Board):
            raise ValueError('input is not an instance of Board')
        
        # when all attributes are the same between two instances of the same class
        return self.board == other.board and self.size == other.size and self.score == other.score
    
    def is_win(self):
        '''
        Method - is_win
            this method checks if any value in the board dictionary had reached 2048.
            If so, it prints out a win message and return True, otherwise returns False.
        
        Return: Boolean values
        '''
        # when biggest number in the board reaches 2048, it wins
        if self.board != {} and max(list(self.board.values())) == 2048:
            print('you win!')
            return True
        return False
    
    def is_lose(self):
        '''
        Method - is_lose
            this method checks if the board is full and can't merge values. If, by then, no value has reached 
            2048, it prints out a game-over message and return True, otherwise returns False.
        
        Return: Boolean values
        '''
        if self.board != {} and min(list(self.board.values())) != 0 and max(list(self.board.values())) != 2048:

            # create a shallow copy to store changes after merging vertically and horizontally
            check_board = self.copy_board()
            check_board.up_down_merge(1)
            check_board.left_right_merge(1)

            # if no change happens by comparing current board and prior shallow copy, game over
            if self.__eq__(check_board):
                print('Game over')
                return True
        return False

    # helper method: sorts board keys and creates four nested lists of keys: 
    # two nested lists of keys by column, one mapped to positive values and the other mapped to 0s
    # two nested lists of keys by row, one mapped to positive values and the other mapped to 0s
    def board_list_key(self):  
        col_of_no_zero = []            
        col_of_zero = []            
        
        for i in range(1, self.size + 1):  
            list_of_no_zero = []            
            list_of_zero = []            
            for key in range(i, self.size ** 2 + 1, self.size):
                if self.board[key] != 0: 
                    list_of_no_zero.append(key)
                else: 
                    list_of_zero.append(key)
            col_of_no_zero.append(list_of_no_zero)
            col_of_zero.append(list_of_zero)

        row_of_no_zero = []            
        row_of_zero = []            
        
        for i in range(1, self.size * (self.size - 1) + 2, self.size):
            list_of_no_zero = []            
            list_of_zero = []   
            for key in range(i, i + self.size): 
                if self.board[key] != 0: 
                    list_of_no_zero.append(key)
                else: 
                    list_of_zero.append(key)
            row_of_no_zero.append(list_of_no_zero)
            row_of_zero.append(list_of_zero)

        return col_of_no_zero, col_of_zero, row_of_no_zero, row_of_zero