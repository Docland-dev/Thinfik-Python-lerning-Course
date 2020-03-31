""" 
Homework Assignment #6: Advanced Loops


Details:
 
Create a function that takes in two parameters: rows, and columns, both of which are integers.
The function should then proceed to draw a playing board (as in the examples from the lectures)
the same number of rows and columns as specified. After drawing the board,
your function should return True.


Extra Credit:

Try to determine the maximum width and height that your terminal and screen can comfortably fit without wrapping.
If someone passes a value greater than either maximum, your function should return False.
"""



def CreateBoard (rows, columns):
    max_columns = 100
    max_rows = 20
    rows = int(rows)
    columns = int(columns)
    if columns <= max_columns and rows <= max_rows:
        for row in range(rows):
            if row % 2 == 0:
                for column in range(1, columns):
                    if column % 2 == 1:
                        if column != columns - 1:
                            print(" ", end="")
                        else:
                            print(" ")
                    else:
                        print("|", end="")
            else:
                print("-" * columns)
        # when done return True
        return True
    else:
        #check if matrix is fitting to the screen
        reason=""
        if columns > max_columns and rows > max_rows:
            reason = "columns and rows"
        elif columns > max_columns:
            reason += "columns"
        elif rows > max_rows:
            reason += "rows"
        print("Sorry, cannot create the board, too many {0:s}.".format(reason))
        return False
                

CreateBoard(20, 100)