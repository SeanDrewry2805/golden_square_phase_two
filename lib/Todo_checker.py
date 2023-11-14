"""
As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.
"""

#Taking an argument that will be a string 
#check if the string contains the tag "#TODO"
#return true or false

def todo_checker(string):
    tag = "#TODO"
    if tag in string:
        return True
    else:
        return False