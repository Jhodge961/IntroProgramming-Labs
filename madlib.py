#MadLib Program

def madLib():
    global noun, verb, adjective, place
    noun = input ("Enter a noun: ")
    verb = input ("Enter a verb: ")
    adjective = input ("Enter a an adjective: ")
    place = input ("Enter a place: ")

def makeAndPrintSentence():
    print ("In the " + place + "we saw a " + adjective + noun + verb + "!")

def main():
    madLib()
    makeAndPrintSentence()
    
main()
