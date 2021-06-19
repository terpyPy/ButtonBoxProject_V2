def idleMenu(event):
    # takes the board, then lights up buttons 0-n which are the game choices,
    # pressing n button returns a string to start n game
    if event == 0:
        return 'four'
    elif event == 1:
        return 'eight'
    else:
        return 'idle'
