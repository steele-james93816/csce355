class DFA:
	alphabet = ""
	numStates = 0
	acceptingStates = []
	transitionStates = []

	def getAlpha(self):
		return self.alphabet
	def setAlpha(self,alph):
		self.alphabet = alph

	def getNumStates(self):
		return self.numStates
	def setNumStates(self,num):
		self.numStates = num

	def getAcceptingStates(self):
		return self.acceptingStates
	def setAcceptingStates(self,accStates):
		self.accceptingStates = accStates

	def getTransitionStates(self):
		return self.transitionStates
	def setTransitionStates(self,transStates):
		self.transitionStates = transStates

	def printDfa(self):
		print("Number of states: ", self.numStates, "\nAccepting states: ", self.acceptingStates, "\nAlphabet: ", self.alphabet)
		for states in self.transitionStates:
			print(states)


	def makeDfa(self,inputfile):
		lineCount = 0
		stateNum = 0
		accStates = []
		alphabet = ""
		transitions = []

		for line in inputfile:
			lineCount = lineCount + 1

			if lineCount == 1:
				tmpLine = line.split()
				stateNum = tmpLine[-1]
			if lineCount == 2:
				accStates = line.replace("Accepting states:","").split()
			if lineCount == 3:
				alphabet = line.replace("Alphabet:","").strip()
			if lineCount > 3:
				transitions.append(line.split())

		self.acceptingStates = accStates
		self.alphabet = alphabet
		self.transitionStates = transitions
		self.numStates = stateNum

