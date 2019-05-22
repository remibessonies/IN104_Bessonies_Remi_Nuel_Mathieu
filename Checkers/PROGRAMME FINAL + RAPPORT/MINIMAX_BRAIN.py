import IN104_simulateur as simu
from EVALUATION2 import evaluate  
from MINIMAX_FINAL import minimax



class MinimaxBrain:

    def __init__(self, config=None, rules=None):
        self.name = 'AI' # set your AI name here
        

    def play(self, gameState, timeLimit):

        nextStates = gameState.findNextStates()
        max = minimax(nextStates[0],timeLimit/10,-21,21,True,simu.GameState.findNextStates,evaluate)  
        i = 0
        rangMax = 0
        for state in nextStates :
            if minimax(state,timeLimit/10,-21,21,True,simu.GameState.findNextStates,evaluate) > max :
                max = minimax(state,timeLimit/10,-21,21,True,simu.GameState.findNextStates,evaluate)
                rangMax = i
            i += 1
        return(nextStates[rangMax])


    def __str__(self):
        return self.name