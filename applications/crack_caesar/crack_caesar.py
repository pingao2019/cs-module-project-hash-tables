

import string
# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
with open("ciphertext.txt") as f:
  text = f.read()
# Your code here
encoded_chars = set(string.ascii_uppercase)
frequencies = {}
letter_count = 0
for char in text:
  if char in encoded_chars:
    # Increment letter_count for finding percentages
    letter_count += 1
    # Set char as key in freq dict; start at 1
    if char not in frequencies:
      frequencies[char] = 1
    # Else, increment count
    else:
      frequencies[char] += 1

# print(letter_count)
# print(frequencies)

# Probably no need to calculate percentages; lining up the rankings an equally valid option
frequency_ranked_letters = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
frequency_tuples = [(letter, frequencies[letter]) for letter in frequencies]
frequency_tuples.sort(key=lambda tup: tup[1], reverse=True)
decoder = {frequency_tuples[i][0]: letter for (i, letter) in enumerate(frequency_ranked_letters)}
# print(decoder)
decoded_text = ''
for char in text:
  if char not in encoded_chars:
    decoded_text += char
  else:
    decoded_char = decoder[char]
    decoded_text += decoded_char

print(decoded_text)