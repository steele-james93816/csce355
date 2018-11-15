#!/usr/bin/python3

import sys
from dfa import DFA

def main():


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
		print("The program needs two arguments to run.\nExample: dfaSim.py dfa.txt tests.txt")
	except FileNotFoundError as err:
		#This error occurs if any of the files do not exist
		print("Unable to locate file: {0}".format(str(err).split()[-1]))

	dfa1 = DFA()
	dfa1.setAlpha("12345")
	dfa1.getAlpha()
	dfa1.checkInput(1)

main()
