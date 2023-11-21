# File: lib/diary.py
from lib.DiaryEntry import DiaryEntry
import math

class Diary:
    def __init__(self):
        self.entries = []

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        self.entries.append(entry)
        pass

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        print(self.entries)
        return self.entries

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        counter = 0
        for listItem in self.entries:
            counter += listItem.count_words()
        return counter


    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        return math.ceil(self.count_words()/wpm)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.

        words = wpm * minutes
        best_difference = words
        best_entry = ""
        for listItem in self.entries:
            if listItem.count_words() - words >= 0:
                difference = listItem.count_words() - words
                if difference < best_difference:
                    best_entry = listItem
                    best_difference = difference
        return best_entry