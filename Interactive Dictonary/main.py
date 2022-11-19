import json # This is used to load a .json file
from difflib import get_close_matches # This is used to match if the input word have any resemblence to the word in the file

data = json.load(open('data.json')) # Loading the data of .json file into the data variable

# Function to take an input from user and return it's discription
def translate(word):
    if(word in data):
        return data[word]
    elif(get_close_matches(word, data.keys())[0]):
        print("Did you mean '%s'?" %  get_close_matches(word, data.keys())[0])
        reply = input("Enter y(Yes) and n(No): ")
        if(reply == 'y'):
            return data[get_close_matches(word, data.keys())[0]]
        else:
            return "Word doesn't exist, please enter a valid word!!"
    else:
        return "Word doesn't exist, please enter a valid word!!"



word = input("Enter a word: ")
output = translate(word.lower())

if(type(output) == list):
    for item in output:
        print(item)
else:
    print(output)