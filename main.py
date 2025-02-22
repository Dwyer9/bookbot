from stats import count_words
from stats import frequency

def main():
  with open("books/frankenstein.txt") as f:
      file_contents = f.read()
      words_number = count_words(file_contents)
      letter_frequency = frequency(file_contents)
      print(f'{words_number} words found in the document')
      print(letter_frequency)

main()