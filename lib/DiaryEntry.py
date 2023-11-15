import math

class DiaryEntry:

    already_read = ''

    def __init__(self, title, contents):
        # Parameters:
        #   title: string
        #   contents: string
        self.title = title
        self.contents = contents
        self.already_read = 0

    def format(self):
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        return f"{self.title}: {self.contents}"

    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry
        list = self.contents.split(' ')
        return len(list)

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        text = self.format()
        list = text.split(' ')
        length = len(list)
        time = round(length/wpm, 2)
        rounded_time = math.ceil(time * 100) / 100
        formatted_time = f'{rounded_time:.2f}'
        return f'Estimated reading time: {formatted_time} minutes'

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
    
        text = self.format()
        list = text.split(' ')
        word_length = len(list)
        words_to_read = math.floor(wpm * minutes)

        if self.already_read == 0:
            text = list[self.already_read:words_to_read]
            format_text = ' '.join(text)
            self.already_read = words_to_read
            if self.already_read >= word_length:
                self.already_read = 0
            print(format_text)
            return format_text
        else:
            text = list[self.already_read:words_to_read]
            format_text = ' '.join(text)
            self.already_read += words_to_read
            if self.already_read >= word_length:
                self.already_read = 0
            print(format_text)
            return format_text