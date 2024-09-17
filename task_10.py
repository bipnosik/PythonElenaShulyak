import re

def count_words(string):

    string = string.lower()


    string = re.sub(r'[^a-z\s]', '', string)


    word_counts = {}
    for word in string.split():
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts

print(count_words("A man, a plan, a canal -- Panama"))


print(count_words("Doo bee doo bee doo"))

