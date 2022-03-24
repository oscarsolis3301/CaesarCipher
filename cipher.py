'''

Today's Date:
March 23rd, 2022

'''


# The starting off alphabet where the checker gets the words from
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Takes in whether we are encrypting or decoding
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# Takes in the message from the user
text = input("Type your message:\n").lower()
# Shifts the word left or right (depending on whether we are encrypting or decoding) 
shift = int(input("Type the shift number:\n"))

# Encrypts the given word
def encrypt(text, shift):
  shifted_word = []
  # checks every letter in the word
  for letters in text:
    shifted_alphabet = alphabet.index(letters)
    # Shifts the word to the right the given amount
    shifted_word += alphabet[shifted_alphabet + shift]
# Prints the encoded word with no spaces
  print("The encoded text is " + ''.join(shifted_word))


# Decrypts the word that the user inputs
def decrypt(text, shift):
  shifted_word = []
  for letters in text:
    shifted_alphabet = alphabet.index(letters)
    # Shifts the word to the left the given amount
    shifted_word += alphabet[shifted_alphabet - shift]
# Prints the decoded word with no spaces
  print("The decoded text is " + ''.join(shifted_word))
  
# Depending on whether the user would like to encode or decode, the appropriate function is run
if direction == 'encode':
    # Encrypts the given word, the given amount
  encrypt(text, shift)
elif direction == 'decode':
    # Decrypts the given word, the given amount
  decrypt(text, shift)

  # End of program