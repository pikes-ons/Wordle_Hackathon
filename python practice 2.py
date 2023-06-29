# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 12:59:08 2023

@author: pikes
"""

#----------------------------------------Import packages----------------------------------------
import pandas as pd
import tkinter as tk
import numpy as np

#----------------------------------------Assign Variables----------------------------------------
words = pd.read_csv("C:/Users/pikes/Downloads/valid_solutions.csv", names = ["WORD"])
lb = np.zeros((5,5)) #letter board 
cb = np.zeros((5,5)) #colour board
word = "hello"
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
    r = r - 1
    return 

def display():
    global r
    get_word()
    letters_board()
    colours_board()
    guess_label()  
    return    
    
#-------------------------------------------Code to run game-------------------------------------------------  

#Create GUI window and size
window = tk.Tk()
window.geometry("350x500")

#User to submit word
text = tk.Entry(window)
text.focus_set()
text.grid(row = 0, column = 0, columnspan = 5, padx = 15, pady = 30)

sbmt_btn = tk.Button(window, text = "Submit", command = lambda: display()).grid(row = 0, column = 5)  


    
window.mainloop()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    