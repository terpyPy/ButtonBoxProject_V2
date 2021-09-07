#!/usr/bin/env python3
import boardFunc
from time import monotonic
from random import randrange
from math import sqrt
class boardState():
    # include the lower level abstraction modules we made and imported    
    # define static tuples for colors
    # this class is a logical representation of the board, it takes the initial gamestate as an arg
    def __init__(self, gridSize):
        self.onColor = (200,18,20)
        self.offColor = (0,0,0)
        self.winColor = (0, 25, 0)
        self.N = int(sqrt(gridSize))
        self.theBoard = [[self.offColor]*self.N for _ in range(self.N)]# the init method takes one argument, the grid size
        self.timePressed = monotonic()
        self.eventButt = None
        self.previousButtonPressed = None

    def debounce(self):
        # filters button inputs, input will only be accepted every 0.2 seconds as measured from last press
        if monotonic() - self.timePressed > 0.2:
            return True
        else:
            return False 

    def checkWin(self):
        flatlist = sum(self.theBoard, [])
        print(flatlist)
        # check logical board against win condition, in this case if the board is empty
        if self.onColor not in flatlist:
            print('you won')
            return True
    def animation(self):
        self.previousButtonPressed = randrange(16)
        self.theBoard = boardFunc.gameLogic(self.theBoard, self.previousButtonPressed,self.onColor,self.offColor)
        
    # random pattern game init
    def randomStart(self):
        for i in range(0,15):
            self.previousButtonPressed = randrange(i,16)
            self.theBoard = boardFunc.gameLogic(self.theBoard, self.previousButtonPressed,self.onColor,self.offColor)
    def clearBoard(self):
        self.previousButtonPressed = None
        self.theBoard = [[self.offColor]*self.N for _ in range(self.N)]
        self.randomStart()

    def boardLogic(self, event):
        self.eventButt = event.number
        # takes theboard and "event" or pressed button as an argument and updates the board state
        if self.debounce():
            # check if the player is pressing the same button they did last turn
            if not self.eventButt == self.previousButtonPressed:
                # if not then do the main game logic
                self.previousButtonPressed = self.eventButt
                # run the game
                self.theBoard = boardFunc.gameLogic(self.theBoard,self.eventButt,self.onColor,self.offColor)
                if self.checkWin():
                        # if a win is registered set the whole board to the win color
                        for row in range(self.N):
                            for col in range(self.N):
                                self.theBoard[row][col] = self.winColor 
            # update the last pressed time for debouncing purposes 
            self.timePressed = monotonic()
