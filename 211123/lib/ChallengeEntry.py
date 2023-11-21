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

class Entry:
    def __init__(self, text):
        self.entry = text

    def entry_type(self):
        if "TODO" in self.entry:
            return False
        else:
            return True
        


