def get_book_text(filePath): #function that will take contents of a file and return it as a string
#declare variable to store string
    contents = ""

#open the file using the filePath variable
    with open(filePath) as f:
        contents = f.read()

    return contents #return string of book contents
### end get_book_text(str)

def get_word_count(contents): #function to count the number of words in the book
    return len(contents.split()) #return the length of an array of the words from the book
### end get_word_count(str)

def get_character_counts(contents): #function to count the occurrence of each character in the book
    characters = {} #declare empty dictionary

    for c in contents: #for loop to parse each character
        char = c.lower()
        #check if the character is already in the dictionary or not and update or add accordingly
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1

    return characters #return dictionary
###end get_character_coutns(str)

def sort_character_counts(characters): #function to update the characters dictionary to be a list of dictionaries and return that list sorted.
     #declare empty lists
    sortedCharacters = []
    keys = list(characters.keys())

    #loop through the keys list and add key and value pairs to individual dictionaries to be added to the list.
    for k in keys:
        sortedCharacters.append({"char": k, "num": characters[k]})
    
    sortedCharacters.sort(reverse=True, key=sort_on)

    return sortedCharacters #return a sorted list of dictionaries
###end sort_character_coutns(dictionary)

def sort_on(characters): #helper function for sort_character_counts to choose what to sort by
    return characters["num"] #return the key to base the sort on
###end sort_on(dictionary)