#Random name generator
import random

def loadTable(letterType, characterTable):
    #get specified csv and make a list
    return(characterList)

def nameGen(consonants, vowels, characters):
    startType = random.randint(0, 1)
    #start consonant or vowel depending on startType
    #alternate appending letters until characters is reached
    return(aRandomName)
    

print('Number of characters: ') #get number of characters
charsMax = int(input())
print('How many names: ') #number of names to generate
qnames = int(input())

#load character library - consonant table, vowel table, maybe more?
    #try loading table only once and splitting into cTab and vTab in main, speed?
cTab = loadTable(c, tabName)
vTab = loadTable(v, tabName)

#Until qnames is reached, generate new names
for namesToOutput in range(qnames + 1):
    namesToOutput = nameGen(cTab, vTab, charsMax)

#print name list
for i in namesToOutput:
    print(i)
