import sys
from dfa import DFA

def invHom():
	dfa1 = DFA()			#This is the initial DFA defined by the exampleDFA.txt
	inputAlphabet = ""
	outputAlphabet = ""
	testStrings = []
	lineCount = 0
	

	'''
	Opening the files and prompting the user if there are any errors.
	'''

	try:
		dfa_filename = sys.argv[1]	#First command line argument that will be the file containing the DFA
		testFilename = sys.argv[2]	#Second command line argument that will be the filecontaining the test cases
		dfa_file = open(dfa_filename,'r')
		testFile = open(testFilename,'r')
	except IndexError:
		#This error occurs when one of the command line arguments are missing
		sys.exit("The program needs two arguments to run.\nExample: dfaSim.py dfa.txt tests.txt")
	except FileNotFoundError as err:
		#This error occurs if any of the files do not exist
		sys.exit("Unable to locate file: {0}".format(str(err).split()[-1]))

	dfa1.makeDfa(dfa_file)	#Creating the dfa from the file using the dfa class

	#dfa1.printDfa()

	for line in testFile:
			lineCount = lineCount + 1

			if lineCount == 1:
				inputAlphabet = line.replace("Input alphabet: ","").replace("\n","")
			if lineCount == 2:
				outputAlphabet = line.replace("Output alphabet: ","").replace("\n","")		
			if lineCount > 2:
				testStrings.append(line.replace("\n",""))
	
	answer = [[0 for i in range(len(testStrings))] for j in range(int(dfa1.getNumStates()))]

	countStrings = 0
	for string in testStrings:
		for j in range(int(dfa1.getNumStates())):
			#print(countStrings, ":", j)
			answer[j][countStrings] = findFinal(dfa1,string,j)
		#print (countStrings)
		countStrings = countStrings + 1
	
	print("Number of states:",dfa1.getNumStates())
	
	tmpStr = ""
	numCount = 0
	for i in dfa1.getAcceptingStates():
		tmpStr = tmpStr + i
		if numCount != len(dfa1.getAcceptingStates()) - 1:
			tmpStr = tmpStr + " "
		numCount = numCount + 1
	print("Accepting states:",tmpStr)
	print("Alphabet:",inputAlphabet)
	for i in answer:
		counter = 0
		for j in i:
			if counter == len(i) - 1:
				print(j, end = "")
			else:
				print(j, end = " ")
			counter = counter + 1
		print()

def findFinal(dfa,testString,startingState):		
	numberAlphabet = len(dfa.getAlpha())
	alphabetList = list(dfa.getAlpha())
	transitions = dfa.getTransitionStates()
	currentLocation = startingState

	if len(testString) == 0 and (str(startingState) in dfa.getAcceptingStates()):
		return startingState

	for character in list(testString):
		if character not in list(dfa.getAlpha()):
			return False
		charIndex = alphabetList.index(character)

		currentLocation = transitions[int(currentLocation)][int(charIndex)]

	return currentLocation

invHom()
