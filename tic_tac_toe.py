from turtle import *

def main():
    
    setup_board()
    
    # win conditions
    win_conditions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    won = False

    # setting up blank, untaken squares
    squares = [False, False, False, False, False, False, False, False, False]

    # resetting the game
    p1_moves = []
    p2_moves = []
    turns = 0
    counter = 0
    winning_combo = -1 # final winning line index from win_conditions


    # game
    while won == False:
        
        p1_input = get_input("x", squares)
        
        # proper input was given
        squares[p1_input - 1] = True
        p1_moves.append(p1_input)
        turns += 1
        square_draw(p1_input - 1, "x")
        
        # test for win
        winning_combo = win_test(p1_moves, win_conditions)    # if there is a winning combo the index will be returned
        if winning_combo != -1:
            won = True
            print("p1 wins")
            draw_win(win_conditions[winning_combo], winning_combo)
            break
                    
        
        # All squares filled; tie
        if turns == 9:
            print("Tie")
            break
        
        p2_input = get_input("o", squares)
    
        # proper input was given
        squares[p2_input - 1] = True
        p2_moves.append(p2_input)
        turns += 1
        
        square_draw((p2_input - 1), "o")
        
        # test for win
        winning_combo = win_test(p2_moves, win_conditions)    # if there is a winning combo the index will be returned
        if winning_combo != -1:
            won = True
            print("p2 wins")
            draw_win(win_conditions[winning_combo], winning_combo)
            break
                 

    mainloop()


def setup_board():
    # setup board
    hideturtle()
    pensize(5)
    speed(10000)
    # horizontal lines
    penup()
    goto(-300, 100)
    pendown()
    forward(600)

    penup()
    goto(-300, -100)
    pendown()
    forward(600)

    # vertical lines
    penup()
    goto(-100, 300)
    right(90)
    pendown()
    forward(600)

    penup()
    goto(100, 300)
    pendown()
    forward(600)

def get_input(letter, squares):
    player_input = -1
    number = 1 if letter == "x" else 2  # player number (using cool ternary assignment)
    
    # forcing user to give proper input, before the program continues
    while True:
        try:
            player_input = int(input(f"Player {number}: where would you like to place your {letter.upper()}? "))
        except ValueError:
            print("Try again; make sure you type an integer from 1-9 and there is nothing already in the square.")
            continue
        if 0 < player_input < 10 and squares[player_input - 1] == False:
            return player_input
        else:
            print("Try again; make sure you type an integer from 1-9 and there is nothing already in the square.")
            continue

def square_draw(square_number, letter):
    if letter == "o":
        penup()
        setheading(0)
        xaxis = (-200 + ((square_number % 3 * 200)))
        yaxis = (125 - (int(square_number / 3) * 200))
        goto(xaxis, yaxis)
        color("blue")
        pendown()
        circle(75)
    
    elif letter == "x":
        penup()
        setheading(0)
        right(45)
        xaxis = (-200 + (((square_number) % 3 * 200)))
        yaxis = (200 - (int(square_number / 3) * 200))
        goto(xaxis, yaxis)
        color("red")
        
        # diagonals
        pendown()
        forward(75)
        backward(150)
        forward(75)
        right(90)
        forward(75)
        backward(150)

def win_test(moves, win_conditions):
    counter = 0
    for i in range(8):
        counter = 0
        for j in range(3):
            if win_conditions[i][j] in moves:
                counter += 1
            
            if counter == 3:
                return i
    
    return -1

def draw_win(number_combo, position):
    pensize(8)
    speed(5)
    # diagonals
    if position > 5:
        if position == 6:
            penup()
            goto(-300, 300)
            setheading(0)
            right(45)
            pendown()
            forward(848.5)
        else:
            penup()
            goto(300, 300)
            setheading(0)
            right(135)
            pendown()
            forward(848.5)


    # verticals    
    elif position > 2:
        penup()
        xaxis = ((position % 3) * 200) - 200
        goto(xaxis, 300)
        setheading(0)
        right(90)
        pendown()
        forward(600)
    # horizontals
    else:
        penup()
        yaxis = (200 - (position % 3) * 200)
        goto(-300, yaxis)
        setheading(0)
        pendown()
        forward(600)


        

main()