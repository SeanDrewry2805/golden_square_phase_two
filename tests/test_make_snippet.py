from lib.make_snippet import *

def test_make_snippet_longer_than_five():
    result = make_snippet("This might not be a long string")
    assert result == "This might not be a..."

def test_make_snippet_equal_to_five():
    result = make_snippet("This is a long string")
    assert result == "This is a long string"