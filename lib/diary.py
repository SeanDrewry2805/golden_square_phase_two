from lib.DiaryEntry import *

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

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        list = [i.format() for i in self.entries]
        text = '\n\n'.join(list)
        print(text)
        return text

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        word_count = 0
        for i in self.entries:
            # print(i.count_words())
            word_count += i.count_words()
        return word_count

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        reading_time_in_minutes = 0
        for i in self.entries:
            reading_time_in_minutes += i.reading_time(wpm)
        
        return f"Estimated reading time: {reading_time_in_minutes} minutes"

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
        '''
        calculate how many words can be read in the time
        sort entries by word count exlcuding any the are over
        return highest word count entry still in list
        '''
        words_to_read = wpm * minutes
        list = [entry for entry in self.entries if entry.count_words() < words_to_read]
        sorted_list = sorted(list, key= lambda i: i.count_words(), reverse=True)
        text = sorted_list[0].format()
        print(text)
        return text