'''
varible              purpose 
========================================================
sentence       -     holds the user input 
sentenceLength -     holds the length of the sentence
'''

sentence = input('Enter a sentence and i\'ll return how many charictor were entered: ')     #ask user for input
sentenceLength = len(sentence)      #calculate sentence length
print('\"' + sentence + '\"',"has",sentenceLength, "characters in it.")     #print message with length

