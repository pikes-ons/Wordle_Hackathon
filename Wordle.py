# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 12:59:08 2023

@author: pikes
"""

#----------------------------------------Import packages----------------------------------------

import tkinter as tk
import numpy as np
import random
import requests
import io
import json

#----------------------------------------Assign Variables----------------------------------------

csv_url = "https://github.com/pikes-ons/Wordle_Hackathon/blob/main/valid_solutions.csv"
# download into memory and not file system
response = requests.get(csv_url)

if response.status_code == 200:    
    csv_data = io.StringIO(response.content.decode('utf-8'))
    json_contents = csv_data.read()
    data_dict = json.loads(json_contents)
    
    word_choice = data_dict['payload']['blob']['rawBlob'].split('\r\n')[1:-1]
else:
    print('Unable to get a response.')
    
letter_board = np.zeros((5,5)) #letter board 
colour_board = np.zeros((5,5)) #colour board

answer = ""

def select_random_word(words):
   answer = random.choice(words)
   return answer

correct_word = select_random_word(word_choice)

#row placements for guess display labels in window
r = 6
guessed_word = "" #Storage for guessed word
correct_word_progress = "" #storage for correct word minus guessed letters to solve double letter problem

#Change format of correct word to upper case
correct_word_upper = correct_word.upper()

#Split correct word into individual letters
correct_word_letter_1 = correct_word_upper[0].upper()
correct_word_letter_2 = correct_word_upper[1].upper()
correct_word_letter_3 = correct_word_upper[2].upper()
correct_word_letter_4 = correct_word_upper[3].upper()
correct_word_letter_5 = correct_word_upper[4].upper()

#----------------------------------------Functions----------------------------------------

def get_word():
    global guessed_word
    submitted_word = text.get()
    guessed_word = submitted_word
    if guessed_word == correct_word:
        sbmt_btn.config(state="disabled")
        tk.Label(window, text = "Congratulations! You solved the word.").grid(row = 7, column = 0, columnspan = 6)
    return

#Update colours board
def colours_board():
    global colour_board #to update the colour board variable outside of the function
    global guessed_word
    global correct_word_progress 
    correct_word_progress = correct_word_upper
    colour_board_del = np.delete(colour_board, 0, 0) #deletes first row in array
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

#Compare single letter of word guess with corresponding letter of correct word to populate colour board 
#with correct colours
#Added adjustments for double letter calculation
def check_letter(guess_letter, correct_letter):
    global correct_word_progress
    if guess_letter not in correct_word_progress:
        return "#FFFFFF"
    elif guess_letter == correct_letter:
        correct_word_progress = correct_word_progress.replace(guess_letter,"_",1)
        return "#77dd77"
    else:
        if guess_letter in correct_word_progress:
            correct_word_progress = correct_word_progress.replace(guess_letter,"_",1)
            return "#ffb347"
    
#Update letters board
def letters_board():
    global letter_board
    global guessed_word
    letter_board_del = np.delete(letter_board, 0, 0) #deletes first row in array
    guessed_word_letter_1 = guessed_word[0].upper()
    guessed_word_letter_2 = guessed_word[1].upper()
    guessed_word_letter_3 = guessed_word[2].upper()
    guessed_word_letter_4 = guessed_word[3].upper()
    guessed_word_letter_5 = guessed_word[4].upper()
    new_guess = [guessed_word_letter_1, guessed_word_letter_2, guessed_word_letter_3, guessed_word_letter_4, guessed_word_letter_5] #creates new array row 
    letter_board = np.vstack([letter_board_del, new_guess]) #makes relevant changes to variables
    return
    
    
def guess_label():
    w = 5
    h = 3
    global letter_board
    global colour_board
    global r
    tk.Label(window, bg = colour_board[4,0], text=letter_board[4,0], width = w, height = h).grid(row = r, column = 1, padx = 5, pady = 10) #text for first letter
    tk.Label(window, bg = colour_board[4,1], text=letter_board[4,1], width = w, height = h).grid(row = r, column = 2, padx = 5, pady = 10) #text for second letter
    tk.Label(window, bg = colour_board[4,2], text=letter_board[4,2], width = w, height = h).grid(row = r, column = 3, padx = 5, pady = 10) #text for third letter
    tk.Label(window, bg = colour_board[4,3], text=letter_board[4,3], width = w, height = h).grid(row = r, column = 4, padx = 5, pady = 10) #text for fourth letter
    tk.Label(window, bg = colour_board[4,4], text=letter_board[4,4], width = w, height = h).grid(row = r, column = 5, padx = 5, pady = 10) #text for fifth letter
    r = r - 1 #updates row count
    return 

def display():
    global r
    #global label
    
    get_word() # new
    
    label_length.grid_forget() # new (remove label `label_length` on new attempt)
    label_valid_word.grid_forget() # new (remove label `label_valid_word` on new attempt)
     
    if r == 0 :
        sbmt_btn.config(state="disabled")
        label_quit.grid(row = 7, column = 0, columnspan = 6)
        quitButton.grid(row = 8, column = 0, columnspan = 6)
    elif len(guessed_word) != 5:
        label_length.grid(row = 9, column = 0, columnspan = 6) # new (show incorrect length)
    elif guessed_word.lower() not in lowercase_words: # new (check valid input)
        label_valid_word.grid(row = 9, column = 0, columnspan = 6) # new (show user put invalid word)
    else:
        letters_board()
        colours_board()
        guess_label()  
    return    

def validate_input(text):
    if not text.isalpha() and text != '': # new only allow letter and to delete the first character
        return False
    return True   
#-------------------------------------------Code to run game-------------------------------------------------  

#Create GUI window and size
window = tk.Tk()
window.geometry("300x700")

# create widgets to check user put valid word
label_valid_word = tk.Label(window, text = "Invalid word.") # new (show user put invalid word) used in display function
lowercase_words = np.char.lower(word_choice) # new (check valid input)

label_length = tk.Label(window, text = "Make sure your word is 5 letters")

# create widgets to quit after 6 valid attempts
quitButton = tk.Button(window, text='Quit', command=window.destroy) # create new function to destroy current window and reopen it
label_quit = tk.Label(window, text = "Press quit and try again")
#User to submit word

validation = window.register(validate_input) # new (allow only letters)
text = tk.Entry(window, validate="key", validatecommand=(validation, "%P")) # new (allow only letters)
text.focus_set()
text.grid(row = 0, column = 0, columnspan = 5, padx = 15, pady = 30)

sbmt_btn = tk.Button(window, text = "Submit", command = lambda: display())
sbmt_btn.grid(row = 0, column = 5)  


    
window.mainloop()
