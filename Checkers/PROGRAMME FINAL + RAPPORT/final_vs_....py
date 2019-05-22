import IN104_simulateur as simu
from MINIMAX_BRAIN import MinimaxBrain
from minimaxbrain_alphabeta import MinimaxBrain2
import RandomBrain as rb


brain1 = MinimaxBrain()
#brain2 = MinimaxBrain2()
brain2 = rb.RandomBrain()


ai_time = 0.01 


victoires_brain1 = 0
for i in range(100):
    game = simu.Game(brain1, ai_time, brain2, ai_time, rules = None)
    game.displayLevel = 1   
    game.runGame()
    if game.status['winner']==1:
        victoires_brain1 += 1
print('Nombre de victoires :')
print(victoires_brain1)
