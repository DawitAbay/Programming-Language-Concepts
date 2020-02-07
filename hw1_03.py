import string
SPL_CHAR = string.punctuation
f = open("hw1_03.txt", "r")
for line in f.readlines():
    word=""
    line = line.rstrip()
    for word_count in line:
        if word_count not in SPL_CHAR and word_count != " ":
            word = word + word_count
        else:
            if word_count == " ":
                print(word)
                word=""
            else:
                print(word)
                print(word_count)
                word=""
print(word)
