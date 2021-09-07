from . import funcTest
def gameLogic(theBoard, event, onColor, offColor):
    #
    # get the 1d event button mapping for grid
    row, col = funcTest.arrayMap(event,4)
    #
    # algorithm corresponding 8 neighbor cell calc
    neighbors = funcTest.neighbors(theBoard, row,col)
    #
    #  unpack the column and row values calc from neighbors y,x orientation to match how board is drawn.
    for y, x in neighbors:
        # first check if the neighbor in the list is off on the game board
        if theBoard[y][x] == offColor:
            # if its not turned on turn y=the light on
            theBoard[y][x] = onColor
        # elif the neighbor cell is not eqaul to the off color thens its turned on
        elif theBoard[y][x] != offColor:
            # so we turn it off it the prevouis isnt true
            theBoard[y][x] = offColor
    # turn off the pressed key
    theBoard[row][col] = offColor
    # return the new board
    return theBoard