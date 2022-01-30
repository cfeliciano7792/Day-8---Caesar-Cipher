alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



def encrypt(plain_text, shift_amount):
  #creates empty string
  shifted_string = ""

  for letter in plain_text:
    #creates an index of item in the list alphabet. Ex a = 0 b = 1 etc
    letter_position = alphabet.index(letter)
    #shifts the letter thats outputted based on user input
    letter_shift = alphabet[letter_position + shift]
    shifted_string += letter_shift
  print(f"The encoded text is {shifted_string}")

def decrypt(cipher_text, shift_amount):
   #creates empty string
  shifted_string = ""

  for letter in cipher_text:
  #creates an index of item in the list alphabet. Ex a = 0 b = 1 etc
    letter_position = alphabet.index(letter)
  #shifts the letter thats outputted based on user input
    letter_shift = alphabet[letter_position - shift]
    shifted_string += letter_shift
  print(f"The decoded text is {shifted_string}")
  
    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list


if direction == "encode":
  encrypt(plain_text = text, shift_amount = shift)
elif direction == "decode":
  decrypt(cipher_text = text, shift_amount = shift)
