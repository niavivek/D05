#!/usr/bin/env python3
# HW05_ex09_01.py

# Write a program that reads words.txt and prints only the
# words with more than 20 characters (not counting whitespace).
##############################################################################
# Imports
"""Program to read a text file and print words with more than 20 characters"""
# Body
def read_words(file_name):
	file_to_read = open(file_name) #open the file
	all_words = file_to_read.read() #read the file
	list_of_words = all_words.split() # split the words into a list

	for words in list_of_words: #iterate list
		if len(words) > 20: # print if length is more than 20
			print(words)

##############################################################################
def main():
    read_words("words.txt")  # Call your functions here.

if __name__ == '__main__':
    main()
