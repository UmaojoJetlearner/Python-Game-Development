import random

secretset=set()

while len(secretset)<5:
    num=random.randint(1,20)
    secretset.add(num)
guessedset=set()
print(" Welcome to guess the scret set game, enjoy! \n Guess the number from 1 through 20") 
while guessedset != secretset:
    guess=int(input("Enter your guess!"))

    if guess in guessedset:
        print("You already guessed this number")
        continue

    if guess in secretset:
        print("Correct guess :)")
        guessedset.add(guess)
    else:
        print("Incorrect guess :(")
    
    print("Your correct guesses so far",guessedset)

print("Congratulations, you have guessed all the numbers!")
print("The secret set was",secretset)