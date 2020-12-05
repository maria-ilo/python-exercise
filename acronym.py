def main():
    phrase = input("Enter the phrase: ")

    # split the phrase into substrings
    phrase_split = phrase.split()
    acronym = ""

    # iterate through every substring
    for i in phrase_split:
        acronym += i[0].upper()

    print(f"The acronym for {phrase} is {acronym}")


main()
