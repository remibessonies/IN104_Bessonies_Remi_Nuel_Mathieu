#To launch a game between two players with the default config:
import IN104_simulateur as simu
import RandomBrain as rb
brain1 = rb.RandomBrain()
brain2 = rb.RandomBrain()
timeLimit = 10 # each player will have 10 seconds to play
game = simu.Game(brain1, timeLimit, brain2, timeLimit)
game.runGame()
print(game.pdn) # display the game summary
fichier = open("log.txt","w")
fichier.write(game.pdn)
fichier.close