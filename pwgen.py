
import random
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9','!', '#', '$', '%', '&', '(', ')', '*', '+','^','?']

def pw_generator():
  results = []
  for char in range(1,nr_letters+1):
    random_char = random.choice(characters)
    results += random_char

  random.shuffle(results)
  password = ""
  for char in results:
    password += char
  print()
  print(f"Your password is: {password}")



print("Random Password Generator!")
nr_letters= int(input("How many characters would you like in your password?\n>> ")) 

pw_generator()
