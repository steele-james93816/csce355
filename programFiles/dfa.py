class DFA:
	'''
	Initializing the main attributes of the dfa: alphabet, number of states, accepting states, and the transition table
	'''
	alphabet = ""				#alphabet of the dfa
	numStates = 0				#number of states within the dfa
	acceptingStates = []		#list of the accepting states of the dfa
	transitionStates = []		#2 dimensional list of the transitions of the dfa (transition table)

	'''
	Setting the alphabet of the dfa.
	The alphabet is taken in through the main file and parsed using the makeDfa method below.
	Alphabet is a string
	'''
	def getAlpha(self):						#Returns the string that is the alphabet
		return self.alphabet
	def setAlpha(self,alph):					#Sets the alphabet from the DFA file
		self.alphabet = alph

	'''
	Setting the number of states of the dfa.
	The number of states is taken in through the main file and then parsed using the makeDfa method below.
	numStates is an integer.
	'''
	def getNumStates(self):					#Returns the integer that is the number of states
		return self.numStates
	def setNumStates(self,num):				#Sets the number of states from the DFA file
		self.numStates = num

	'''
	Setting the accepting states of the dfa
	The accepting states are received from the dfa file that is taken in through the main program.
	Then it is parsed through and set using the makeDfa method below.
	acceptingStates is a 1 dimensional array.
	'''
	def getAcceptingStates(self):				#Returns the list that is the accepting states of the DFA
		return self.acceptingStates
	def setAcceptingStates(self,accStates):		#Sets the list of accepting states from the DFA file	
		self.accceptingStates = accStates


	'''
	Setting the transition table of the dfa.
	The transition table is received from the dfa file that is taken in through the main program.
	Then it is parsed through and set using the makeDfa method below.
	Transiton table is a 2 dimensional array.
	'''
	def getTransitionStates(self):			#Returns the 2 dimensional array which is the transition table of the DFA
		return self.transitionStates
	def setTransitionStates(self,transStates):	#Sets the 2 dimensional array which is the transition table  of the DFA
		self.transitionStates = transStates

	'''
	Prints the dfa to be desplayed in either a text document or printed in std out
	'''
	def printDfa(self):
		print("Number of states: ", self.numStates)
		print("Accepting states: ", self.acceptingStates)
		print("Alphabet: ", self.alphabet)
		for states in self.transitionStates:
			print(states)


	def makeDfa(self,inputfile):
		lineCount = 0		#Stores a count of the number of lines in the file so that parsing is easier
		stateNum = 0		#Stores the number of states
		accStates = []		#List that stores the accepting states
		alphabet = ""		#String that stores the alphabet for the DFA
		transitions = []	#2 dimensional list that stores the transitions of the DFA

		for line in inputfile:
			lineCount = lineCount + 1

			if lineCount == 1:				#Line in the DFA input file that contains the number of states of the DFA
				tmpLine = line.split()
				stateNum = tmpLine[-1]
			if lineCount == 2:				#Line in the DFA input file that contains the list of accepting states of the DFA
				accStates = line.replace("Accepting states:","").split()
			if lineCount == 3:				#Line in the DFA input file that contains the string of the alphabet the DFA can accept
				alphabet = line.replace("Alphabet: ","").replace("\n","")			
			if lineCount > 3:				#Every other line of the DFA input file will be the transitions table of the DFA
				transitions.append(line.split())

		self.acceptingStates = accStates		#Sets the object's accepting states
		self.alphabet = alphabet				#Sets the object's alphabet
		self.transitionStates = transitions	#Sets the object's transition table
		self.numStates = stateNum			#Sets the object's number of states

