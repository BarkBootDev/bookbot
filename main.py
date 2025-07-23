import sys
from stats import book_report 

def main():
    book_local = ""
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_report(sys.argv[1])

if __name__ == "__main__":
    main()
