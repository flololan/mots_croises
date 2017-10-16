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
    """
	files_used = file_finder()
	keywords_list = []

	for file in files_used: # Explore each file
		files_data = open(file, encoding="utf8").read() # We put the document in a string variable
		keywords_found_list = keywords_finder(files_data) 
		
		for word in keywords_found_list: # We add keywords to the good list
			word = word[2:-2] # Remove the ** at the start and at the end of the word
			keywords_list.append(word) # Add the word to the keywords_list

	return keywords_list


#------------------------------------------------#
#	  Second part : Find something good !        #
#------------------------------------------------#

def searching_keywords_with_size(size_word, keywords_list):
	good_keywords = []
	for word in keywords_list: # We
		if size_word == len(word): # If the word has the size
			good_keywords.append(word) # We add the word
	return good_keywords

def searching_with_letters(letters, keywords_list):
	keywords_good_size_list = []
	string_to_regular_expressions = r""
	for letter in letters:
		if letter == '-':
			string_to_regular_expressions += r"[/w]"
		else:
			string_to_regular_expressions += letter
	
	string_to_regular_expressions = string_to_regular_expressions
	good_keywords = []

	for word in keywords_list:
		if re.findall(string_to_regular_expressions, word) != None:
			good_keywords.append(word)

	print(good_keywords)
	return good_keywords


#------------------------------------------------#
# Third part : Printing ! Because it's beautiful #
#------------------------------------------------#

def printing(words):
	""" Why should I comment this ? """
	print('############')
	for word in words:
		print('->', word)
	print('############')


#------------------------------------------------#
#	      MAIN (so many lines of code)           #
#------------------------------------------------#
keywords_list = keywords_search()

while "User don't want exit":
	words = searching_keywords_with_size(int(input("Size of the word: ")), keywords_list)
	printing(words)
	exit_statut = input("Exit? (y/n): ")
	if exit_statut == "y":
		break


