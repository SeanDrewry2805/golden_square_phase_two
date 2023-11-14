"""
As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.
"""

#take in a parameter with text
#figure out the length of the text in words
#compare amount of words to timeframe
#return a estimate time for reading the text

def estimate_time(string):
    words = 200
    list = string.split(" ")
    length = len(list)
    result = length/words
    return f"It would take you {result} minutes to read this text"