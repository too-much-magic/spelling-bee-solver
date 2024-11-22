def main(): 
    import json

    print("""Note that the NYT Spelling Bee uses a shortened dictionary, 
    so some words here may not be valid answers.\n""")
    centre_letter = input("Input the centre letter: ").lower()
    letters = list(input("Input all other letters consecutively, (e.g. MWILDE): ").lower())
    
    with open('words_dictionary.json', 'r') as file:
        valid = json.load(file)
    
    solution = []
    for word in valid:
        has_centre = False
        for letter in word:
            if letter == centre_letter:
                has_centre = True
            elif letter not in letters:
                break
        else:
            if has_centre: solution.append(word)
    
    def is_pangram(word, letters, centre_letter):
        if centre_letter not in word: return False
        for letter in letters:
            if letter not in word: return False
        return True
    
    print("\nValid words:")
    for word in solution:
        if is_pangram(word,letters,centre_letter):
            # converts to bold, then converts back to normal text
            print('\033[1m' + "PANGRAM: ",end="\033[0m")
        print(word)
if __name__ == '__main__':
    main()
