"""
FR :) 

Bon c'est pas très propre pour l'instant mais ça fonctionne !
J'essaye de commenter au maximum. J'ai une idée d'amélioration mais on verra plus tard :)

Notions utilisées:
--> Import de bibliothèques et leur utilisation :)
--> Boucle for, if ...
--> Fonctions
--> Listes 
Je crois que c'est tout 
"""

import re # Library with regular expressions
from os import listdir # List the files 

#------------------------------------------------#
#	First part of the programm : Find keywords ! #
#------------------------------------------------#
def file_finder():
	""" Find the file of the class, typically tag_[topic].ipynb """
	file_in_directory = listdir('.') # List all files
	file_with_answer = []

	for file in file_in_directory:
		if re.match(r"tag(.)*", file) != None: # When a tag*** file is found
			file_with_answer.append(file)
	return file_with_answer


def keywords_finder(file):
	""" Find the keywords in the 'file' argument with regular expression"""
	keywords_list =  re.findall(r"\*\*[\w]+\*\*", file) # Understand pattern : **word**
	return keywords_list
	

def keywords_search():
	""" 
	Main function of the first part : 
	Find the keywords
	This function call other functions (file_finder and keywords_finder)
    """
	files_used = file_finder()
	keywords_list = [] # Create the list named keywords_list

	for file in files_used: # Explore each file
		files_data = open(file).read() # Put the data of the document in a string variable
		keywords_found_list = keywords_finder(files_data) 
		
		for word in keywords_found_list: # Add keywords to the good list
			word = word[2:-2] # Remove the ** at the start and at the end of the word
			keywords_list.append(word) # Add the word to the keywords_list

	return keywords_list


#------------------------------------------------#
#	  Second part : Find something good !        #
#------------------------------------------------#

def searching_keywords_with_size(size_word, keywords_list):
	keywords_good_size_list = [] # Create the list named keywords_good_size_list
	for word in keywords_list:
		if size_word == len(word): # If the word has the size
			keywords_good_size_list.append(word) # We add the word
	return keywords_good_size_list


#------------------------------------------------#
# Third part : Printing ! Because it's beautiful #
#------------------------------------------------#

def printing(words):
	""" This is a useless docstring """
	for word in words:
		print(word)

#------------------------------------------------#
#	      MAIN (so many lines of code :p )       #
#------------------------------------------------#
keywords_list = keywords_search()

words = searching_keywords_with_size(int(input("Size of the word: ")), keywords_list)

printing(words)