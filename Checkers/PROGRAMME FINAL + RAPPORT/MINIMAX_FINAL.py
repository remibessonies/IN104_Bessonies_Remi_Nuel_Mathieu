import time

def minimax(state,T,alpha,beta,maximize,get_children,evaluate):
    dictionnaire = {}  # Le dictionnaire permet de ne pas recalculer des états déja évalués
    if state in dictionnaire :
        return dictionnaire[state]

    if (T <= 5e-5) :   # 5e-5 est la valeur moyenne pour faire un getchildren que l'on a observé en faisait des essais
        return(evaluate(state))

    L = get_children(state)  # Liste des enfants d'un état
    
    if (L==[]):
        return(evaluate(state))

    n = len(L)

    if maximize == True:   # Pour alpha beta on fait 2 cas en fonction de maximize

        Tdispo = T # Temps disponible restant
        compt_enfants = 0   # On a besoin de compter le nombre d'enfants déja traités car le nouveau temps disponible va dépendre de ce nombre 
        debut = time.time()  # Début du compteur de temps
        value = -21       # Valeur extrême du score d'un état
        
        for enfant in L :
            value = max(value, minimax(enfant,Tdispo/(len(L) - compt_enfants),alpha,beta,False,get_children,evaluate))
            alpha = max(alpha,value)
            if alpha >= beta :
                break
            fin = time.time()
            Treel = fin - debut
            Tdispo = T - Treel  # On décrémente le temps disponible restant
            compt_enfants = compt_enfants + 1
        
        dictionnaire[state]=value
        return value
        

    else:   # 2ème cas pour alpha beta

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
            Treel = fin - debut
            Tdispo = T-Treel
            compt_enfants = compt_enfants + 1
            
        dictionnaire[state] = value
        return value