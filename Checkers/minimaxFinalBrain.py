import IN104_simulateur as simu
from evaluation2 import evaluate  #modifier ici pour evaluate 1 ou 2
from minimaxFinal import minimax



class MinimaxBrain:

    def __init__(self, config=None, rules=None):
        self.name = 'PierrickAB' # set your AI name here
        self.depth = 1 # Set the exploration depth here
        


    def play(self, gameState, timeLimit):

        nextStates=gameState.findNextStates()
        max = minimax(nextStates[0],self.depth,-21,21,True,simu.GameState.findNextStates,evaluate)
        i=0
        rangMax=0
        for state in nextStates :
            if minimax(state,self.depth,-21,21,True,simu.GameState.findNextStates,evaluate) > max :
                max = minimax(state,self.depth,-21,21,True,simu.GameState.findNextStates,evaluate)
                rangMax=i
            i+=1
        return(nextStates[rangMax])


    def __str__(self):
        return self.name