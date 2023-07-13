# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 12:59:08 2023

@author: pikes
"""

#-------------------------------IMPORT PACKAGES-------------------------------

import tkinter as tk
import numpy as np
import random
import requests
import io
import json

#--------------------------FETCH AND PICK ANSWER WORD-------------------------
"""
A dataset has been created containing all valid English, 5 letter words 
(stored in the csv_url variable). This code allows the dataset to be called in
  without needing to be downloaded onto the users computer. 

From this dataset, it will pull a random word to be the solution to the Wordle
problem. 
"""
csv_url = "https://github.com/pikes-ons/Wordle_Hackathon/blob/main/valid_sol"\
    "utions.csv"

response = requests.get(csv_url)

char = "\r"

if response.status_code == 200:    
    csv_data = io.StringIO(response.content.decode('utf-8'))
    json_contents = csv_data.read()
    data_dict = json.loads(json_contents)
    word_choice = data_dict['payload']['blob']['rawLines']
    word_choice = [ele.replace(char, "") for ele in word_choice]
else:
    print('Unable to get a response.')

answer = ""

def select_random_word(words):
   answer = random.choice(words)
   return answer

correct_word = select_random_word(word_choice)   

#------------------------------ASSIGN VARIABLES-------------------------------
"""
A blank array to be populated by the player's guesses. Each word is on it's 
own row and each letter is in it's own column
"""

letter_board = np.zeros((5,5)) #letter board 

"""
A blank array to be populated by the colours associated with the player's 
guess. This will be used for the background colour when the word is displayed.
"""

colour_board = np.zeros((5,5)) #colour board

"""
Row number to ensure that new guesses and colours are added to a different 
row within each board every time a user submits a new guess. This variable
is updated within the guess_label function.
"""

r = 6

#A blank variable for each new guess from the user to be stored
guessed_word = "" 

#Changes the correct word to upper case to match the user guessed word
correct_word_upper = correct_word.upper()

#Splits correct word into individual letters to allow checks to take place.
correct_word_letter_1 = correct_word_upper[0].upper()
correct_word_letter_2 = correct_word_upper[1].upper()
correct_word_letter_3 = correct_word_upper[2].upper()
correct_word_letter_4 = correct_word_upper[3].upper()
correct_word_letter_5 = correct_word_upper[4].upper()

"""
To resolve an issue of letters being counted twice within the colour check, 
each letter from the guessed word is removed from the correct word (if it is 
present). The correct_word_progress variable stores the correct word 
throughout the colour check process to prevent any permanent changes to the 
answer word.
"""

correct_word_progress = "" 
#---------------------------------FUNCTIONS-----------------------------------
"""
When actioned, get_word will pull the word submitted by a user, populate it in
the guessed_word variable, and check is against the correct word. If the 
guessed word matches the correct word, it will disable the submit button and 
display a congratulatory message underneath the word display. 
"""
def get_word():
    global guessed_word
    submitted_word = text.get()
    guessed_word = submitted_word
    if guessed_word == correct_word:
        sbmt_btn.config(state="disabled")
        tk.Label(window, text = "Congratulations! You solved the word.").grid(
            row = 7, column = 0, columnspan = 6)
    return

"""
colours_board function pulls in the blank colour board, assigns 
correct_word_upper to correct_word_progress and deletes the first row of the 
blank array. 
The function then splits the guessed word into its individual letters and puts
them in upper case to match the correct_word format - otherwise it will not 
match correctly in the check_letter function. The check_letter function is run 
5 times, once for each letter in both words. These results are assigned to 
variables col1 to col5. col1 to col5 are added to create a new row for the 
array, which is then appended to the bottom of the colour_board to prevent it 
being deleted in the next guess. This colour board then replaces the previous 
itteration of the colour board. 
"""

def colours_board():
    global colour_board 
    global guessed_word
    global correct_word_progress 
    correct_word_progress = correct_word_upper
    colour_board_del = np.delete(colour_board, 0, 0) 
    guessed_word_letter_1 = guessed_word[0].upper()
    guessed_word_letter_2 = guessed_word[1].upper()
    guessed_word_letter_3 = guessed_word[2].upper()
    guessed_word_letter_4 = guessed_word[3].upper()
    guessed_word_letter_5 = guessed_word[4].upper()
    col1 = check_letter(guessed_word_letter_1, correct_word_letter_1)
    col2 = check_letter(guessed_word_letter_2, correct_word_letter_2)
    col3 = check_letter(guessed_word_letter_3, correct_word_letter_3)
    col4 = check_letter(guessed_word_letter_4, correct_word_letter_4)
    col5 = check_letter(guessed_word_letter_5, correct_word_letter_5)
    colour_row = [col1, col2, col3, col4, col5]
    colour_board = np.vstack([colour_board_del, colour_row])
    return 

"""
check_letter pulls in the global variable correct_word_progress to compare 
the letters to. It will test if the guessed letter is not in 
correct_word_progress and return the hex code coordinating with white if true.

It will then test if guess_letter matches correct_letter, in which case it 
return the hex code for green. 

Lastly, it will test if guess_letter is in 
correct_word_progress, in which case it will return the hex code for orange. 

