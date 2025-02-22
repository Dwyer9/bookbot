def count_words(text):
  words = text.split()
  words_number = len(words)
  return words_number

def frequency(text):
  freq = {}
  for i in range(0, len(text)):
    character = text[i].lower()
    if character in freq:
      freq[character]+= 1
    else:
      freq[character] = 1
  return freq

# text = 'testing'
# print(frequency(text))