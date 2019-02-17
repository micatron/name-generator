#Random name generator
import random

print('Number of characters: ') #get number of characters
charsMax = input()
print('How many names: ') #number of names to generate
qnames = input()

#load character library - consonant table, vowel table, maybe more?

#Until charsMax is reached, generate new names
names = 0
while names < qnames:
    namesToOutput[names] = nameGen(cTab, vTab, charsMax)

#print name
for i in range(qnames):
    print(namesToOutput[i]
