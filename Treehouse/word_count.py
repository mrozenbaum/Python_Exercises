string = "I do not like it Sam I Am"

def word_count(string):

    string_list = string.split(" ")
    word_count = {}
    string_lower = []

    for word in string_list:
      string_lower.append(word.lower())

    for word in string_lower:
      word_count[word] = string_lower.count(word)

    print(word_count)

word_count(string)
