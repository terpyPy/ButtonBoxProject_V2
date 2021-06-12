import boardFunc
from time import monotonic
from random import randrange, choice
class boardState():

    # include the lower level abstraction modules we made and imported    
    # define static tuples for colors

    # this class is a logical representation of the board, it takes the initial gamestate as an arg
    def __init__(self, theBoard):

        self.onColor = (50,50,50)
        self.offColor = (0,0,0)
        self.winColor = (0, 25, 0)
        self.sim = False
        # gives boardState access to the theBoard and patternSize arg passed from init 
        self.theBoard = theBoard
        
        # the init method takes one argument, the game board
        self.patternSize = 1
        self.timePressed = monotonic()
       
        self.previousButtonPressed = None
    def simTest(self):
        eventButt = choice([0,3,6,9,12,15])
        if not eventButt == self.previousButtonPressed:
            # if not then do the main game logic
            self.previousButtonPressed = eventButt
            self.theBoard = boardFunc.gameLogic(self.theBoard, eventButt, self.onColor, self.offColor)
        else:
            eventButt = choice([1,4,7,9,8])
            self.theBoard = boardFunc.gameLogic(self.theBoard, eventButt, self.onColor, self.offColor)
            self.previousButtonPressed = eventButt
        
        
        

    def debounce(self):
        # filters button inputs, input will only be accepted every 0.2 seconds as measured from last press
        if monotonic() - self.timePressed > 0.2:
            return True
        else:
            return False 

    def checkWin(self):
        # check logical board against win condition, in this case if the board is empty
        if self.onColor not in self.theBoard:
           return True

    # random pattern game init
    def randomStart(self):
        self.theBoard[randrange(0,15)] = self.onColor

    def clearBoard(self):
        # return a list representation of a blank board
        self.theBoard = [(0,0,0)]*16

    def buttonPressed(self, event):
        
        if self.sim:
            eventButt = event
        else:
            eventButt = event.number
        
        # takes theboard and "event" or pressed button as an argument and updates the board state
            if self.debounce():
                # check if the player is pressing the same button they did last turn
                if not eventButt == self.previousButtonPressed:
                    # if not then do the main game logic
                    self.previousButtonPressed = eventButt
                    self.theBoard = boardFunc.gameLogic(self.theBoard, eventButt, self.onColor, self.offColor)
                    if self.checkWin():
                        # if a win is registered set the whole board to the win color
                        for i in range(16):
                            self.theBoard[i] = self.winColor

            
                # update the last pressed time for debouncing purposes 
                self.timePressed = monotonic()

    def buttonCheck(self, event):
        timeBetween = monotonic() - self.timePressed
        print(timeBetween)
        print(self.previousButtonPressed)
        print(0.07 < timeBetween)
        if (timeBetween > 0.5) and not (timeBetween > 1.7):
            if (event.number == self.previousButtonPressed):
                print("cond met")
                self.theBoard[1] = self.winColor
    

    # def buttonPressed(self, event):
    #     if event.number == 15:
    #         self.clearBoard()
    #     self.buttonCheck(event)
    #     self.previousButtonPressed = event.number
    #     self.timePressed = monotonic()    
