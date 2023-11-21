import re
#from lib.ChallengeEntry import *
# As a user
# So that I can record my experiences
# I want to keep a regular diary

# As a user
# So that I can reflect on my experiences
# I want to read my past diary entries

# As a user
# So that I can reflect on my experiences in my busy day
# I want to select diary entries to read based on how much time I have and my reading speed

# As a user
# So that I can keep track of my tasks
# I want to keep a todo list along with my diary

# As a user
# So that I can keep track of my contacts
# I want to see a list of all of the mobile phone numbers in all my diary entries

#Diary entry class (diary class)
#Implement todo list in diary class
#Functionality:
#A list of diary entries
#be able to add to the list and access the list
#seperate list with Todo items - be able to add to list and access it
#find phone numbers in diary entries and return a list
#return a diary entry with the most appropriate number of words for the users wpm and timeframe

class Diary:
    def __init__(self):
        self.diaryEntry = [] #True option
        self.todoEntry = [] #False option

    def add_entry(self, entry):
        if entry.entry_type() == False:
            self.todoEntry.append(entry)
        else:
            self.diaryEntry.append(entry)
        

    def all(self, option):
        if option == True:
            return self.diaryEntry
        else:
            return self.todoEntry

    def find_numbers(self):
        numbersList = []
        for entry in self.diaryEntry:
            number = str(re.findall(r'[0-9]+', entry.entry)[0])
            if len(number) == 11 and number[0] == "0":
                numbersList.append(number)
        return numbersList

    def reading_best_entry(self, wpm, minutes):
        words = wpm * minutes
        if words <= 0:
            raise Exception("Invalid numbers")
        starting_diff = words
        final_entry = ""
        for entryVal in self.diaryEntry:
            wordCount = len(entryVal.entry.split(" "))
            if wordCount - words >= 0:
                difference = wordCount - words
                if difference < starting_diff:
                    starting_diff = difference
                    final_entry = entryVal
        return final_entry
