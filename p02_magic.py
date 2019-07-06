import random
count = 0
play = True
game = True
name = input("Hello, What is your name?\n>> ")
while play:
    num = random.randint(1, 88)
    guess = input(f"Well {name}, try to guess the number I have in mind!\n>> ")
    try:
        if guess.isdigit():
            guess1 = int(guess)
            if guess1 != num:
                if guess1 > 88:
                    print("Invalid number, USAGE: 1-88, try again!")
                    count = count + 1
                elif guess1 > num:
                    print("Too high, try again!")
                    count = count + 1
                else:
                    print("Too low, try again!")
                    count = count + 1
            else:
                print(f"It took you {count} turns to guess my number which was {num}!")
                while game:
                    ask = input("Do you want to play again? [Y/N]\n>> ")
                    if ask.upper() == "Y":
                        play = True
                        break
                    elif ask.upper() == "N":
                        print(f"Ok, bye {name}! See you later!")
                        play = False
                        break
                    else:
                        print("Sorry, I did not understand. Let me repeat:")
                        again = True
        else:
            print("Sorry, I did not understand. Let me repeat:")
            again = True
    except ValueError:
        print("Sorry, I did not understand. Let me repeat:")









