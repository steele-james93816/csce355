#!/usr/bin/python3

import sys
from dfa import DFA

def main():
	dfa1 = DFA()	#This is the initial DFA defined by the exampleDFA.txt
	testString = ""

	'''
	Opening the files and prompting the user if there are any errors.
	'''

	try:
		dfa_filename = sys.argv[1]	#command line argument that will be the filecontaining the test cases
		dfa_file = open(dfa_filename,'r')
	except IndexError:
		#This error occurs when one of the command line arguments are missing
		sys.exit("The program needs two arguments to run.\nExample: dfaSim.py dfa.txt tests.txt")
	except FileNotFoundError as err:
		#This error occurs if any of the files do not exist
		sys.exit("Unable to locate file: {0}".format(str(err).split()[-1]))

	dfa1.makeDfa(dfa_file)	#Creating the dfa from the file using the dfa class

	#dfa1.printDfa()

	#print (testInf(dfa1,'0',[],False,[False,False]))

	tmpAnswer = testInf(dfa1,'0',[False,False])


	if tmpAnswer[0] == True and tmpAnswer[1] == True:
		print ("nonempty infinite")
	if tmpAnswer[0] == True and tmpAnswer[1] == False:
		print ("nonempty finite")
	if tmpAnswer[0] == False and tmpAnswer[1] == True:
		print ("empty infinite")
	if tmpAnswer[0] == False and tmpAnswer[1] == False:
		print ("empty finite")


def testHelper(dfa,curState,termState,visStates,paths,pathindex):
	transitions = dfa.getTransitionStates()
	finals = dfa.getAcceptingStates()
	visitedStates = visStates
	
	visitedStates[int(curState)] = True;
	paths.append(curState);
	pathindex = pathindex + 1

	if int(curState) == int(termState):
		print (paths)
	else:
		for i in transitions[int(curState)]:
			if i not in visitedStates:
				testHelper(dfa,i,termState,visitedStates,paths,pathindex)

	pathindex = pathindex - 1
	visitedStates[int(curState)] = False;
	
	return "empty"

def testInf(dfa,currLoc,finalAnswer):
	transitions = dfa.getTransitionStates()
	finals = dfa.getAcceptingStates()
	alphLen = len(dfa.getAlpha())
	visitedStates = []
	pathindex = 0
	paths = []

	for i in range(len(transitions)):
		visitedStates.append(False)

	for i in finals:
		testHelper(dfa,0,i,visitedStates,paths,pathindex)

	return finalAnswer	
	
	'''
	for j in range(len(transitions[currentLocation])):
		print (visitedStates)
		destination = transitions[currentLocation][j]
		print ("Current State: ", currentLocation , " -> Destination: " ,destination)

		if str(currentLocation) in finals:
			finalAnswer[0] = True
		
		if destination not in visitedStates:
			visitedStates.append(str(destination))
			testInf(dfa,int(destination),visitedStates,finalAnswer)
		if destination in visitedStates:
			visitedStates.append(str(currentLocation))
			visitedStates = (visitedStates[0:visitedStates.index(str(destination))])
			currentLocation = int(visitedStates[-2])
		if j == 2:
			visitedStates = (visitedStates[0])

			print ("looped")
			print ("Looped States" , visitedStates[(visitedStates.index(str(destination)))::])
			print ("Nonlooped States" , visitedStates[0:visitedStates.index(str(destination))])
print ("Visited States: ", visitedStates)


else:
			visitedStates = (visitedStates[0:visitedStates.index(str(currentLocation))])

testInf(dfa,int(destination),visitedStates,madeloop,finalAnswer)
		print (currentLocation , " going to " , destination)
		if destination not in visitedStates:
			visitedStates.append(str(currentLocation))
			if str(currentLocation) in finals:
				finalAnswer[0] = True
			testInf(dfa,int(destination),visitedStates,madeloop,finalAnswer)
		else:
			#print ("loop")
			print (visitedStates)
			loopedStates = visitedStates[(visitedStates.index(str(destination)))::]
			if visitedStates.index(str(destination)) != 0:
				print ("Looped States" , visitedStates[(visitedStates.index(str(destination)))::])
				print ("Nonlooped States" , visitedStates[0:visitedStates.index(str(destination))])
				visitedStates = visitedStates[0:visitedStates.index(str(destination)) + 1]
			for i in range(len(loopedStates)):
				if loopedStates[i] in finals:
					finalAnswer[1] = True
		visitedStates = visitedStates[0:len(visitedStates) - 1]
	'''

main()
