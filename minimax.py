def minimax(state,max_depth,maximize):
	if (max_depth==0) or (state.get_children()==[]):
		return(state.evaluate())
	else :
		L = state.get_children()
		Scores = []
		for enfant in L:
			score = minimax(enfant,max_depth - 1,not(maximize))
			Scores.append(score)
		if (maximize == True):
			return(max(Scores))
		else :
			return(min(Scores))
