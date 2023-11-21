import math
# File: lib/diary_entry.py

class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        self.title = title
        self.contents = contents
        self.list = [self.title, self.contents]
        pass

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
        return len(self.contents.split(" "))

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        return math.ceil(self.count_words()/wpm)

    def reading_chunk(self, wpm, minutes):
        self.count = 0
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        count_list = self.contents.split()
        number_of_words_read =  wpm * minutes
        words_read = []
        words_read = count_list[0 + self.count:number_of_words_read + self.count]
        self.count += number_of_words_read
        return " ".join(words_read)