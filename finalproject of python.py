# Import random for generating a secret number
import random

# Import qrcode for making QR codes
import qrcode
from PIL import Image

def play_game():
  print("🎉 Welcome to 'Guess the Number' 🎉")
  print("I'm thinking of a number between 1 and 100.")

  
# Show welcome message
  print("Welcome to the Guessing Game!")
  print("I picked a number between 1 and 100.")

# Random number between 1 and 100
number = random.randint(1, 100)

# Counter for how many tries the player makes
tries = 0

# Loop until player guesses correctly
while True:
     guess = input("👉 Insert your number for result: ")

# Check if input is a number (not text)
     if not guess.isdigit():
       print("⚠️ Please enter a number!\n")
       continue # ask again
     
# Convert input to integer
     guess = int(guess)

# Count this as an attempt
     tries += 1

# Check if guess is lower, higher or correct
     if guess < number:
        print("📉 Too low! Try again.\n")
     elif guess > number:
        print("📈 Too high! Try again.\n")
     else:
        print(f"✅ Correct! The number was {number}.")
        print(f"🎯 You guessed it in {tries} tries.\n")
        break # exit loop when guessed
     
def make_qr():
    # Put your hosted game link here (Replit, PythonAnywhere, etc.)
    link = "https://YourUsername.pythonanywhere.com/"

    # Make QR code with the link
    img = qrcode.make(link)
    img.save("guess_game_qr.png") 

    # Display the QR code
    img.show()
    print("haha QR code displayed in your image viewer!")
    img.save("guess_game_qr.png")# Save to current directory

    # Message for user
    print("QR code saved as 'game_qr.png'.")
    print(" Scan it to play online on iOS or Android.")

    # ---------------------- MAIN PROGRAM ---------------------- 
    if __name__ == "__main__":
       play_game() # Start the game
make_qr() # Create QR code
   