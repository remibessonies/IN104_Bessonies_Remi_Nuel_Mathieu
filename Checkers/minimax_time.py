import time

def minimax_time(state,T,maximize):
	dictionnaire = {}
	if state in dictionnaire:
		return(dictionnaire[state])
	if (T <= 5e-5) :
		return(state.evaluate())
	L = state.get_children()
	if (L==[]):
		return(state.evaluate())
	else :
		Scores = []
		Tdispo = T
		Temps = []
		compt_enfants = 0
		debut = time.time()
		for enfant in L :
			score = minimax_time(enfant,Tdispo/(len(L)-compt_enfants),not(maximize))
			fin = time.time()
			Treel= fin - debut
			Tdispo = T-Treel
			Scores.append(score)
			Temps.append(Tdispo)
			compt_enfants = compt_enfants + 1

		#print(Temps)	
		if (maximize == True) :
			return(max(Scores))
			dictionnaire[state] = max(Scores)
		else :
			return(min(Scores))
			dictionnaire[state] = min(State)