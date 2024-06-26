from Board_2048 import Board
import math
import turtle

def main():
    '''
    the main() presents Board 2048 by python turtle and interacts with python by screen key press.
    during the game, the board and related messages are presented both on terminal and Turtle window.
    possible screen keys include:

    1: menu option 1; start a board size 4x4 game
    2: menu option 2; quit game by turning off turtle
    3: menu option 3; challenge a new board size and start a new game
    Up: press up-arrow key, calling shift_up() from Board
    Down: press down-arrow key, calling shift_down() from Board
    Left: press left-arrow key, calling shift_left() from Board
    Right: press right-arrow key, calling shift_right() from Board

    '''
    draw_board_bg()
    game = Board()
    game.board = {}
    game.size = 4
    game.new_board()
    print('Game ON ! !\n\n')
    print(game)
    draw_board(game)
    

    def draw_print():
        '''
        this function updates screen on turtle and terminal
        '''
        print(game)
        draw_board(game)
        draw_lose(game)
        draw_win(game)
            
    def up():
        '''
        this function calls shift_up() from Board
        '''
        if game.board != {}:
            game.shift_up()
            draw_print()

    def down():
        '''
        this function calls shift_down() from Board
        '''
        if game.board != {}:
            game.shift_down()
            draw_print()
        
    def left():
        '''
        this function calls shift_left() from Board
        '''
        if game.board != {}:
            game.shift_left()
            draw_print()

    def right():
        '''
        this function calls shift_right() from Board
        '''
        if game.board != {}: 
            game.shift_right() 
            draw_print()

    def new_game():
        '''
        this function initializes a 4x4 new board board game.
        '''
        game.board = {}
        game.size = 4
        game.new_board()
        print('start a 4x4 new game\n\n')
        draw_print()

    def challenge_game():
        '''
        this function challenges for a bigger size board game.
        '''
        board_size = turtle.numinput('Challenges','Input the board size you want to challenge')

        # when click cancel on the message window
        if board_size == None:
            print('keep going')

        # when input a size and press enter
        else:
            # if keep wrong input in the loop
            while board_size < 5:
                board_size = turtle.numinput('Challenges','input should be bigger than 4')
                
                # break loop when click cancel after wrong input last time
                if board_size == None:
                    print('keep going')
                    break
            else:
                # when input >=5 and press enter after wrong input last time
                game.challenge(int(board_size))
                game.new_board()
                print(f"start a {int(board_size)}x{int(board_size)} new game\n\n")
                draw_print()
        turtle.listen()
    
    turtle.onkey(new_game, "1")
    turtle.onkey(quit_game, "2")
    turtle.onkey(challenge_game, "3")
    turtle.onkey(up, "Up")
    turtle.onkey(down, "Down")
    turtle.onkey(left, "Left")
    turtle.onkey(right, "Right")
    turtle.listen() 
      
    turtle.mainloop()
  
    
def quit_game():
    '''
    this function turns off turtle 
    '''
    turtle.clear()
    def slogan():
        turtle.pu()
        turtle.goto(-80, 150)
        turtle.pencolor('red')
        turtle.write('****** See You ******', font = ('Comic Sans MS', 28, 'normal'))
        turtle.ontimer(quit, 500)
    def quit():
        turtle.bye()
    print('bye bye~')
    slogan()


