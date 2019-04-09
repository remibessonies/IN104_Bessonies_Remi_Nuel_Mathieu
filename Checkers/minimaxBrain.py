import IN104_simulateur as simu
from evaluation import evaluate
from minimax import minimax
simu.GameState.get_children = simu.GameState.findNextStates
simu.GameState.evaluate = evaluate

class MinimaxBrain:

    def __init__(self, config=None, rules=None):
        self.name = 'Pierrrick' # set your AI name here
        self.depth = 5 # Set the exploration depth here



    def play(self, gameState, timeLimit):

        nextStates=gameState.findNextStates()
        max = minimax(nextStates[0],self.depth,True)
        i=0
        rangMax=0
        for state in nextStates :
            if minimax(state,self.depth,True) > max :
                max = minimax(state,self.depth,True)
                rangMax=i
            i+=1
        return(nextStates[rangMax])




        #use minimax here to return the next state with higher score
        raise NotImplementedError() # remove this error once it is done



    def __str__(self):
        return self.name