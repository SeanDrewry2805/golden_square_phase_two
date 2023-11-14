def make_snippet(string):
    list = string.split(' ')

    if len(list) > 5:
        new_list = list[:5]
        new_string = ' '.join(new_list)
        return new_string + '...'
    else:
        return(string)