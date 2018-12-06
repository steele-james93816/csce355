#!/usr/bin/python3

import sys
from dfa import DFA

def main():
	dfa1 = DFA()	#This is the initial DFA defined by the exampleDFA.txt
	dfa2 = DFA()	#If this is the intersection it houses the second DFA if there is no second DFA it will go unused
	testString = ""

	'''
	Opening the files and prompting the user if there are any errors.
	'''

	try:
		dfa_filename = sys.argv[1]					#First command line argument that will be the file containing the DFA
		dfa_file = open(dfa_filename,'r')
		if len(sys.argv) != 2:						#If there is no second argument given in the command
			secondFilename = sys.argv[2]				#Second command line argument that will be the filecontaining the test cases
			secondFile = open(secondFilename,'r')
			dfa2.makeDfa(secondFile)					#Creating the dfa from the second file using the dfa class
	except IndexError:
		#This error occurs when one of the command line arguments are missing
		sys.exit("The program needs two arguments to run.\nExample: dfaSim.py dfa.txt tests.txt")
	except FileNotFoundError as err:
		#This error occurs if any of the files do not exist
		sys.exit("Unable to locate file: {0}".format(str(err).split()[-1]))

	dfa1.makeDfa(dfa_file)	#Creating the dfa from the file using the dfa class
	

	if dfa2.transitionStates == []:
		dfa1.acceptingStates = comp(dfa1)
		dfa1.printDfa()

	newTmpTransitionTable = []
	'''
	for i in range(len(dfa1.transitionStates)):
		for j in range(len(dfa1.alphabet) - 1):
			tmpArray = []
			for k in range(len(dfa2.alphabet) - 1):
				tmpArray2 = []
				tmpArray2.append(int(dfa1.transitionStates[i][j]))
				tmpArray2.append(int(dfa2.transitionStates[i][k]))
				tmpArray.append(tmpArray2)
			newTmpTransitionTable.append(tmpArray)
	'''
	'''
				for l in range(len(dfa2.transitionStates)):
					tmpArray2 = []
					tmpArray2.append(int(dfa1.transitionStates[i][j]))
					tmpArray2.append(int(dfa2.transitionStates[k][l]))
					tmpArray.append(tmpArray2)
				newTmpTransitionTable.append(tmpArray)
	'''
	'''
			for k in range(len(dfa1.alphabet) - 1):
				tmpArray2 = []
				tmpArray2.append(int(dfa1.transitionStates[i][j]))
				tmpArray2.append(int(dfa2.transitionStates[i][k]))
				tmpArray.append(tmpArray2)
			newTmpTransitionTable.append(tmpArray)
	'''
	
	newTransitionTable = []
	transitions = []

	for i in range(len(dfa1.transitionStates)):
		for j in range(len(dfa1.transitionStates)):
			transitions.append([i,j])

	for i in range(len(newTmpTransitionTable)):
		tmp = []
		for j in range(len(newTmpTransitionTable[i])):
			tmp.append(transitions.index(newTmpTransitionTable[i][j]))
		newTransitionTable.append(tmp)

	for i in newTransitionTable:
		counter = 0
		for j in i:
			if counter == len(i) - 1:
				print(j, end = "")
			else:
				print(j, end = " ")
			counter = counter + 1
		print()
	
	print(transitions)
	print(len(transitions))
	#print(newTmpTransitionTable)
	#print(newTransitionTable)
def comp(dfa):
	transitions = dfa.getTransitionStates()	
	acceptingStates = dfa.getAcceptingStates()
	newAcceptingStates = []
	tmpArray = []

	counter = 0
	for i in range(len(transitions)):
		tmpArray.append(counter)
		counter = counter + 1

	for i in acceptingStates:
		tmpArray[tmpArray.index(int(i))] = ""

	for i in tmpArray:
		if i != "":
			newAcceptingStates.append(str(i))
	
	return newAcceptingStates

main()
