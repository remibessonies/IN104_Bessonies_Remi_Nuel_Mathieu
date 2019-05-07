def minimax(state,max_depth,alpha,beta,maximize,get_children,evaluate):
    dictionnaire={}
    if state in dictionnaire :
        return dictionnaire[state]
    if max_depth==0 or get_children(state)==[] :
        return(evaluate(state))
    L = get_children(state)
    n = len(L)
    """Scores = []
    for enfant in L: 
        score = minimax(enfant,max_depth-1,not maximize)
        Scores.append(score)"""
    if maximize == True:
        value = -21
        for enfant in L :
            value = max(value, minimax(enfant,max_depth-1,alpha,beta,False,get_children,evaluate))
            alpha=max(alpha,value)
            if alpha >= beta :
                break
        dictionnaire[state]=value
        return value
        

       
    else:
        value = 21
        for enfant in L :
            value = min(value, minimax(enfant,max_depth-1,alpha,beta,True,get_children,evaluate))
            beta=min(beta,value)
            if alpha >= beta :
                break
        dictionnaire[state]=value
        return value