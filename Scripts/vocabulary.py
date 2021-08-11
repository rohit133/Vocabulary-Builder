from enum import Flag
from random_word import RandomWords
from PyDictionary import PyDictionary

# initilizing the Variables

dictionary=PyDictionary()
r = RandomWords()

# Get a Random Word 

def get_word():
    word = r.get_random_word()
    return word

# Get The Meaning

def get_meaning():
    valid_word = False
    while(not valid_word):
        word = get_word() 
        if(dictionary.meaning(word, disable_errors =True)):         
            defs = dictionary.meaning(word)
            for key,value in defs.items():
                meaning = str(key)+" : "+str(value).strip("[]\'\"").replace("\'","")
            valid_word = True 

    return meaning
get_meaning()