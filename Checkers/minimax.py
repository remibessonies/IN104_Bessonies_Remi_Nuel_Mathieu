i=0

def minimax(state,max_depth,maximize)
	if max_depth==0:
		return(state.evaluate(state))
	L = state.get_children()
	n = len(L)
	Scores = []
	for enfant in L: 
		score = minimax(enfant,max_depth-1,!maximize)
		Scores.append(score)

	if maximize == True:
		nombre = max(minimax(enfant,max_depth-1,False),minimax(enfant2,max_depth-1,False))
	else :
		nombre = min(minimax(enfant1,max_depth-1,True),minimax(enfant2,max_depth-1,True))


#fonctions max et min d'une liste