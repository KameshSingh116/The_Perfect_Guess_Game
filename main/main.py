#Radhe Radhe 
#The perfect guess game.
import random
comp_choice=random.randint(1,10)

choice='y'
guess=0
while(choice=='y'):
    your_guess=int(input("Enter Your Guess:"))

    if(your_guess==comp_choice and guess==0):
        print("That was a great guess!")
        print("You made the right guess in the first attempt!")
        guess+=1
        break
    elif(your_guess==comp_choice and guess!=0):
        if(guess>=1 and guess<3):
            print(f"Thats was good you took {guess} guesses to guess the right number...")
        elif(guess>3 and guess<10):
            print(f"Not bad !, it took {guess} guesses for you to guess the right number.")
        else:
            print("You exceeded 10 guesses!, you gotta concentrate more!!")

    guess+=1
    
    choice=input("Try again/ No:(y/n):")
    if(choice=='y'):
        continue
    elif(choice=='n'):
        print("See you soon!")
        break
    else:
        print("Invalid choice!")

