import random
playing = True
number = str(random.randint(10, 20))
print("I will generate a no from 0 to 9 and you have to guess the no one digit at a time")
print("The game ends when you get 1 hero!")
while playing:
    guess = input("Guess the no:")
    if number == guess:
        print("You win the game")
        print("The no was ", number)
        break
    else:
        print("Your guess was wrong, try again. \n")
        