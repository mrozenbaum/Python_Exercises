nums = range(10)
small_numbers = [num for num in nums if num < 6]
# Only add numbers to the new list if the value is less than 6

words = ['big', 'red', 'dog', 'ate', 'his', 'food']
three_letters_words = [ word.title() for word in words if len(word) == 3 ]
#.title() will capatalize the first letters of the word
# len(stringVariable) is equivalent to stringVariable.length in JavaScript


####### --------------- #######


# Using a set comprehension, create a new set that contains all songs that were not performed by Nickelback.

nickelback_songs = {}
songs = {
    ('Nickelback', 'How You Remind Me'),
    ('Will.i.am', 'That Power'),
    ('Miles Davis', 'Stella by Starlight'),
    ('Nickelback', 'Animals')
}

songz = {song[1] for song in songs if song[0] != 'Nickelback'}
print(songz)
