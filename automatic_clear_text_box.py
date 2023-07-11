# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 12:59:08 2023

@author: pikes
"""

#----------------------------------------Import packages----------------------------------------
import pandas as pd
import tkinter as tk
import numpy as np
import random
#----------------------------------------Assign Variables----------------------------------------
import requests
import io
import json

csv_url = "https://github.com/pikes-ons/Wordle_Hackathon/blob/main/valid_solutions.csv"
# download into memory into memory and not file system
response = requests.get(csv_url)

if response.status_code == 200:    
    csv_data = io.StringIO(response.content.decode('utf-8'))
    json_contents = csv_data.read()
    data_dict = json.loads(json_contents)
    
    word_choice = data_dict['payload']['blob']['rawBlob'].split('\r\n')[1:-1]
else:
    print('unable to get a response.')
    
lb = np.zeros((5,5)) #letter board 
cb = np.zeros((5,5)) #colour board

random_word = ""

def select_random_word(words):
   random_word = random.choice(words)
   return random_word

word = select_random_word(word_choice)

print(word)

#row placements for guess display labels in window
r = 6
sw = "" #Storage for guessed word

#Change format of correct word to upper case
word_selection2 = word.upper()

#Split correct word into individual letters
wl1 = word_selection2[0].upper()
wl2 = word_selection2[1].upper()
wl3 = word_selection2[2].upper()
wl4 = word_selection2[3].upper()
wl5 = word_selection2[4].upper()

#----------------------------------------Functions----------------------------------------

def get_word():
    global sw
    submitted_word = text.get()
    sw = submitted_word
    if sw == word:
        sbmt_btn.config(state="disabled")
        tk.Label(window, text = "Congratulations! You solved the word.").grid(row = 7, column = 0, columnspan = 6)
    return

#Update colours board
def colours_board():
    global cb #to update the colour board variable outside of the function
    global sw
    colour_board_del = np.delete(cb, 0, 0) #deletes first row in array
    sl1 = sw[0].upper()
    sl2 = sw[1].upper()
    sl3 = sw[2].upper()
    sl4 = sw[3].upper()
    sl5 = sw[4].upper()
    col1 = check_letter(sl1, wl1)
    col2 = check_letter(sl2, wl2)
    col3 = check_letter(sl3, wl3)
    col4 = check_letter(sl4, wl4)
    col5 = check_letter(sl5, wl5)
    colour_row = [col1, col2, col3, col4, col5]
    cb = np.vstack([colour_board_del, colour_row])
    return 

#Compare single letter of word guess with corresponding letter of correct word to populate colour board with correct colours
def check_letter(sl, wl):
    if sl not in word_selection2:
        return "#FFFFFF"
    elif sl == wl:
        return "#77dd77"
    else:
        return "#ffb347"
    
    
#Update letters board
def letters_board():
    global lb
    global sw
    letter_board_del = np.delete(lb, 0, 0) #deletes first row in array
    sl1 = sw[0].upper()
    sl2 = sw[1].upper()
    sl3 = sw[2].upper()
    sl4 = sw[3].upper()
    sl5 = sw[4].upper()
    new_guess = [sl1, sl2, sl3, sl4, sl5] #creates new array row 
    lb = np.vstack([letter_board_del, new_guess]) #makes relevant changes to variables
    return
    
    
def guess_label():
    w = 5
    h = 3
    global lb
    global cb
    global r
    tk.Label(window, bg = cb[4,0], text=lb[4,0], width = w, height = h).grid(row = r, column = 1, padx = 5, pady = 10) #text for first letter
    tk.Label(window, bg = cb[4,1], text=lb[4,1], width = w, height = h).grid(row = r, column = 2, padx = 5, pady = 10) #text for second letter
    tk.Label(window, bg = cb[4,2], text=lb[4,2], width = w, height = h).grid(row = r, column = 3, padx = 5, pady = 10) #text for third letter
    tk.Label(window, bg = cb[4,3], text=lb[4,3], width = w, height = h).grid(row = r, column = 4, padx = 5, pady = 10) #text for fourth letter
    tk.Label(window, bg = cb[4,4], text=lb[4,4], width = w, height = h).grid(row = r, column = 5, padx = 5, pady = 10) #text for fifth letter
    r = r - 1 #updates row count
    return 

def display():
    global r
    #global label
    
    get_word() # new
    
    label_length.grid_forget() # new (remove label on new attempt)
    label_valid_word.grid_forget() # new (remove label on new attempt)
     
    if r == 0 :
        sbmt_btn.config(state="disabled")
        label_quit.grid(row = 7, column = 0, columnspan = 6)
        quitButton.grid(row = 8, column = 0, columnspan = 6)
    elif len(sw) != 5:
        label_length.grid(row = 9, column = 0, columnspan = 6) # new (show incorrect length)
    elif sw.lower() not in lowercase_words: # new (check valid input)
        label_valid_word.grid(row = 9, column = 0, columnspan = 6) # new (show user put invalid word)
    else:
        letters_board()
        colours_board()
        guess_label()
        text.delete(0, tk.END) # new
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
label_valid_word = tk.Label(window, text = "invalid word!") # new (show user put invalid word) used in display function
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