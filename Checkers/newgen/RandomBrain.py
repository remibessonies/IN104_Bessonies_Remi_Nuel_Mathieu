import IN104_simulateur as simu
import random

import sys
import time

class RandomBrain:

    def __init__(self):
         print("Please enter a name")
         self.name = sys.stdin.readline()[0:-1]
         self.alwaysSeeAsWhite = False

    def play(self, gameState, timeLimit):
        possibleMoves = gameState.findPossibleMoves()
        print(gameState.toDisplay(True))
        print("Authorized moves : ")
        for m in possibleMoves: print(m.toPDN())
        n = len(possibleMoves)
        i = random.randint(0,n-1)
        move = possibleMoves[i]  
        print(move.toPDN())      
        choice = gameState.doMove(move, inplace = False)
        return choice


    def __str__(self):
        return self.name