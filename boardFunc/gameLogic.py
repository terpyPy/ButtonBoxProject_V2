from . import funcTest
def gameLogic(theBoard, event, onColor, offColor):
    #
<<<<<<< Updated upstream
    # dictionary that contains button numbers and their corresponding direct neighbor cells (does not include corner neighbors)
    neighbors ={0:(4, 1, 5), 1:(5, 2, 0, 4, 6), 2:(1, 6, 3, 5, 7), 3:(7, 2, 6), 4:(0, 8, 5, 1, 9), 5:(1, 4, 9, 6, 0, 2, 8, 10), 6:(2, 5, 10, 7, 1, 3, 9, 11), 7:(6, 3, 11, 2, 10), 8:(12, 9 , 4, 5, 13), 9:(5, 8, 13, 10, 4, 6, 12, 14), 10:(6, 9, 14, 11, 5, 7, 13, 15), 11:(7, 10, 15, 6, 14), 12:(8, 13, 9),
                13:(12, 9, 14, 8, 10),
                14:(13, 10, 15, 9, 11),
                15:(11, 14, 10)}
    theBoard[event] = offColor
    # get the range length of the list of neighbor cells 
    for i in range(len(neighbors[event])):
        # pass the neighbors dict the key(which is the button pressed number)
        # and the pass i for the index of the value of each neighbor cell and turn it on
        if theBoard[neighbors[event][i]] == offColor:
            theBoard[neighbors[event][i]] = onColor
        elif theBoard[neighbors[event][i]] == onColor:
            theBoard[neighbors[event][i]] = offColor
    return theBoard
=======
    # get the 1d event button mapping for grid
    row, col = funcTest.arrayMap(event,4)
    #
    # algorithm corresponding 8 neighbor cell calc
    neighbors = funcTest.neighbors(theBoard, row,col)
    #
    #  unpack the column and row values calc from neighbors y,x orientation to match how board is drawn.
    for y, x in neighbors:
        if theBoard[y][x] == offColor:
            theBoard[y][x] = onColor
        elif theBoard[y][x] == onColor:
            theBoard[y][x] = offColor
    # turn off the pressed key
    theBoard[row][col] = offColor
    print(event, 'cords are: ',[row], [col])
    # return the new board
    return theBoard
>>>>>>> Stashed changes
