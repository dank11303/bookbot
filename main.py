###imports
from stats import get_book_text, get_word_count, get_character_counts

def main():#main function that runs the program
    print(f"Found {get_word_count(get_book_text("books/frankenstein.txt"))} total words")
    characterCounts = get_character_counts(get_book_text("books/frankenstein.txt"))

    for c in characterCounts:
        print(f"{c}: {characterCounts[c]}")

###end main function

main() #call main()