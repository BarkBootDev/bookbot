import sys
from stats import count_unique_words  

def main():
    book_local = ""
    if len(sys.argv) < 2:
        book_local = "books/frankenstein.txt"
    else:
        book_local = sys.argv[1]
    count_unique_words(book_local)

if __name__ == "__main__":
    main()