def draw_board_bg():
    '''
    the function draws a pre-game background and shows a menu to the user.
    optional inputs include menu options: 1, 2, 3.
    '''
    window = turtle.Screen()
    window.setup(700, 700)
    window.tracer(0)
    turtle.colormode(255)
    turtle.hideturtle()
    turtle.title('Board 2048')

    t = turtle.Turtle()
    t.hideturtle()
    t.pensize(3)
    draw_rectangle(t, -320, 100, (192, 192, 192), 160, 150)
    t.pencolor(127, 0, 255)
    t.pu()
    t.goto(-150, 300)
    t.pu()
    t.write('*** Welcome to 2048 ***', font = ('Comic Sans MS', 25, 'normal'))
    t.goto(0, -150)
    t.pencolor('red')
    t.write('    Game On !', font = ('Comic Sans MS', 18, 'normal'))
    t.goto(-50, -180)
    t.write('Press Arrow Key for playing or Any number on the Menu', font = ('Comic Sans MS', 14, 'normal'))
    t.pencolor(127, 0, 255)
    t.goto(-200, -250)
    t.write('Join the numbers and get to the 2048 tile!', font = ('Comic Sans MS', 18, 'normal'))

    t.pu()
    t.goto(-310, 120)
    contents = 'Menu\n1. new game\n2. Quit\n3. Challenges'
    t.write(contents, font = ('Comic Sans MS', 20, 'normal'))
    window.update()


def draw_board(game: Board):
    '''
    the function draws update on user-interactions with board numbers and scores during the game.
    optional inputs include: 1, 2, 3, Up, Down, Left, Right.
    '''
    window = turtle.Screen()
    window.tracer(0)
    turtle.colormode(255)
    turtle.pensize(3)
    turtle.clear()
    turtle.hideturtle()

    for i in range(1, game.size * (game.size - 1) + 2, game.size):
        for j in range(i, game.size + i):
            x = -30 + 60 * (j - i)
            y = 120 - 60 * (i // game.size)

            # cell color for positive numbers change in accordance with number value
            if game.board[j] != 0:
                power_number = int(math.log2(game.board[j]))
                color = (255 - power_number * 20, 150 - 10 * power_number, 35 + 20 * power_number) # abc
                draw_rectangle(turtle, x, y, color, 60, 60)

            turtle.pu()
            turtle.pencolor('white')
            if game.board[j] == 0:
                draw_rectangle(turtle, x, y, (128, 128, 128), 60, 60)
            
            # conditions for number size and location when it grows bigger in digits
            elif game.board[j] < 10:  
                turtle.goto(x + 25, y + 15)
                turtle.write(game.board[j], font = ('Arial', 24, 'normal'))

            elif game.board[j] < 100:  
                turtle.goto(x + 20, y + 15)
                turtle.write(game.board[j], font = ('Arial', 22, 'normal'))

            elif game.board[j] < 1000:  
                turtle.goto(x + 14, y + 15)
                turtle.write(game.board[j], font = ('Arial', 21, 'normal'))

            else:  
                turtle.goto(x + 11, y + 15)
                turtle.write(game.board[j], font = ('Arial', 20, 'normal'))
    
    draw_rectangle(turtle, -30, 190, (192, 192, 192), 140, 60)
    turtle.pu() 
    turtle.pencolor(127, 0, 255)
    turtle.goto(-10, 210)
    turtle.write(f"score: {game.score}", font = ('Comic Sans MS', 20, 'normal'))
    window.update()


def draw_lose(game: Board):
    '''
    this function prints out lose message on turtle screen
    '''
    if game.is_lose():
        turtle.pu()
        turtle.goto(-290, - 120)
        turtle.pencolor('green')
        turtle.write(f"***Game Over***", font = ('Comic Sans MS', 28, 'normal'))


def draw_win(game: Board):
    '''
    this function prints out win message on turtle screen
    '''
    if game.is_win():
        turtle.pu()
        turtle.goto(-290, - 120)              
        turtle.pencolor(255, 51, 255)
        turtle.write(f"Congratulations!\n\n***You Win***", font = ('Comic Sans MS', 25, 'normal'))

        # freeze any arrow key event when win message prints out. only menu options are available
        game.board = {}

# helper function 
def draw_rectangle(t, x, y, color, edge_y, edge_x):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.color((96, 96, 96),color)
    t.begin_fill()
    t.forward(edge_y)
    t.left(90)
    t.forward(edge_x)
    t.left(90)
    t.forward(edge_y)
    t.left(90)
    t.forward(edge_x)
    t.end_fill()  

if __name__ == "__main__":
    main()