import boardStateDriver
from time import sleep
from board import SCL, SDA
import busio
from adafruit_neotrellis.neotrellis import NeoTrellis
from random import randrange

# create the i2c object for the trellis
i2c_bus = busio.I2C(SCL, SDA)   

# create the trellis object with the given i2c object
theTrellis = NeoTrellis(i2c_bus)

# create an instance of the driver for the board which handles logical updates, instantiate it with a blank board
boardDriver = boardStateDriver.boardState([(0,0,0)]*16)

# assign what function should be called when the rising edge of a pushed button event occurs by adding it to the callbacks list
# this will always automatically pass an event object created by the board to the assigned function
for i in range(16):
    theTrellis.activate_key(i, NeoTrellis.EDGE_RISING)
    theTrellis.callbacks[i] = boardDriver.buttonPressed

# light up a random button on the board to set the initial board condition
boardDriver.randomStart()
boardDriver.sim = True
# main program loop where all major code execution should happen
while True:
    # always wait 0.02 seconds before reading/writing to the trellis because it can only update every 17 milliseconds 
    sleep(0.1)
    if boardDriver.sim:
        boardDriver.simTest()
    else:
        continue
    # TODO reset condition
        # boardDriver.previousButtonPressed = None
        # boardDriver.clearBoard()
        # boardDriver.randomStart()
    # redraw the physical board by reading from the logical board
    for i in range(len(boardDriver.theBoard)):
        theTrellis.pixels[i] = boardDriver.theBoard[i]
    if theTrellis.pixels[0] == boardDriver.winColor:
        break
    # run all callbacks triggered by button presses via the sync method
    theTrellis.sync()
