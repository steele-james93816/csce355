import sys


def main():
    inputfile = open("dfaExample.txt")
    lineCount = 0
    stateNum = 0
    accStates = []
    alphabet = ""
    transitions = []

    for line in inputfile:
        lineCount = lineCount + 1

        if lineCount == 1:
            tmpLine = line.split()
            stateNum = tmpLine[3]
        if lineCount == 2:
            accStates = line.replace("Accepting states:","").split()
        if lineCount == 3:
            alphabet = line.replace("Alphabet:","").strip()
        if lineCount > 3:
            transitions.append(line.split())
    
    dfaSim(stateNum,accStates,alphabet,transitions)

def dfaSim(numStates,accStates,alphabet,transitions):
    numberAlp = len(alphabet)
    numStates = int(numStates)
    transTable = [[0 for x in range(int(numberAlp))] for y in range(int(numStates))]
    alphabetList = list(alphabet)
    currentLocation = 0

    userCheck = list(input("Enter a string to check: "))
    
    for character in userCheck:
        if character not in alphabet:
            print ("string is not in the alphabet")
            sys.exit(2)
        charIndex = alphabetList.index(character)
        
        currentLocation = transitions[int(currentLocation)][int(charIndex)]
    

    '''
        for index in range(numStates):
            print (transitions[index][charIndex])
    '''

    print ("Final state is:",currentLocation)
    if currentLocation not in accStates:
        print ("This string is not accepted")
    else:
        print ("This string is accepted")

main()
