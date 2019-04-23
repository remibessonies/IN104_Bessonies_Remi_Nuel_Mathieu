import time

def minimax_time(state,T,maximize):
	dictionnaire = {}

	if T <= 2.5e-5 :
		return(state.evaluate())
	if state in dictionnaire:
		return(dictionnaire[state])
	if (max_depth==0) or (state.get_children()==[]):
		return(state.evaluate())

	else :
		L = state.get_children()
		Scores = []
		Tdispo = T
		compt_enfants = 0
		for enfant in L :
			debut = time.time()
			score = minimax(enfant,Tdispo/(len(L)-compt_enfants),not(maximize))
			fin = time.time()
			Treel= fin - debut
			Tdispo = Tdispo-Treel
			
			Scores.append(score)
			compt_enfants = compt_enfants + 1


		if (maximize == True) :
			return(max(Scores))
			dictionnaire[state] = max(Scores)
		else :
			return(min(Scores))
			dictionnaire[state] = min(State)