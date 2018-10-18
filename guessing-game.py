def main():
    print("PYTHON GUESSING GAME")
    print(gameLoop())
    
answer = "gorilla"
g = 0
def gameLoop():
    global g
    print("I am thinking of an animal.")
    while g < 5:
        print("What animal am I thinking of?")
        guess = input("\nGuess an animal.").lower().strip()
        g += 1
        if guess == "quit":
            break
        elif guess == answer:
            return "\nCongratulations, you've guessed corrctly!"
        else:
            print("Wow 5 guesses and you still couldn't get it?")
            
main()
