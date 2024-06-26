from Board_2048 import Board
import unittest
class Board_test(unittest.TestCase):
    def test_init(self):
        '''
        test the constructor __init__
        '''
        board0 = Board({}, 4, 0)

        # test board by definition
        self.assertEqual(board0.board, {})

        # test size by definition
        self.assertEqual(board0.size, 4)

        # test score by definition
        self.assertEqual(board0.score, 0)

    def test_new_board(self):
        '''
        test the method new_board()
        '''
        # case 1
        # when the size 4x4 board is over-written and a new board is created.
        dict0 = {1: 2, 2: 0, 3: 4, 4: 0, 5: 0, 6: 8, 7: 0, 8: 0, 9: 2, 10: 0, 11: 0, 12: 4, 13: 0, 14: 8, 15: 0, 16: 0}
        board1 = Board(dict0, 4, 32)
        board1.new_board()
        
        list_of_values = list(board1.board.values())
        zero_count = list_of_values.count(0)
        number_count = list_of_values.count(2) + list_of_values.count(4)
        sum_number = list_of_values.count(2) * 2 + list_of_values.count(4) * 4

        # test the new game has two values as 2 or 4, all 14 values as 0.
        self.assertEqual(zero_count, 14)
        self.assertEqual(number_count, 2)
        self.assertEqual(board1.size, 4)
        self.assertEqual(board1.score, 0)

        # test when randomly added numbers are two 4s.
        if sum_number == 8:
            self.assertEqual(list_of_values.count(2), 0)
            self.assertEqual(list_of_values.count(4), 2)

        # test when randomly added numbers are two 2s.
        if sum_number == 4:
            self.assertEqual(list_of_values.count(2), 2)
            self.assertEqual(list_of_values.count(4), 0)

        # test when randomly added numbers are one 2 and one 4.
        if sum_number == 6:
            self.assertEqual(list_of_values.count(2), 1)
            self.assertEqual(list_of_values.count(4), 1)

        # case 2
        # when the size 5x5 board is created and random numbers are set to 4 or 8.
        board11 = Board({}, 5, 0)
        board11.new_board([4, 8])

        list_of_values = list(board11.board.values())
        zero_count = list_of_values.count(0)
        number_count = list_of_values.count(4) + list_of_values.count(8)
        sum_number = list_of_values.count(4) * 4 + list_of_values.count(8) * 8

        # test the new game has two values as 4 or 8, all other 23 values as 0.
        self.assertEqual(zero_count, 23)
        self.assertEqual(number_count, 2)
        self.assertEqual(board11.size, 5)
        self.assertEqual(board11.score, 0)

        # test when randomly added numbers are two 8s.
        if sum_number == 16:
            self.assertEqual(list_of_values.count(4), 0)
            self.assertEqual(list_of_values.count(8), 2)

        # test when randomly added numbers are two 4s.
        if sum_number == 8:
            self.assertEqual(list_of_values.count(4), 2)
            self.assertEqual(list_of_values.count(8), 0)

        # test when randomly added numbers are one 4 and one 8.
        if sum_number == 12:
            self.assertEqual(list_of_values.count(4), 1)
            self.assertEqual(list_of_values.count(8), 1)

    def test_challenge(self):
        '''
        test the method challenge()
        '''
        dict0 = {1: 2, 2: 0, 3: 4, 4: 0, 5: 0, 6: 8, 7: 0, 8: 0, 9: 2, 10: 0, 11: 0, 12: 4, 13: 0, 14: 8, 15: 0, 16: 0}
        board2 = Board(dict0, 4, 16)
        board2.challenge(6)

        # case 1
        # test when a size 6x6 is created, the board is set to empty and score set to 0
        self.assertEqual(board2.board, {})
        self.assertEqual(board2.size, 6)
        self.assertEqual(board2.score, 0)

    def test_up_move(self):
        '''
        test method up_down_move(0) in the up direction 
        '''
        # case 1
        # when numbers are in the middle, up_move changes the board
        dict0 = {1: 2, 2: 0, 3: 4, 4: 0, 5: 0, 6: 8, 7: 0, 8: 0, 9: 2, 10: 0, 11: 0, 12: 4, 13: 0, 14: 8, 15: 0, 16: 0}
        board3 = Board(dict0, 4, 0)
        board3.up_down_move(0)

        # test actual board dict vs expected board dict after up move
        dict1 = {1: 2, 2: 8, 3: 4, 4: 4, 5: 2, 6: 8, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0}
        self.assertDictEqual(board3.board, dict1)

        # case 2
        # test when move does not happen
        board3.up_down_move(0)
        self.assertDictEqual(board3.board, dict1)
    
    def test_down_move(self):
        '''
        test method up_down_move(1) in the down direction 
        '''
        # case 1
        # when numbers are in the middle, down_move changes the board
        dict0 = {1: 0, 2: 0, 3: 2, 4: 0, 5: 4, 6: 0, 7: 4, 8: 4, 9: 0, 10: 2, 11: 0, 12: 4, 13: 0, 14: 0, 15: 0, 16: 0}
        board3 = Board(dict0, 4, 0)
        board3.up_down_move(1)

        # test actual board dict vs expected board dict after down move
        dict1 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 2, 12: 4, 13: 4, 14: 2, 15: 4, 16: 4}
        self.assertDictEqual(board3.board, dict1)

        # case 2
        # test when move does not happen
        board3.up_down_move(1)
        self.assertDictEqual(board3.board, dict1)

    def test_left_move(self):
        '''
        test method left_right_move(0) in the left direction 
        '''
        # case 1
        # when numbers are in the middle, left_move changes the board
        dict0 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 2, 8: 0, 9: 2, 10: 0, 11: 2, 12: 4, 13: 0, 14: 4, 15: 2, 16: 0}
        board3 = Board(dict0, 4, 0)
        board3.left_right_move(0)

        # test actual board dict vs expected board dict after left move
        dict1 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 2, 6: 0, 7: 0, 8: 0, 9: 2, 10: 2, 11: 4, 12: 0, 13: 4, 14: 2, 15: 0, 16: 0}
        self.assertDictEqual(board3.board, dict1)

        # case 2
        # test when move does not happen 
        board3.left_right_move(0)
        self.assertDictEqual(board3.board, dict1)
    
    def test_right_move(self):
        '''
        test method left_right_move(1) in the right direction 
        '''
        # case 1
        # when numbers are in the middle, right_move changes the board
        dict0 = {1: 0, 2: 2, 3: 0, 4: 4, 5: 0, 6: 0, 7: 2, 8: 0, 9: 0, 10: 4, 11: 4, 12: 0, 13: 4, 14: 0, 15: 0, 16: 0}
        board3 = Board(dict0, 4, 0)
        board3.left_right_move(1)

        # test actual board dict vs expected board dict after right move
        dict1 = {1: 0, 2: 0, 3: 2, 4: 4, 5: 0, 6: 0, 7: 0, 8: 2, 9: 0, 10: 0, 11: 4, 12: 4, 13: 0, 14: 0, 15: 0, 16: 4}
        self.assertDictEqual(board3.board, dict1)

        # case 2
        # test when move does not happen 
        board3.left_right_move(1)
        self.assertDictEqual(board3.board, dict1)
    
    def test_up_merge(self):
        '''
        test method up_down_merge(1) in the up direction 
        '''
        # case 1
        # one merge with only two same number in the column
        dict3 = {1: 2, 2: 0, 3: 2, 4: 0, 5: 4, 6: 0, 7: 2, 8: 0, 9: 0, 10: 0, 11: 4, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0}
        board4 = Board(dict3, 4, 0)
        board4.up_down_merge(1)

        # test expected board dict after up merge
        dict4 = {1: 2, 2: 0, 3: 4, 4: 0, 5: 4, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 4, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0}  
        self.assertDictEqual(board4.board, dict4)

        # test expected update in score
        self.assertEqual(board4.score, 4)

        # case 2
        # two merges in same column
        dict5 = {1: 2, 2: 2, 3: 4, 4: 0, 5: 4, 6: 4, 7: 4, 8: 0, 9: 0, 10: 0, 11: 4, 12: 0, 13: 0, 14: 0, 15: 4, 16: 0}
        board5 = Board(dict5, 4, 0)
        board5.up_down_merge(1)

        # test expected board dict after up merge
        dict6 = {1: 2, 2: 2, 3: 8, 4: 0, 5: 4, 6: 4, 7: 0, 8: 0, 9: 0, 10: 0, 11: 8, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0}
        self.assertDictEqual(board5.board, dict6)
        
        # test expected update in score
        self.assertEqual(board5.score, 16)

        # case 3
        # two merges in different columns
        dict7 = {1: 2, 2: 2, 3: 4, 4: 2, 5: 4, 6: 4, 7: 4, 8: 2, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0}
        board6 = Board(dict7, 4, 0)
        board6.up_down_merge(1)
        
        # test expected board dict after up merge
        dict8 = {1: 2, 2: 2, 3: 8, 4: 4, 5: 4, 6: 4, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0}
        self.assertDictEqual(board6.board, dict8)
        
        # test expected update in score
        self.assertEqual(board6.score, 12)

        # case 4
        # one merge with three same numbers in the column, where only two of them closest to the upper edge merge
        dict9 = {1: 2, 2: 0, 3: 2, 4: 0, 5: 4, 6: 0, 7: 2, 8: 0, 9: 0, 10: 0, 11: 2, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0}
        board7 = Board(dict9, 4, 0)
        board7.up_down_merge(1)
        
        # test expected board dict after up merge
        dict10 = {1: 2, 2: 0, 3: 4, 4: 0, 5: 4, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 2, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0}
        self.assertDictEqual(board7.board, dict10)
        
        # test expected update in score
        self.assertEqual(board7.score, 4)

        # case 5
        # when merge does not happen again after prior merge
        board7.up_down_merge(1)
        self.assertDictEqual(board7.board, dict10)
    
    def test_down_merge(self):
        '''
        test method up_down_merge(-1) in the down direction 
        '''
        # case 1
        # one merge with only two same number in the column
        dict3 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 2, 12: 4, 13: 4, 14: 2, 15: 4, 16: 4}
        board4 = Board(dict3, 4, 0)
        board4.up_down_merge(-1)
        
        # test expected board dict after down merge
        dict4 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 2, 12: 0, 13: 4, 14: 2, 15: 4, 16: 8}
        self.assertDictEqual(board4.board, dict4)
        
        # test expected update in score
        self.assertEqual(board4.score, 8)

        # case 2
        # two merges in same column
        dict5 = {1: 0, 2: 4, 3: 0, 4: 0, 5: 0, 6: 4, 7: 2, 8: 2, 9: 0, 10: 4, 11: 4, 12: 0, 13: 0, 14: 4, 15: 0, 16: 0}
        board5 = Board(dict5, 4, 0)
        board5.up_down_merge(-1)
        
        # test expected board dict after down merge
        dict6 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 8, 7: 2, 8: 2, 9: 0, 10: 0, 11: 4, 12: 0, 13: 0, 14: 8, 15: 0, 16: 0}
        self.assertDictEqual(board5.board, dict6)
        
        # test expected update in score
        self.assertEqual(board5.score, 16)

        # case 3
        # two merges in different columns
        dict7 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 4, 7: 0, 8: 0, 9: 0, 10: 4, 11: 2, 12: 4, 13: 4, 14: 2, 15: 4, 16: 4}
        board6 = Board(dict7, 4, 0)
        board6.up_down_merge(-1)
        
        # test expected board dict after down merge
        dict8 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 8, 11: 2, 12: 0, 13: 4, 14: 2, 15: 4, 16: 8}
        self.assertDictEqual(board6.board, dict8)
        
        # test expected update in score
        self.assertEqual(board6.score, 16)

        # case 4
        # one merge with three same numbers in the column, where only two of them closest to the down edge merge
        dict9 = {1: 0, 2: 2, 3: 0, 4: 0, 5: 4, 6: 0, 7: 0, 8: 2, 9: 0, 10: 2, 11: 0, 12: 2, 13: 0, 14: 4, 15: 0, 16: 2}
        board7 = Board(dict9, 4, 0)
        board7.up_down_merge(-1)
        
        # test expected board dict after down merge
        dict10 = {1: 0, 2: 2, 3: 0, 4: 0, 5: 4, 6: 0, 7: 0, 8: 2, 9: 0, 10: 2, 11: 0, 12: 0, 13: 0, 14: 4, 15: 0, 16: 4}
        self.assertDictEqual(board7.board, dict10)
        
        # test expected update in score
        self.assertEqual(board7.score, 4)

        # case 5
        # when merge does not happen again after prior merge
        board7.up_down_merge(-1)
        self.assertDictEqual(board7.board, dict10)

    def test_left_merge(self):
        '''
        test method left_right_merge(1) in the left direction 
        ''' 
        # case 1 
        # one merge with only two same number in the row
        dict3 = {1: 2, 2: 4, 3: 0, 4: 0, 5: 2, 6: 2, 7: 0, 8: 0, 9: 4, 10: 0, 11: 0, 12: 0, 13: 2, 14: 4, 15: 0, 16: 0}
        board4 = Board(dict3, 4, 0)
        board4.left_right_merge(1)
       
        # test expected board dict after left merge
        dict4 = {1: 2, 2: 4, 3: 0, 4: 0, 5: 4, 6: 0, 7: 0, 8: 0, 9: 4, 10: 0, 11: 0, 12: 0, 13: 2, 14: 4, 15: 0, 16: 0}
        self.assertDictEqual(board4.board, dict4)
       
        # test expected update in score
        self.assertEqual(board4.score, 4)

        # case 2 
        # two merges in same row
        dict5 = {1: 4, 2: 2, 3: 0, 4: 0, 5: 2, 6: 4, 7: 2, 8: 0, 9: 4, 10: 4, 11: 2, 12: 2, 13: 4, 14: 0, 15: 0, 16: 0}
        board5 = Board(dict5, 4, 0)
        board5.left_right_merge(1)
        
        # test expected board dict after left merge
        dict6 = {1: 4, 2: 2, 3: 0, 4: 0, 5: 2, 6: 4, 7: 2, 8: 0, 9: 8, 10: 0, 11: 4, 12: 0, 13: 4, 14: 0, 15: 0, 16: 0}
        self.assertDictEqual(board5.board, dict6)
        
        # test expected update in score
        self.assertEqual(board5.score, 12)

        # case 3 
        # two merges in different rows
        dict7 = {1: 4, 2: 4, 3: 0, 4: 0, 5: 2, 6: 2, 7: 0, 8: 0, 9: 4, 10: 2, 11: 0, 12: 0, 13: 2, 14: 0, 15: 0, 16: 0}
        board6 = Board(dict7, 4, 0)
        board6.left_right_merge(1)
        
        # test expected board dict after left merge
        dict8 = {1: 8, 2: 0, 3: 0, 4: 0, 5: 4, 6: 0, 7: 0, 8: 0, 9: 4, 10: 2, 11: 0, 12: 0, 13: 2, 14: 0, 15: 0, 16: 0}
        self.assertDictEqual(board6.board, dict8)
        
        # test expected update in score
        self.assertEqual(board6.score, 12)

        # case 4 
        # one merge with three same numbers in the row, where only two of them closest to the left edge merge
        dict9 = {1: 4, 2: 8, 3: 0, 4: 0, 5: 2, 6: 2, 7: 2, 8: 0, 9: 2, 10: 0, 11: 0, 12: 0, 13: 4, 14: 0, 15: 0, 16: 0}
        board7 = Board(dict9, 4, 0)
        board7.left_right_merge(1)
        
        # test expected board dict after left merge
        dict10 = {1: 4, 2: 8, 3: 0, 4: 0, 5: 4, 6: 0, 7: 2, 8: 0, 9: 2, 10: 0, 11: 0, 12: 0, 13: 4, 14: 0, 15: 0, 16: 0}
        self.assertDictEqual(board7.board, dict10)
       
        # test expected update in score
        self.assertEqual(board7.score, 4)

        # case 5 
        # case when merge does not happen again after prior merge
        board7.left_right_merge(1)
        self.assertDictEqual(board7.board, dict10)

    def test_right_merge(self):  
        '''
        test method left_right_merge(-1) in the right direction 
        ''' 
        # case 1 
        # one merge with only two same number in the row
        dict3 = {1: 0, 2: 0, 3: 0, 4: 4, 5: 0, 6: 0, 7: 2, 8: 4, 9: 0, 10: 0, 11: 4, 12: 2, 13: 0, 14: 0, 15: 2, 16: 2}
        board4 = Board(dict3, 4, 0)
        board4.left_right_merge(-1)
        
        # test expected board dict after right merge
        dict4 = {1: 0, 2: 0, 3: 0, 4: 4, 5: 0, 6: 0, 7: 2, 8: 4, 9: 0, 10: 0, 11: 4, 12: 2, 13: 0, 14: 0, 15: 0, 16: 4}
        self.assertDictEqual(board4.board, dict4)
        
        # test expected update in score
        self.assertEqual(board4.score, 4)

        # case 2 
        # two merges in same row
        dict5 = {1: 0, 2: 0, 3: 0, 4: 2, 5: 8, 6: 8, 7: 4, 8: 4, 9: 0, 10: 0, 11: 0, 12: 2, 13: 0, 14: 0, 15: 0, 16: 2}
        board5 = Board(dict5, 4, 0)
        board5.left_right_merge(-1)
        
        # test expected board dict after right merge
        dict6 = {1: 0, 2: 0, 3: 0, 4: 2, 5: 0, 6: 16, 7: 0, 8: 8, 9: 0, 10: 0, 11: 0, 12: 2, 13: 0, 14: 0, 15: 0, 16: 2}
        self.assertDictEqual(board5.board, dict6)
       
        # test expected update in score
        self.assertEqual(board5.score, 24)

        # case 3 
        # two merges in different rows
        dict7 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 2, 7: 2, 8: 4, 9: 0, 10: 8, 11: 4, 12: 4, 13: 0, 14: 0, 15: 0, 16: 2}
        board6 = Board(dict7, 4, 0)
        board6.left_right_merge(-1)
        
        # test expected board dict after right merge
        dict8 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 4, 8: 4, 9: 0, 10: 8, 11: 0, 12: 8, 13: 0, 14: 0, 15: 0, 16: 2}
        self.assertDictEqual(board6.board, dict8)
        
        # test expected update in score
        self.assertEqual(board6.score, 12)

        # case 4 
        # one merge with three same numbers in the row, where only two of them closest to the right edge merge
        dict9 = {1: 0, 2: 0, 3: 0, 4: 2, 5: 2, 6: 4, 7: 4, 8: 4, 9: 0, 10: 0, 11: 4, 12: 2, 13: 0, 14: 0, 15: 0, 16: 0}
        board7 = Board(dict9, 4, 0)
        board7.left_right_merge(-1)
        
        # test expected board dict after right merge
        dict10 = {1: 0, 2: 0, 3: 0, 4: 2, 5: 2, 6: 4, 7: 0, 8: 8, 9: 0, 10: 0, 11: 4, 12: 2, 13: 0, 14: 0, 15: 0, 16: 0}
        self.assertDictEqual(board7.board, dict10)
        
        # test expected update in score
        self.assertEqual(board7.score, 8)

        # case 5 
        # when merge does not happen again after prior merge
        board7.left_right_merge(-1)
        self.assertDictEqual(board7.board, dict10)

    def test_add_number(self):
        '''
        test method add_number() 
        '''
        # case 1
        # when board is not full and a number gets randomly added
        dict11 = {1: 2, 2: 2, 3: 8, 4: 0, 5: 4, 6: 4, 7: 0, 8: 0, 9: 0, 10: 0, 11: 8, 12: 0, 13: 0, 14: 8, 15: 0, 16: 0}
        board8 = Board(dict11, 4, 0)
        dict12 = dict11.copy()
        count_zero1 = list(dict12.values()).count(0)
        count_two1 = list(dict12.values()).count(2)
        count_four1 = list(dict12.values()).count(4)
        
        board8.add_number()
        count_two2 = list(board8.board.values()).count(2)
        count_four2 = list(board8.board.values()).count(4)
        count_zero2 = list(board8.board.values()).count(0)

        # test if the number of 0s on the board decreases by 1, the number of '2's and '4's increase by 1. 
        self.assertEqual(count_zero2, count_zero1 - 1)
        self.assertEqual(count_two2 + count_four2, count_two1 + count_four1 + 1)

        # test if all original postive key-values pairs are not changed after calling the function
        for key, value in dict12.items():
            if value != 0:
                self.assertEqual(dict12[key], board8.board[key])
        
    def test_str_(self):
        '''
        test method __str__()
        '''
        # case 1
        # when board is not empty and is sized 4x4
        dict13 = {1: 2, 2: 2, 3: 8, 4: 0, 5: 4, 6: 4, 7: 0, 8: 0, 9: 0, 10: 0, 11: 8, 12: 0, 13: 0, 14: 8, 15: 0, 16: 0}
        board9 = Board(dict13, 4, 0)
        print_dict13 = '2  2  8  0\n\n4  4  0  0\n\n0  0  8  0\n\n0  8  0  0\n\n'
        self.assertEqual(board9.__str__(), print_dict13)

        # case 2
        # when board is empty
        dict14 = {}
        board10 = Board(dict14, 4, 0)
        print_dict14 = ''
        self.assertEqual(board10.__str__(), print_dict14)

        # case 3
        # when board is not empty and is sized 5x5
        dict15 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 4, 7: 0, 8: 0, 9: 0, 10: 2, 11: 0, 12: 4,
                  13: 2, 14: 2, 15: 0, 16: 4, 17: 0, 18: 0, 19: 0, 20: 4, 21: 0, 22: 0, 23: 4, 24: 4, 25: 0}
        board11 = Board(dict15, 5, 0)
        print_dict15 = '0  0  0  0  0\n\n4  0  0  0  2\n\n0  4  2  2  0\n\n4  0  0  0  4\n\n0  0  4  4  0\n\n'
        self.assertEqual(board11.__str__(), print_dict15)

    def tets_copy_board(self):
        '''
        test method copy_board()
        '''
        # case 1
        # when creating a new Board instance with same attributes as the prior Board instance 
        dict16 = {1: 2, 2: 2, 3: 8, 4: 0, 5: 4, 6: 4, 7: 0, 8: 0, 9: 0, 10: 0, 11: 8, 12: 0, 13: 0, 14: 8, 15: 0, 16: 0}
        board12 = Board(dict16, 4, 0)
        copy_board12 = board12.copy_board()
        self.assertEqual(board12, copy_board12)

        # case 2
        # when prior object changes and the copy board stays the same
        board12.board[12] = 16
        board12.board[5] = 0
        self.assertNotEqual(board12, copy_board12)

    def test_eq(self):
        '''
        test method __eq__()
        '''
        # true case 1
        # when all attributes are the same
        dict17 = {1: 2, 2: 2, 3: 8, 4: 0, 5: 4, 6: 4, 7: 0, 8: 0, 9: 0, 10: 0, 11: 8, 12: 0, 13: 0, 14: 8, 15: 0, 16: 0}
        board13 = Board(dict17, 4, 12)
        board14 = Board(dict17.copy(), 4, 12)
        self.assertEqual(board13, board14)

        # false case 1
        # when score is different
        board15 = Board(dict17.copy(), 4, 0)
        self.assertNotEqual(board13, board15)

        # false case 2
        # when board and size are different
        dict18 = {1: 2, 2: 2, 3: 8, 4: 0, 5: 4, 6: 4, 7: 0, 8: 0, 9: 0, 10: 0, 11: 8, 12: 0, 13: 0, 14: 8, 15: 0, 16: 0,
                  17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0, 24: 0, 25: 0}
        board16 = Board(dict18, 5, 12)
        self.assertNotEqual(board13, board16)
    
    def test_shift_up(self):
        '''
        test method shift_up()

        '''
        # case 1 
        # when move and merge both happen and random number is added
        dict0 = {1: 0, 2: 0, 3: 0, 4: 4, 5: 0, 6: 4, 7: 4, 8: 0, 9: 4, 10: 0, 11: 4, 12: 2, 13: 2, 14: 2, 15: 0, 16: 2}
        board0 = Board(dict0, 4, 32)
        board0.shift_up()

        # test expected update in score
        self.assertEqual(board0.score, 44)

        # test expected board after shifting up before adding random number
        dict00 = {1: 4, 2: 4, 3: 8, 4: 4, 5: 2, 6: 2, 7: 0, 8: 4, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0}
        dict00_count_0 = list(dict00.values()).count(0)
        for key, value in dict00.items():
            if value != 0:
                self.assertEqual(board0.board[key], dict00[key])

        # test one 0 on board is replaced by a random positive number after adding random number
        board0_count_0 = list(board0.board.values()).count(0)
        self.assertEqual(board0_count_0, dict00_count_0 - 1)
        
        # case 2 
        # when the board doen't change after shifting up, thus no random number is added
        dict1 = {1: 8, 5: 2, 9: 0, 13: 0, 2: 2, 6: 4, 10: 0, 14: 0, 3: 8, 7: 0, 11: 0, 15: 0, 4: 4, 8: 0, 12: 0, 16: 0}
        dict1_count_0 = list(dict1.values()).count(0)
        board1 = Board(dict1, 4, 32)
        board1.shift_up()
        board1_count_0 = list(board1.board.values()).count(0)

        self.assertEqual(board1.board, dict1)
        self.assertEqual(board1_count_0, dict1_count_0)
        self.assertEqual(board1.score, 32)


        # case 3 
        # when up_move changes the board but up_merge doesn't happen.
        dict2 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 4, 10: 4, 11: 0, 12: 2, 13: 2, 14: 2, 15: 4, 16: 4}
        board2 = Board(dict2, 4, 32)
        board2.shift_up()
        board2_count_0 = list(board2.board.values()).count(0)

        # test no change in score (no merging happens)
        self.assertEqual(board2.score, 32)

        # test expected board after shifting up before adding random number
        dict22 = {1: 4, 5: 2, 9: 0, 13: 0, 2: 4, 6: 2, 10: 0, 14: 0, 3: 4, 7: 0, 11: 0, 15: 0, 4: 2, 8: 4, 12: 0, 16: 0}
        dict22_count_0 = list(dict22.values()).count(0)

        for key, value in dict22.items():
            if value != 0:
                self.assertEqual(board2.board[key], dict22[key])

        # test if random number is still added to the board because board moved.
        self.assertEqual(board2_count_0, dict22_count_0 - 1)

    def test_shift_down(self):
        '''
        test method shift_down()

        '''
        # case 1 
        # when move and merge both happen and random number is added
        dict0 = {1: 4, 2: 4, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 4, 9: 2, 10: 0, 11: 4, 12: 2, 13: 0, 14: 2, 15: 0, 16: 2}
        board0 = Board(dict0, 4, 32)
        board0.shift_down()
        board0_count_0 = list(board0.board.values()).count(0)

        # test expected update in score
        self.assertEqual(board0.score, 36)

        # test expected board after shifting down before adding random number
        dict00 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 4, 10: 4, 11: 0, 12: 4, 13: 2, 14: 2, 15: 4, 16: 4}
        for key, value in dict00.items():
            if value != 0:
                self.assertEqual(board0.board[key], dict00[key])

        # test one 0 on board is replaced by a random positive number after adding random number
        dict00_count_0 = list(dict00.values()).count(0)
        self.assertEqual(board0_count_0, dict00_count_0 - 1)

        # case 2
        # when the board doen't change after shifting down, thus no random number is added
        dict1 = {1: 0, 5: 0, 9: 2, 13: 4, 2: 0, 6: 0, 10: 0, 14: 8, 3: 0, 7: 0, 11: 0, 15: 8, 4: 0, 8: 0, 12: 0, 16: 8}
        dict1_count_0 = list(dict1.values()).count(0)
        board1 = Board(dict1, 4, 32)
        board1.shift_down()
        board1_count_0 = list(board1.board.values()).count(0)

        self.assertEqual(board1.board, dict1)
        self.assertEqual(board1_count_0, dict1_count_0)
        self.assertEqual(board1.score, 32)

        # case 3
        # when down_move changes the board but down_merge doesn't happen.
        dict2 = {1: 8, 5: 2, 9: 0, 13: 0, 2: 2, 6: 4, 10: 0, 14: 0, 3: 8, 7: 0, 11: 0, 15: 0, 4: 4, 8: 0, 12: 0, 16: 0}
        board2 = Board(dict2, 4, 32)
        board2.shift_down()
        board2_count_0 = list(board2.board.values()).count(0)

        # test no change in score (no merging happens)
        self.assertEqual(board2.score, 32)

        # test expected board after shifting down before adding random number
        dict22 = {1: 0, 5: 0, 9: 8, 13: 2, 2: 0, 6: 0, 10: 2, 14: 4, 3: 0, 7: 0, 11: 0, 15: 8, 4: 0, 8: 0, 12: 0, 16: 4}
        for key, value in dict22.items():
            if value != 0:
                self.assertEqual(board2.board[key], dict22[key])

        # test if random number is still added to the board because board moved
        dict22_count_0 = list(dict22.values()).count(0)
        self.assertEqual(board2_count_0, dict22_count_0 - 1)
    
    def test_shift_left(self):
        '''
        test method shift_left()

        '''
        # case 1 
        # when move and merge both happen and random number is added
        dict0 = {1: 4, 2: 4, 3: 0, 4: 0, 5: 0, 6: 0, 7: 2, 8: 2, 9: 0, 10: 4, 11: 2, 12: 0, 13: 4, 14: 0, 15: 4, 16: 0}
        board0 = Board(dict0, 4, 32)
        board0.shift_left()
        board0_count_0 = list(board0.board.values()).count(0)

        # test expected update in score
        self.assertEqual(board0.score, 52)

        # test expected board after shifting left before adding random number
        dict00 = {1: 8, 2: 0, 3: 0, 4: 0, 5: 4, 6: 0, 7: 0, 8: 0, 9: 4, 10: 2, 11: 0, 12: 0, 13: 8, 14: 0, 15: 0, 16: 0}
        for key, value in dict00.items():
            if value != 0:
                self.assertEqual(board0.board[key], dict00[key])

        # test one 0 on board is replaced by a random positive number after adding random number
        dict00_count_0 = list(dict00.values()).count(0)
        self.assertEqual(board0_count_0, dict00_count_0 - 1)

        # case 2
        # when the board doen't change after shifting left, thus no random number is added
        dict1 = {1: 4, 2: 0, 3: 0, 4: 0, 5: 2, 6: 4, 7: 0, 8: 0, 9: 4, 10: 0, 11: 0, 12: 0, 13: 4, 14: 2, 15: 4, 16: 0}
        dict1_count_0 = list(dict1.values()).count(0)
        board1 = Board(dict1, 4, 32)
        board1.shift_left()
        board1_count_0 = list(board1.board.values()).count(0)

        self.assertEqual(board1.board, dict1)
        self.assertEqual(board1_count_0, dict1_count_0)
        self.assertEqual(board1.score, 32)

        # case 3
        # when left_move changes the board but left_merge doesn't happen.
        dict2 = {1: 0, 2: 0, 3: 0, 4: 4, 5: 0, 6: 0, 7: 0, 8: 8, 9: 0, 10: 0, 11: 2, 12: 4, 13: 0, 14: 0, 15: 2, 16: 4}
        board2 = Board(dict2, 4, 32)
        board2.shift_left()
        board2_count_0 = list(board2.board.values()).count(0)

        # test no change in score (no merging happens)
        self.assertEqual(board2.score, 32)

        # test expected board after shifting left before adding random number
        dict22 = {1: 4, 2: 0, 3: 0, 4: 0, 5: 8, 6: 0, 7: 0, 8: 0, 9: 2, 10: 4, 11: 0, 12: 0, 13: 2, 14: 4, 15: 0, 16: 0}
        for key, value in dict22.items():
            if value != 0:
                self.assertEqual(board2.board[key], dict22[key])

        # test if random number is still added to the board because board moved
        dict22_count_0 = list(dict22.values()).count(0)
        self.assertEqual(board2_count_0, dict22_count_0 - 1)
    
    def test_shift_right(self):
        '''
        test method shift_right()

        '''
        # case 1 
        # when move and merge both happen and random number is added
        dict0 = {1: 4, 2: 0, 3: 4, 4: 0, 5: 0, 6: 2, 7: 0, 8: 0, 9: 0, 10: 2, 11: 4, 12: 2, 13: 4, 14: 0, 15: 2, 16: 0}
        board0 = Board(dict0, 4, 32)
        board0.shift_right()
        board0_count_0 = list(board0.board.values()).count(0)

        # test expected update in score
        self.assertEqual(board0.score, 40)

        # test expected board after shifting right before adding random number
        dict00 = {1: 0, 2: 0, 3: 0, 4: 8, 5: 0, 6: 0, 7: 0, 8: 2, 9: 0, 10: 2, 11: 4, 12: 2, 13: 0, 14: 0, 15: 4, 16: 2}
        for key, value in dict00.items():
            if value != 0:
                self.assertEqual(board0.board[key], dict00[key])

        # test one 0 on board is replaced by a random positive number after adding random number
        dict00_count_0 = list(dict00.values()).count(0)
        self.assertEqual(board0_count_0, dict00_count_0 - 1)

        # case 2
        # when the board doen't change after shifting right, thus no random number is added
        dict1 = {1: 0, 2: 0, 3: 0, 4: 4, 5: 0, 6: 0, 7: 0, 8: 8, 9: 0, 10: 0, 11: 2, 12: 4, 13: 0, 14: 0, 15: 2, 16: 4}
        dict1_count_0 = list(dict1.values()).count(0)
        board1 = Board(dict1, 4, 32)
        board1.shift_right()
        board1_count_0 = list(board1.board.values()).count(0)

        self.assertEqual(board1.board, dict1)
        self.assertEqual(board1_count_0, dict1_count_0)
        self.assertEqual(board1.score, 32)

        # case 3
        # when right_move changes the board but right_merge doesn't happen.
        dict2 = {1: 4, 2: 0, 3: 0, 4: 0, 5: 2, 6: 4, 7: 0, 8: 0, 9: 4, 10: 0, 11: 0, 12: 0, 13: 4, 14: 2, 15: 4, 16: 0}
        board2 = Board(dict2, 4, 32)
        board2.shift_right()
        board2_count_0 = list(board2.board.values()).count(0)

        # test no change in score (no merging happens)
        self.assertEqual(board2.score, 32)

        # test expected board after shifting right before adding random number
        dict22 = {1: 0, 2: 0, 3: 0, 4: 4, 5: 0, 6: 0, 7: 2, 8: 4, 9: 0, 10: 0, 11: 0, 12: 4, 13: 0, 14: 4, 15: 2, 16: 4}
        for key, value in dict22.items():
            if value != 0:
                self.assertEqual(board2.board[key], dict22[key])

        # test if random number is still added to the board because board moved
        dict22_count_0 = list(dict22.values()).count(0)
        self.assertEqual(board2_count_0, dict22_count_0 - 1)

    def test_iswin(self):
        '''
        test method is_win()

        '''
        # case 1
        # when 2048 appears in board.values() and the board is not full
        dict0 = {1: 2, 2: 2, 3: 8, 4: 128, 5: 4, 6: 64, 7: 0, 8: 0, 9: 0, 10: 32, 11: 8, 12: 64, 13: 0, 14: 8, 15: 0, 16: 2048}
        board17 = Board(dict0, 4, 4500)
        self.assertTrue(board17.is_win(), True)

        # case 2
        # when 2048 appears in board.values() and the board is full
        dict1 = {1: 2, 2: 2, 3: 8, 4: 128, 5: 4, 6: 64, 7: 2, 8: 4, 9: 4, 10: 32, 11: 8, 12: 64, 13: 128, 14: 8, 15: 8, 16: 2048}
        board17 = Board(dict1, 4, 6400)
        self.assertTrue(board17.is_win(), True)

    def test_islose(self):
        '''
        test method is_lose()

        '''
        # case 1
        # when board is full, no merge is detected and no 2048 appears.
        dict0 = {1: 2, 2: 4, 3: 16, 4: 2, 5: 16, 6: 8, 7: 4, 8: 8, 9: 4, 10: 2, 11: 32, 12: 2, 13: 16, 14: 4, 15: 2, 16: 4}
        board18 = Board(dict0, 4, 236)
        self.assertTrue(board18.is_lose(), True)
        
    def test_error_raise_cases(self):
        # error of board type
        with self.assertRaises(ValueError):
            Board([], 4, 0)
        
        # error of score and size type
        with self.assertRaises(ValueError):
            Board({}, 4.0, 0.0)

        # error of size
        with self.assertRaises(ValueError):
            Board({}, 3, 0)
        
        # error of score not being 0
        with self.assertRaises(ValueError):
            Board({}, 6, 8)
        
        # error of socre not being positive
        with self.assertRaises(ValueError):
            Board({}, 6, -16)
        
        # error of score not a multiply of 4
        with self.assertRaises(ValueError):
            Board({}, 6, 15)
        
        # error of dict length not equal size
        with self.assertRaises(ValueError):
            dict0 = {1: 2, 2: 2, 3: 8, 4: 0, 5: 4, 6: 4, 7: 0, 8: 0, 9: 0, 10: 0, 11: 8, 12: 0, 13: 0, 14: 8, 15: 0, 16: 0}
            Board(dict0, 6, 16)
        
        # error of wrong dict key
        with self.assertRaises(ValueError):
            dict2 = {21: 2, 20: 2, 3: 8, 4: 0, 5: 4, 6: 4, 7: 0, 8: 0, 9: 0, 10: 0, 11: 8, 12: 0, 13: 0, 14: 8, 15: 0, 16: 0}
            Board(dict2, 4, 16)
        
        # error of wrong dict value(not powers of 2)
        with self.assertRaises(ValueError):
            dict3 = {1: 12, 2: 1, 3: 9, 4: 0, 5: 4, 6: 4, 7: 0, 8: 0, 9: 0, 10: 0, 11: 8, 12: 0, 13: 0, 14: 8, 15: 0, 16: 0}
            Board(dict3, 4, 16)
        
        # error of dict value bigger than 2048
        with self.assertRaises(ValueError):
            dict4 = {1: 2, 2: 2, 3: 4, 4: 4096, 5: 4, 6: 4, 7: 0, 8: 0, 9: 0, 10: 0, 11: 8, 12: 0, 13: 0, 14: 8, 15: 0, 16: 0}
            Board(dict4, 4, 16)
        
        # error of wrong size
        with self.assertRaises(ValueError):
            Board({}, 0, 0).new_board()
        
        # error of challenge size
        with self.assertRaises(ValueError):
            Board({}, 5, 0).challenge(4)
        
        # error of board being empty
        with self.assertRaises(ValueError):
            Board({}, 5, 0).up_down_move(0)
        
        # error of board being empty
        with self.assertRaises(ValueError):
            Board({}, 4, 0).up_down_merge(-1)

        # error of board being empty
        with self.assertRaises(ValueError):
            Board({}, 4, 0).add_number()
        
        # error of board being full
        with self.assertRaises(ValueError):
            dict5 = {1: 2, 5: 4, 9: 8, 13: 2, 2: 16, 6: 8, 10: 4, 14: 2, 3: 4, 7: 16, 11: 2, 15: 8, 4: 2, 8: 4, 12: 8, 16: 4}
            Board(dict5, 4, 0).add_number()
    
        # error of comparing different types
        with self.assertRaises(ValueError):
            dict5 = {1: 2, 5: 4, 9: 8, 13: 2, 2: 16, 6: 8, 10: 4, 14: 2, 3: 4, 7: 16, 11: 2, 15: 8, 4: 2, 8: 4, 12: 8, 16: 4}
            Board(dict5, 4, 0).__eq__(dict5)

def main():
    unittest.main(verbosity=3)

main()