def main():
    inputfile = open('./dfaExamples/example1.txt')
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
            alphabet = line.replace("Alphabet:","")
        if lineCount > 3:
            transitions.append(line.split())

    print ("The number of states is:",stateNum,"\n")
    print ("The accepting states are:",accStates,"\n")
    print ("The alphabet is:",alphabet,"\n")
    print ("The transitions are:",transitions,"\n")
    
main()
