###imports
from stats import get_book_text, get_word_count, get_character_counts, sort_character_counts

def main():#main function that runs the program
    print(f"Found {get_word_count(get_book_text("books/frankenstein.txt"))} total words") #print word count
    sortedCharacterCounts = sort_character_counts(get_character_counts(get_book_text("books/frankenstein.txt"))) #get a sorted list of characters

    #loop through the sorted list and print only alphabetical characters
    for c in sortedCharacterCounts:
        if c["char"].isalpha():
            print(f"{c["char"]}: {c["num"]}")
        else:
            continue
    #end for loop
###end main function

main() #call main()