from lib.DiaryEntry import  *

one_hundred_words = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras vitae nulla sed neque laoreet faucibus pretium vel augue. Aliquam porttitor velit nisi, a sodales purus mollis ac. Aenean feugiat venenatis fringilla. Sed quis facilisis dui. In hac habitasse platea dictumst. Curabitur id arcu nibh. Quisque a massa magna. Aliquam pulvinar semper enim sit amet pretium. Sed vitae libero nisl. Donec egestas iaculis lorem, id ullamcorper ipsum volutpat nec. Suspendisse potenti. Nam maximus porta rutrum. Curabitur ultrices eleifend nisi sit amet feugiat. Sed porta congue pulvinar. Curabitur congue diam urna. Donec eget felis a mauris efficitur mollis eget eget ipsum. Integer.'
two_hundred_thirtty_seven_words = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis at finibus metus. Nulla aliquam hendrerit diam ut suscipit. Praesent porta eros vel risus ornare tincidunt. Aliquam id justo id enim mattis viverra. Mauris in ullamcorper nibh, semper pellentesque sem. Pellentesque sit amet nibh dui. Nam fringilla, ante id commodo ultrices, augue lacus tempus enim, quis elementum justo purus in quam. Maecenas gravida velit posuere magna bibendum, vitae porta nulla fermentum. Vestibulum ante ipsum, tempor ac semper eget, laoreet quis ligula. Donec tristique vestibulum est, vitae sodales ligula aliquet sed. Nunc vitae imperdiet purus. Nulla elit mi, fringilla vel porttitor ac, commodo vitae enim. Pellentesque ac pretium nisl. Sed pretium facilisis ligula, eget egestas odio finibus sit amet. Cras venenatis varius aliquet. Morbi mollis scelerisque tincidunt. Maecenas sit amet convallis nulla. Cras feugiat mollis magna vel fermentum. Proin scelerisque lectus dui, id tristique diam sodales id. Integer diam eros, feugiat eu neque ut, malesuada tempor nulla. Pellentesque a ullamcorper leo. Maecenas sapien leo, egestas ac lobortis nec, volutpat et ipsum. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras mollis iaculis neque sit amet convallis. Aenean ultricies efficitur libero in tempor. Donec quis purus elit. Morbi a mollis ipsum, a faucibus nulla. In auctor libero luctus tellus aliquam, a tristique lacus scelerisque. Morbi tincidunt mauris dui. Aenean mattis convallis ligula id fermentum. Morbi efficitur augue at ligula rutrum, nec congue tellus hendrerit. Morbi et.'


def test_title():
    # when an entry is made with a title make sure the title is reflected in title attribute
    entry = DiaryEntry('My first entry', 'Today I am writing my first diary entry!')
    assert entry.title == 'My first entry'

def test_contents():
    # when contents are passed, make sure they are reflected in the contents attriute
    entry = DiaryEntry('My first entry', 'Today I am writing my first diary entry!')
    assert entry.contents == 'Today I am writing my first diary entry!'

def test_format():
    # when format() is called a string is returned in the correct format
    entry = DiaryEntry('My first entry', 'Today I am writing my first diary entry!')
    assert entry.format() == 'My first entry:\nToday I am writing my first diary entry!'

def test_count_words_equal_to_eight():
    # make sure count_words() returns the correct nuber of words in the diary rentry
    entry = DiaryEntry('My first entry', 'Today I am writing my first diary entry!')
    assert entry.count_words() == 11

def test_count_words_equal_to_twenty_five():
    # make sure count_words() returns the correct nuber of words in the diary rentry
    entry = DiaryEntry('My first entry', 'Today I am writing my first diary entry! I rode a bus this morning and got all my groceries for dinner, we are having Lasagna.')
    assert entry.count_words() == 28

def test_reading_time_200():
    # when given a wpm this method outputs a reading time estimate for the contents with minutes rounded to 2 dp
    entry = DiaryEntry('My first entry', 'Today I am writing my first diary entry! I rode a bus this morning and got all my groceries for dinner, we are having Lasagna.')
    assert entry.reading_time(200) == 0.15

def test_reading_time_267():
    # when given a wpm this method outputs a reading time estimate for the contents with minutes rounded to 2 dp
    entry = DiaryEntry('My first entry', 'Today I am writing my first diary entry! I rode a bus this morning and got all my groceries for dinner, we are having Lasagna.')
    assert entry.reading_time(267) == 0.10

def test_reading_time_184():
    # when given a wpm this method outputs a reading time estimate for the contents with minutes rounded to 2 dp
    entry = DiaryEntry('My first entry', 'Today I am writing my first diary entry! I rode a bus this morning and got all my groceries for dinner, we are having Lasagna.')
    assert entry.reading_time(183) == 0.15

def test_reading_chunk():
    # when called with wpm and minutes reading_chunk() will return the amount of contents readable in that time
    entry = DiaryEntry('My first entry', one_hundred_words)
    assert entry.reading_chunk(200, 0.2) == 'My first entry:\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Cras vitae nulla sed neque laoreet faucibus pretium vel augue. Aliquam porttitor velit nisi, a sodales purus mollis ac. Aenean feugiat venenatis fringilla. Sed quis facilisis dui. In hac habitasse'

def test_contents_read_stored():
    # after reading_chunk() is called, store the amount read in an attribute
    entry = DiaryEntry('My first entry', one_hundred_words)
    entry.reading_chunk(200, 0.2)
    assert entry.already_read == 40

def test_reading_chunk_repeat():
    # when called again for the same contents reading_chunk() will return the next section of contents not yet read
    entry = DiaryEntry('My first entry', one_hundred_words)
    entry.reading_chunk(200, 0.2)
    assert entry.reading_chunk(200, 2) == 'platea dictumst. Curabitur id arcu nibh. Quisque a massa magna. Aliquam pulvinar semper enim sit amet pretium. Sed vitae libero nisl. Donec egestas iaculis lorem, id ullamcorper ipsum volutpat nec. Suspendisse potenti. Nam maximus porta rutrum. Curabitur ultrices eleifend nisi sit amet feugiat. Sed porta congue pulvinar. Curabitur congue diam urna. Donec eget felis a mauris efficitur mollis eget eget ipsum. Integer.'

def test_reading_chunk_return_to_start():
    # when called again for the same contents reading_chunk() when the contents have already been read, return contents from the start 
    entry = DiaryEntry('My first entry', one_hundred_words)
    entry.reading_chunk(200, 0.2)
    entry.reading_chunk(200, 2)
    assert entry.reading_chunk(200, 0.2) == 'My first entry:\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Cras vitae nulla sed neque laoreet faucibus pretium vel augue. Aliquam porttitor velit nisi, a sodales purus mollis ac. Aenean feugiat venenatis fringilla. Sed quis facilisis dui. In hac habitasse'