'''
As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.
'''

# take in a sentence as an argument
# check first and last character of the string
# check the first is a capital letter
# check the last is a sentence ending punctuation mark
# return True/False comment

def grammar_checker(text):
    first_char = text[0]
    last_char = text[-1]
    punctuation = ['.', '?', '!']

    if first_char.upper() == first_char and last_char in punctuation:
        return True
    else:
        return False