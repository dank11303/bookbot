###imports
from stats import get_book_text, get_word_count

def main():#main function that runs the program
    print(f"Found {get_word_count(get_book_text("books/frankenstein.txt"))} total words")

###end main function

main() #call main()