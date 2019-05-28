from collections import defaultdict
from collections import Counter

def count_characters(string):
    count_dictionary = {}
    for c in string:
        if c in count_dictionary:
            count_dictionary[c] += 1
        else:
            count_dictionary[c] = 1
    print(count_dictionary)

count_characters("Dynasty")

def count_characters_collection(string):
    count_dictionary = defaultdict(int)
    for c in string:
        count_dictionary[c] += 1

    print(count_dictionary)

count_characters_collection("Dynasty")

print(Counter("Dynasty"))
