
# Full Name: Kevin T Le

# Student ID: 2406054

# Chapman Email: kevle@chapman.edu

# Course Number and Section: CPSC 230-07

# In Class Programming Assignment 6: Exercise #1

# Purpose: This program asks the user to enter a text file.
# All punctuation is removed.
# The number of occurences of each unique word will be recorded
# and written to a seperate text file called "counts.txt"

import operator

def read_file(txt_file): # This function opens and reads an inputted text file.
                         # It also checks if the file is in the same directory.
    while True:
        try: # Opens and reads the text file
            open_txt_file = open(txt_file, 'r')
            read_txt_file = open_txt_file.readlines()
            break
        except: # If text file not in same directory, prompts user to enter another text file.
            txt_file = input("Unable to open file. Please try another file: ")

    return read_txt_file # Returns the read text file as a list of words

def build_dictionary(read_txt_file): # This function creates a dictionary of words
                                     # and the number of times they occur within
                                     # a text file
    word_count_dictionary = {} # Dictionary of unique words with the number of occurrences

    punctuation_removed = [] # List of sentences after punctuation removed (spaces stay)

    for sentence in read_txt_file:
        clean_sentence = "" # Each character that is a letter, number, or space will be put into a sentence
                            # These sentences will be individual elements in "punctuation_removed"

        sentence = sentence.replace("\n","") # Removes newline character
        for char in sentence:
            if char.isalpha() == True: # Letters will be included after filtering
                char = char.lower()
                clean_sentence += char
            elif char.isdigit() == True: # Numbers will be included after filtering
                clean_sentence += char
            elif char.isspace() == True: # Spaces will be included after filtering
                clean_sentence += char
            else:
                continue # Skips if not letter, number, or space.

        punctuation_removed.append(clean_sentence) # Each resulting sentence will be appended to "punctuation_removed"

    word_list = [] # List of word elements after splitting sentences in "punctuation_removed"

    for sentence in punctuation_removed:
        word_list += sentence.split(" ") # Splits sentences into smaller word elements using space as the divider

    for word in word_list:
        if word in list(word_count_dictionary.keys()): # If the word is a key in the "word_count_dictionary"
            word_count = word_count_dictionary[word] # "word_count" is assigned to its respective word
            word_count += 1
            word_count_dictionary[word] = word_count # Number of occurrence value is updated

        else:
            word_count_dictionary[word] = 1 # Key is added into dictionary with starting value of "1"


    return word_count_dictionary

def write_file(word_count_dictionary, txt_file): # This function sorts the dictionary in descending order
                                                 # and outputs into seperate text file

    sort_txt_file = sorted(word_count_dictionary.items(), key=operator.itemgetter(1)) # Sorts dictionary in ascending order
    sort_txt_file.reverse() # Changes to descending order
    sort_txt_file.pop(1) # Empty element in dictionary is removed

    open_txt_file = open(txt_file, 'w')
    for element in sort_txt_file: # Formats the output text file
        write_txt_file = open_txt_file.write("{}: {} times\n\n".format(element[0], element[1]))


# Start of Program

file_name = input("Enter your file name: ") #Prompts user to enter file name

write_file( build_dictionary( read_file(file_name) ), "counts.txt" ) #Filters inputted text file with above functions and outputs into "counts.txt"
