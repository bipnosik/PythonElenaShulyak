def combine_anagrams(words_array):

    anagram_groups = {}


    for word in words_array:

        key = ''.join(sorted(word.lower()))


        if key not in anagram_groups:
            anagram_groups[key] = []


        anagram_groups[key].append(word)


    return list(anagram_groups.values())

print(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar",
"creams", "scream"]))