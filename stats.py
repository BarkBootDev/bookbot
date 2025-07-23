# bookbot/stats.py
def get_book_text(book_param):
    with open(book_param) as f:
        file_content = f.read()
        print(file_content)

def get_num_words(book_param):
    with open(book_param) as f:
        file_content = f.read()
        book_content = file_content.split()
        print(f"{len(book_content)} words found in the document")

def count_unique_letters(book_param):
    with open(book_param) as f:
        file_content = f.read()
        book_content = file_content.split()
        unique_letters = {}
        for word in book_content:
            for letter in word:
                unique_letters[letter.lower()] = unique_letters.get(letter.lower(), 0) + 1
        sorted_letters_list = sorted(unique_letters.items())
        for letter, count in sorted_letters_list:
            print(f"{letter}: {count}")

def count_unique_words(book_param):
    with open(book_param) as f:
        file_content = f.read()
        book_content = file_content.split()
        unique_letters = {}
        for word in book_content:
            for letter in word:
                unique_letters[letter.lower()] = unique_letters.get(letter.lower(), 0) + 1
        print(unique_letters)

def book_report(book_param):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_param}...")
    print("----------- Word Count ----------")
    print(f"Found {len(open(book_param).read().split())} total words")
    print("--------- Character Count -------")
    count_unique_letters(book_param)
    print("============= END ===============")