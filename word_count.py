phrase = input("Enter string: ")
word = input("Enter word: ")
word_count = []
count = 0
word_count = phrase.split(" ")
for i in range(0, len(word_count)):
    if word == word_count[i]:
        count += 1
print(f"The word '{word}' appears {count} ")