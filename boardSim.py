import random
import boardFunc
from matplotlib import pyplot as plt
theBoard = [[0]*4 for _ in range(4)]

for i in range(16):
    boardFunc.gameLogic(theBoard,random.randrange(0,16),1,0)
    plt.imshow(theBoard)
    plt.show()