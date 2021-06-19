#!/usr/bin/env python3
import boardFunc
from time import monotonic
from random import randrange
class boardState():
    # include the lower level abstraction modules we made and imported    
    # define static tuples for colors
    # this class is a logical representation of the board, it takes the initial gamestate as an arg
    def __init__(self, theBoard):
        self.onColor = (5,25,50)
        self.offColor = (0,0,0)
        self.winColor = (0, 25, 0)
        self.sim = False
        # gives boardState access to the theBoard and patternSize arg passed from init 
        self.theBoard = theBoard
        # the init method takes one argument, the game board
        self.timePressed = monotonic()
        self.eventButt = None
        self.previousButtonPressed = None
        self.gamePlaying = 'eight'
    def debounce(self):
        # filters button inputs, input will only be accepted every 0.2 seconds as measured from last press
        if monotonic() - self.timePressed > 0.2:
            return True
        else:
            return False 
    def checkWin(self):
        # check logical board against win condition, in this case if the board is empty
        if self.onColor not in self.theBoard:
            print('you won')
            return True
    def randomStart(self):
        self.theBoard[randrange(0,15)] = self.onColor
    def clearBoard(self):
        # return a list representation of a blank board
        self.theBoard = [(0,0,0)]*16
    def choseGame(self):
        # if the game type flag starts with 'e' assume eight neighbor game and operate its logic on the board
        # else its four game
        if 'e' in self.gamePlaying:
            self.theBoard = boardFunc.gameLogic(self.theBoard, self.eventButt, self.onColor, self.offColor)
        else:
            self.theBoard = boardFunc.fourNeighborGame(self.theBoard, self.eventButt, self.onColor, self.offColor)
    # this is the first method to go when refactoring for none test builds or when memory errors happen
    def simTest(self):
            if self.checkWin():# check win first to make the if else less heavy on the stack and logical
                            # if a win is registered set the whole board to the win color
                            for i in range(16):
                                self.theBoard[i] = self.winColor
            else:
                #play the game like normal, just no debounce
                self.eventButt = randrange(0,15)
                if not self.eventButt == self.previousButtonPressed:
                    # if not then do the main game logic
                    self.choseGame()    
                else:
                    self.eventButt = randrange(self.previousButtonPressed,15)
                    self.choseGame()
                self.previousButtonPressed = self.eventButt
    def buttonPressed(self, event):
        if self.sim:
            self.eventButt = event
        else:
            self.eventButt = event.number
        # takes theboard and "event" or pressed button as an argument and updates the board state
            if self.debounce():
                # check if the player is pressing the same button they did last turn
                if not self.eventButt == self.previousButtonPressed:
                    # if not then do the main game logic
                    self.previousButtonPressed = self.eventButt
                    # choseGame modify the board state given the flag set on main for the given game
                    self.choseGame()
                    if self.checkWin():
                        # if a win is registered set the whole board to the win color
                        for i in range(16):
                            self.theBoard[i] = self.winColor
                # update the last pressed time for debouncing purposes 
                self.timePressed = monotonic()
