#! /usr/bin/python3
# Name: bulletPointAdder.py
# Description: adds bullet points to start of each line of text on the clipboard

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):         # loop through indexes 
    lines[i] = '* ' + lines[i]      # add star
text = '\n'.join(lines)
pyperclip.copy(text)

