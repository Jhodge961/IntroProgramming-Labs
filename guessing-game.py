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
            return ("\nCongratulations, you guessed corrctly!")
            question = input("Do you like that animal? yes or no")
            if question == "yes":
                print("Awesome")
            else:
                print("I am sorry you do not like this animal.")
        else:
             print("That is not it try again.")
    print("Wow 5 guesses and you still couldn't get it?")
            
main()
