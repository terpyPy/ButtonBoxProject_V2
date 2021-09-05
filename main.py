#!/usr/bin/env python3
from boardFunc import funcTest
import boardStateDriver
from time import sleep
from board import SCL, SDA
import busio
from adafruit_neotrellis.neotrellis import NeoTrellis
# create the i2c object for the trellis
i2c_bus = busio.I2C(SCL, SDA)   
# create the trellis object with the given i2c object
theTrellis = NeoTrellis(i2c_bus)
<<<<<<< Updated upstream
boardDriver = boardStateDriver.boardState([(0,0,0)]*16)
=======

# create an instance of the driver for the board which handles logical updates, instantiate it with a blank board
boardDriver = boardStateDriver.boardState(16)

>>>>>>> Stashed changes
# assign what function should be called when the rising edge of a pushed button event occurs by adding it to the callbacks list
# this will always automatically pass an event object created by the board to the assigned function
for i in range(16):
    theTrellis.activate_key(i, NeoTrellis.EDGE_RISING)
<<<<<<< Updated upstream
    theTrellis.callbacks[i] = boardDriver.buttonPressed
# light up a random button on the board to set the initial board condition
theTrellis.pixels.fill(boardDriver.offColor)
boardDriver.randomStart()
# set the sim flag
boardDriver.sim = bool(input('sim the game?: '))
# set the game type default it eight
boardDriver.gamePlaying = input('game type: ')
while True:
    # always wait 0.02 seconds
    sleep(0.023)
    if boardDriver.sim:
        boardDriver.simTest()
    # redraw the physical board by reading from the logical board
    for i in range(16):
        theTrellis.pixels[i] = boardDriver.theBoard[i]
    # if the game has been won stop
    if boardDriver.winColor == boardDriver.theBoard[0]:
        sleep(5)
        boardDriver.previousButtonPressed = None
        boardDriver.clearBoard()
        boardDriver.randomStart()
=======
    theTrellis.callbacks[i] = boardDriver.boardLogic

boardDriver.randomStart()
# main program loop where all major code execution should happen
while True:
    # always wait 0.02 seconds before reading/writing to the trellis because it can only update every 17 milliseconds 
    sleep(0.02)
    # redraw the physical board by reading from the logical board
    for i in range(16):
        #boardDriver.animation()
        y,x =funcTest.arrayMap(i,4)
        theTrellis.pixels[i] = boardDriver.theBoard[y][x]
>>>>>>> Stashed changes
        # run all callbacks triggered by button presses via the sync method
    if boardDriver.winColor == boardDriver.theBoard[0][0]:
        sleep(3)
        boardDriver.clearBoard()
    theTrellis.sync()
