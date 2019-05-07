import IN104_simulateur as simu
from minimaxBrain import MinimaxBrain
from minimaxBrainAlphaBeta import MinimaxBrainAB


    

brain1 = MinimaxBrain(config = simu.Game.defaultConfig, rules = simu.Game.CheckersRules)
brain2 = MinimaxBrainAB()
ai_time = 10 #the AI will only have 1 sec to play
game = simu.Game(brain2, ai_time, brain1, ai_time, rules = None)
game.displayLevel = 1   # this prints the board after each move
game.runGame()
print(game.pdn) #print the summary of the game. 
