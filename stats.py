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

def sort_on(dict):
  sort_key = ''
  for key in dict:
    sort_key = key
  # print(dict, sort_key)
  return dict[sort_key]

def sorted_frequency(frequency):
  sorted = []
  for freq in frequency:
    if freq.isalpha():
      dict = {freq: frequency[freq]}
      sorted.append(dict)
  # print(new_list)
  sorted.sort(reverse=True, key=sort_on)
  return sorted

# text = 'testingaaa..'
# freqs = frequency(text)
# print(frequency(text))
# print(sorted_frequency(freqs))
# dict = {'t': 3}
# print(dict[1])

# sorted_letters = sorted_frequency(freqs)
# for letter in sorted_letters:
#   sort_key = ''
#   for key in letter:
#     sort_key = key
#   count = letter[key]
#   print(f'{key}: {count}')