This is so if someone guesses a letter with double letters but the correct 
word only has one of those letters, only one letter will have an orange/green
assignment.  
"""

def check_letter(guess_letter, correct_letter):
    global correct_word_progress
    if guess_letter not in correct_word_progress:
        return "#FFFFFF"
    elif guess_letter == correct_letter:
        correct_word_progress = correct_word_progress.replace(guess_letter,
                                                              "_",1)
        return "#77dd77"
    else:
        if guess_letter in correct_word_progress:
            correct_word_progress = correct_word_progress.replace(guess_letter,
                                                                  "_",1)
            return "#ffb347"
    
"""
letters_board function pulls in the blank letter board and guessed_word. It 
deletes the first row and assigns each letter of guessed_word to its own 
variable. These individual letters are added in a list (new_guess) and then 
appended to the bottom of the letter_board. This new version of letter_board
becomes the main version used for the next guess rather than the blank board.
"""

def letters_board():
    global letter_board
    global guessed_word
    letter_board_del = np.delete(letter_board, 0, 0) 
    guessed_word_letter_1 = guessed_word[0].upper()
    guessed_word_letter_2 = guessed_word[1].upper()
    guessed_word_letter_3 = guessed_word[2].upper()
    guessed_word_letter_4 = guessed_word[3].upper()
    guessed_word_letter_5 = guessed_word[4].upper()
    new_guess = [guessed_word_letter_1, guessed_word_letter_2, 
                 guessed_word_letter_3, guessed_word_letter_4, 
                 guessed_word_letter_5] 
    letter_board = np.vstack([letter_board_del, new_guess]) 
    return
    
"""
guess_label function calls the updated letter_board and colour_board 
variables, as well as the row count. Based on the values of these variables, 
it creates individual labels to display in the GUI.
Width and height are set in variables w and h respectively. 
The hex codes from the colour board are used to colour the background of the 
labels displayed on the GUI and the text from the letter_board is displayed
in the labels. 
The row count is updated so that the next set of labels does not display over 
the current one. 
"""    
    
def guess_label():
    w = 5
    h = 3
    global letter_board
    global colour_board
    global r
    tk.Label(window, bg = colour_board[4,0], text=letter_board[4,0], 
             width = w, height = h).grid(row = r, column = 1, padx = 5, 
                                         pady = 10) 
    tk.Label(window, bg = colour_board[4,1], text=letter_board[4,1], 
             width = w, height = h).grid(row = r, column = 2, padx = 5, 
                                         pady = 10) 
    tk.Label(window, bg = colour_board[4,2], text=letter_board[4,2], 
             width = w, height = h).grid(row = r, column = 3, padx = 5, 
                                         pady = 10) 
    tk.Label(window, bg = colour_board[4,3], text=letter_board[4,3], 
             width = w, height = h).grid(row = r, column = 4, padx = 5, 
                                         pady = 10) 
    tk.Label(window, bg = colour_board[4,4], text=letter_board[4,4], 
             width = w, height = h).grid(row = r, column = 5, padx = 5, 
                                         pady = 10) 
    r = r - 1 
    return 

"""
The display() function is run when the submit button is clicked. It runs the 
function get_word(). It then removes the labels showing if the previous entry 
was too long or an invalid word. 

If the row count is 0, it will disable the submit button as this means the 
user has run out of guesses. It will show label_quit and a button that closes
the window. 

The function then tests if this word is the correct length or a valid word. If 
it is then it will run the lettes_board(), colours_board(), and guess_label() 
functions and clear the guess ready for the next attempt.
"""

def display():
    global r
    get_word() 
    label_length.grid_forget() 
    label_valid_word.grid_forget() 
     
    if r == 0 :
        sbmt_btn.config(state="disabled")
        label_quit.grid(row = 7, column = 0, columnspan = 6)
        quitButton.grid(row = 8, column = 0, columnspan = 6)
    elif len(guessed_word) != 5:
        label_length.grid(row = 9, column = 0, columnspan = 6) 
    elif guessed_word.lower() not in lowercase_words: 
        label_valid_word.grid(row = 9, column = 0, columnspan = 6) 
    else:
        letters_board()
        colours_board()
        guess_label()  
        text.delete(0, tk.END) 
    return    

"""
This function only allows users to input letters in the guess box. 
It also prevents a blank word guess.
"""

def validate_input(text):
    if not text.isalpha() and text != '': 
        return False
    return True   

#-------------------------------CODE TO RUN GAME------------------------------

#Creates the GUI window and sets the size
window = tk.Tk()
window.geometry("300x700")

#Creates label if the submitted word is not valid
label_valid_word = tk.Label(window, text = "Invalid word.") 
lowercase_words = np.char.lower(word_choice) 
#Creates label for if the word is more/less than 5 letters
label_length = tk.Label(window, text = "Make sure your word is 5 letters")

#Creates a quit button
quitButton = tk.Button(window, text='Quit', command=window.destroy) 

#Creates label for if the guess count maximum is reached.
label_quit = tk.Label(window, text = "The word was:" + correct_word_upper + 
                      "Press quit and try again")

"""
Creates a widget for users to enter their submitted words. Checks the 
validation so users can only submit letters.
"""

validation = window.register(validate_input) 
text = tk.Entry(window, validate="key", validatecommand=(validation, "%P")) 
text.focus_set()
text.grid(row = 0, column = 0, columnspan = 5, padx = 15, pady = 30)

#Creates a submit button to run the game.
sbmt_btn = tk.Button(window, text = "Submit", command = lambda: display())
sbmt_btn.grid(row = 0, column = 5)  


    
window.mainloop()
