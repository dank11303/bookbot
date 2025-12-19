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