import random
import string

print("Welcome to the password generator\n")
total_characters = int(input("Enter the total number of characters in the password:  "))
total_numbers = int(input("Enter the number of numbers in the password:  "))
total_symbols = int(input("Enter the total symbols in the password: "))
total_letters = int(input("Enter the total letters in the password: "))
sum = total_numbers + total_letters + total_symbols

if total_characters != sum:
  print("The total number of the password is incorrect!")
  
else:

  generated_password = (
    random.choices(string.ascii_letters, k =total_characters)+
    random.choices(string.digits , k=total_numbers)+
    random.choices(string.punctuation, k=total_symbols)
  )
  random.shuffle(generated_password)
  password = "".join(generated_password)
  print(f"Your generated_password is: {password} ")
