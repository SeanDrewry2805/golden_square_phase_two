# File: tests/test_vowel_remover.py

from lib.vowel_remove import *

def test_simple():
    remover = VowelRemover("ab")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == "b"

def test_long_sentence_with_punctuation():
    remover = VowelRemover("We will remove the vowels from this sentence.")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == "W wll rmv th vwls frm ths sntnc."

def test_only_vowels():
    remover = VowelRemover("aEiou")
    result = remover.remove_vowels()
    assert result == ""