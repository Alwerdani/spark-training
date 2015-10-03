def change_word(string, word, temp):
    split = string.split()
    split.insert(temp, split.pop(split.index(word)))
    return ' '.join(split)

string = 'bob likes dogs'
w1 = change_word(string, 'bob', 3)
print(change_word(w1, 'dogs', 0))
