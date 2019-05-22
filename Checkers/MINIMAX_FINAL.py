import time

def minimax(state,T,alpha,beta,maximize,get_children,evaluate):
    dictionnaire={}
    if state in dictionnaire :
        return dictionnaire[state]

    if (T <= 5e-5) :
        return(evaluate(state))
    L = get_children(state)
    if (L==[]):
        return(evaluate(state))

    n = len(L)

    if maximize == True:

        Tdispo = T
        #Temps = []
        compt_enfants = 0
        debut = time.time()
        value = -21
        
        for enfant in L :
            value = max(value, minimax(enfant,Tdispo/(len(L)-compt_enfants),alpha,beta,False,get_children,evaluate))
            alpha=max(alpha,value)
            if alpha >= beta :
                break
            fin = time.time()
            Treel= fin - debut
            Tdispo = T-Treel
           
            compt_enfants = compt_enfants + 1
        
        dictionnaire[state]=value
        return value
        

       
    else:

        Tdispo = T
        compt_enfants = 0
        debut = time.time()
        value = 21

        for enfant in L :
            value = min(value, minimax(enfant,Tdispo/(len(L)-compt_enfants),alpha,beta,True,get_children,evaluate))
            beta=min(beta,value)
            if alpha >= beta :
                break
            fin = time.time()
            Treel= fin - debut
            Tdispo = T-Treel
            compt_enfants = compt_enfants + 1
            
        dictionnaire[state]=value
        return value