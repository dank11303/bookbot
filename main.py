###imports
from stats import get_book_text, get_word_count, get_character_counts, sort_character_counts
import sys


def main():#main function that runs the program
    #check if sys.argv has 2 entries
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(get_book_text(sys.argv[1]))} total words") #print word count
    print("--------- Character Count -------")
    
    sortedCharacterCounts = sort_character_counts(get_character_counts(get_book_text(sys.argv[1]))) #get a sorted list of characters

    #loop through the sorted list and print only alphabetical characters
    for c in sortedCharacterCounts:
        if c["char"].isalpha():
            print(f"{c["char"]}: {c["num"]}")
        else:
            continue
    #end for loop
###end main function

main() #call main()