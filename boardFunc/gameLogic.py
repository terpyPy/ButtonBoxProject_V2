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
        if theBoard[y][x] == offColor:
            theBoard[y][x] = onColor
        elif theBoard[y][x] == onColor:
            theBoard[y][x] = offColor
    # turn off the pressed key
    theBoard[row][col] = offColor
    print(theBoard)
    # return the new board
    return theBoard