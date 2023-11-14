'''
As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.
'''

from lib.grammar_checker import *

# check that function gets the correct first and last character
# check a gramatically correct sentence
# check an incorrect sentence

# def test_grammer_checker():
#     result = grammar_checker("Hello, World!")
#     assert result == "H!"

def test_grammer_checker_correct():
    result = grammar_checker("Hello, World!")
    assert result == True

def test_grammer_checker_incorrect():
    result = grammar_checker("hello, World")
    assert result == False

def test_grammer_checker_partially_incorrect():
    result = grammar_checker("Hello, World")
    assert result == False