"""
Word Occurrences Prac 05
Estimated time:15 minutes
Actual:21 minutes
"""


word_count = {}
text = input("Text: ")
strings = text.split()
for word in strings:
    occurrences = word_count.get(word, 0)
    word_count[word] = occurrences + 1
strings = list(word_count.keys())
strings.sort()

max_length = max((len(word) for word in strings))
for word in strings:
    print(f"{word:{max_length}} : {word_count[word]}")
