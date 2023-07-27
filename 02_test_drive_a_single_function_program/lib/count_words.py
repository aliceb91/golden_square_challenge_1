def count_words(string):
    string_array = string.split()
    end_list = []
    for word in string_array:
        if word[0].isalpha() == True:
            end_list.append(word)
    return len(end_list)
