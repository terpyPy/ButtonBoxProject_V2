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
        self.simColor = (10, 93, 30)
        self.N = int(sqrt(gridSize))
        self.theBoard = [[self.offColor]*self.N for _ in range(self.N)]# the init method takes one argument, the grid size
        self.timePressed = monotonic()
        self.eventButt = None
        self.previousButtonPressed = 0
        self.mode = None

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
        if flatlist == [(0,0,0)]*16:
            print('you won')
            return True

    def animation(self):
        # this function runs the game in a way where each button press is random
        # and the color is as well, and it uses the real game anb board logic to produce an animation.
        self.onColor = (randrange(0,254),randrange(27,254),randrange(0,254))
        simPress = randrange(0,16)
        self.boardLogic(simPress)

    def choseMode(self):
            self.theBoard[0][0] = self.onColor
            self.theBoard[0][1] = self.simColor
            self.theBoard[0][2] = (123,30,170)
            if self.eventButt == 0:
                self.mode = 'run'
                self.clearBoard()
            elif self.eventButt == 1:
                # event = 1
                self.mode = 'sim'
                self.clearBoard()
            elif self.eventButt == 2:
                self.mode = 'draw'
                self.clearBoard()

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
        # self.onColor = (randrange(0,254),randrange(27,254),randrange(0,254))
        #print(self.mode)
        # the sim mode flag needs to use an interget value while button presses are key events
        # so if we chose sim mode, leave the event as a int value if not use the event.number data type.
        if self.mode != 'sim':
            self.eventButt = event.number
        else:
            self.eventButt = event
        # takes theboard and "event" or pressed button as an argument and updates the board state
        if self.debounce():
            # check if the player is pressing the same button they did last turn
            if not self.eventButt == self.previousButtonPressed:
                print(event)
                # if not then do the main game logic
                self.previousButtonPressed = self.eventButt
                # run the game
                self.theBoard = boardFunc.gameLogic(self.theBoard,self.eventButt,self.onColor,self.offColor)
                if self.mode != 'draw':
                # if the mode flag isnt set to draw check the win condition
                    if self.checkWin():
                        for row in range(self.N):
                                for col in range(self.N):
                                    self.theBoard[row][col] = self.winColor
            else:
                print('debounce failed')
                                    
            # update the last pressed time for debouncing purposes 
            self.timePressed = monotonic()

