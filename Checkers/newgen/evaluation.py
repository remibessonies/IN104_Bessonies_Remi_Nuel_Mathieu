import IN104_simulateur as simu

def evaluate(gameState) :
    boardState=gameState.boardState
    Cells=boardState.cells
    n=len(Cells)
    d=0
    for i in range(n):
        if Cells[i]==119 or Cells[i]==87 :
            d+=1
        elif Cells[i]==98 or Cells[i]==66 :
            d-=1
    return(d)        





# w : 119
# . : 46
# b : 98
# W : 87
# B : 66
