from lib.count_words import *

def test_count_words():
    result = count_words("hello, world! How are you?")
    assert result == 5

def test_count_words_six():
    result = count_words("What are you doing this weekend?")
    assert result == 6