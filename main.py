from stats import count_words
from stats import frequency
from stats import sorted_frequency
import sys

def main():
  if len(sys.argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  file = sys.argv[1]

  with open(file) as f:
      file_contents = f.read()
      words_number = count_words(file_contents)
      letter_frequency = frequency(file_contents)
      sorted_letters = sorted_frequency(letter_frequency)
      # print(f'{words_number} words found in the document')
      # print(letter_frequency)
      print("============ BOOKBOT ============")
      print(f'Analyzing book found at {file}...')
      print("----------- Word Count ----------")
      print(f'Found {words_number} total words')
      print("--------- Character Count -------")
      for letter in sorted_letters:
        sort_key = ''
        for key in letter:
          sort_key = key
        count = letter[key]
        print(f'{key}: {count}')
      print("============= END ===============")

# file = "books/frankenstein.txt"

main()