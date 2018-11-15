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

	dfa1.makeDfa(dfa_file)

	for line in testFile:
		line = line.replace("\n","")
		if acceptReject(dfa1,line):
			print("accepted")
		else:
			print("not accepted")

def acceptReject(dfa,testString):
	numberAlphabet = len(dfa.getAlpha())
	alphabetList = list(dfa.getAlpha())
	transitions = dfa.getTransitionStates()
	currentLocation = 0

	print("\n",testString)
	for character in list(testString):
		if character not in list(dfa.getAlpha()):
			return False
		charIndex = alphabetList.index(character)
		currentLocation = transitions[int(currentLocation)][int(charIndex)]

	if currentLocation not in dfa.getAcceptingStates():
		return False
	else:
		return True
main()
