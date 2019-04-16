def minimax(state,max_depth,alpha,beta,maximize):
    dictionnaire={}
    if state in dictionnaire :
        return dictionnaire[state]
    if max_depth==0 or state.get_children()==[] :
        return(state.evaluate())
    L = state.get_children()
    n = len(L)
    """Scores = []
    for enfant in L: 
        score = minimax(enfant,max_depth-1,not maximize)
        Scores.append(score)"""
    if maximize == True:
        value = -21
        for enfant in L :
            value = max(value, minimax(enfant,max_depth-1,alpha,beta,False))
            alpha=max(alpha,value)
            if alpha >= beta :
                break
        dictionnaire[state]=value
        return value
        

       
    else:
        value = 21
        for enfant in L :
            value = min(value, minimax(enfant,max_depth-1,alpha,beta,True))
            beta=min(beta,value)
            if alpha >= beta :
                break
        dictionnaire[state]=value
        return value
