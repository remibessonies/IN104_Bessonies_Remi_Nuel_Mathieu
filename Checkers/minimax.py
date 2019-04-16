def minimax(state,max_depth,maximize):
	dictionnaire={}
	if state in dictionnaire:
		return(dictionnaire[state])
	if (max_depth==0) or (state.get_children()==[]) or 
		return(state.evaluate())
	else :
		L = state.get_children()
		Scores = []
		for enfant in L:
			score = minimax(enfant,max_depth - 1,not(maximize))
			Scores.append(score)
		if (maximize == True):
			return(max(Scores))
			dictionnaire[state] = max(Scores)
		else :
			return(min(Scores))
			dictionnaire[state] = min(State)