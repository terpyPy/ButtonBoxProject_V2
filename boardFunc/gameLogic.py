def gameLogic(theBoard, event, onColor, offColor):
    #
    # dictionary that contains button numbers and their corresponding direct neighbor cells (does not include corner neighbors)
    neighbors ={0:(4, 1, 5),
                1:(5, 2, 0, 4, 6),
                2:(1, 6, 3, 5, 7),
                3:(7, 2, 6),
                4:(0, 8, 5, 1, 9),
                5:(1, 4, 9, 6, 0, 2, 8, 10),
                6:(2, 5, 10, 7, 1, 3, 9, 11),
                7:(6, 3, 11, 2, 10),
                8:(12, 9 , 4, 5, 13),
                9:(5, 8, 13, 10, 4, 6, 12, 14),
                10:(6, 9, 14, 11, 5, 7, 13, 15),
                11:(7, 10, 15, 6, 14),
                12:(8, 13, 9),
                13:(12, 9, 14, 8, 10),
                14:(13, 10, 15, 9, 11),
                15:(11, 14, 10)}
    keyPressed = event
    newBoard = theBoard
    # turn off the pressed key
    newBoard[keyPressed] = offColor
    # do this loop i times, where i is the number of neighbors for the pressed button 
    for i in range(len(neighbors[keyPressed])):
        # invert the value of this neighbor of the pressed button
        if theBoard[neighbors[keyPressed][i]] == offColor:
            newBoard[neighbors[keyPressed][i]] = onColor
        elif theBoard[neighbors[keyPressed][i]] == onColor:
            newBoard[neighbors[keyPressed][i]] = offColor
    # return the new board
    return newBoard
