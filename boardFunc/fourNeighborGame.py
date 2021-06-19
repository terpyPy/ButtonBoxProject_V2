def fourNeighborGame(theBoard, event, onColor, offColor):
    # dict that contains the button numbers and corresponding neighbor cells 
    neighbors = {0:[4, 1],1:[5, 2, 0],2:[1, 6, 3],3:[7, 2], 4:[0, 8, 5],5:[1, 4, 9, 6], 6:[2,5,10,7], 7:[6, 3,11],8:[12, 9,4],9:[5,8,13,10],10:[6,9,14,11],11:[7,10,15],12:[8,13],13:[12,9,14],14:[13,10,15],15:[11,14]}
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
