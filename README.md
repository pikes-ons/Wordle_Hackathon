# Wordle_Hackathon

## Table of Contents
1. [Project Statement](https://github.com/pikes-ons/Wordle_Hackathon/edit/main/README.md#description)
2. [Description](#description)
3. [Technologies](#technologies)
4. [Dependencies](#dependencies)
5. [Installation](#installation)
6. [Usage](#usage)
7. [Contributors](#contributors)
8. [Collaboration](#collaboration)
9. [FAQs](#faqs)
   
## Project Statement
Python code to run a Wordle-style game.

## Description
Wordle Hackathon is a project developed by the Bits and Bytes team as part of the Coffee and Coding: Coding Best Practices Hackathon that allows users to play a Wordle-style game. When the code is run, a tkinter window will pop up on the users' screen. Users can type in a valid, English, 5 letter word and press submit. The GUI will then output the word submitted by the user in a colour coordinated fashion. For more information on how to run the game, please see section 6: Usage.

## Technologies
This project is programmed using Python Version 3.10.12. 

## Dependencies
All packages used in the code are inbuilt into Python. These packages are:
   - tkinter
   - numpy
   - random
   - requests
   - io
   - json
  
## Installation
1. Download the python file called Wordle.py
2. Open in your python application of choice (e.g. Spyder)
3. Run the code

## Usage
1. Launch the game by running Wordle.py
2. The game will display a user interface where you can guess English five letter words.
3. After making a guess, the game will provide feedback in the form of coloured indicators:
   Green: The letter is in the word and in the correct place.
   Orange: The letter is in the word but in the incorrect place.
   White: The letter is not in the word at all.
4. Keep guessing until you guess the correct word or you run out of attempts. You have 6 attempts to guess the correct word.
   
## Contributors

Thanks to the following people who have contributed to this project:
* Sophie Pike: @pikes-ons
* Robbie Nicoll: @nicolr-ons
* Elias Kellow: @kelloe-ons
* Hannah Howard: @hannahhowardons

## Collaboration
This project does not currently accept contributions.

## FAQs
1. What do the colours mean?
   Green: The letter is in the word and in the correct place.
   Orange: The letter is in the word but in the incorrect place.
   White: The letter is not in the word at all.

2. How many guesses do we have?
   You have 6 guesses. If you don't get the word within these guesses, a button will pop up that you can click to close the game.
   
3. How do we run the code?
   First, download the Wordle.py file and open in your Python programme of choice (e.g. Spyder). Then run by clicking the green play button on the tool bar. The code will create a pop up window where you can play the game.
   
4. How do we try again?
   If you run out of guesses, you can close the game and restart the code. This will generate a different random word for you to guess so, even if you get the correct answer, you can play as many times as you like. 
