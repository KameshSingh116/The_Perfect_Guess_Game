#Radhe Radhe 
#The perfect guess game.
import random
comp_choice=random.randint(1,10)
print(comp_choice)

def score():
 while(comp_choice==your_guess):
    if(choice=='y'):
        print("Your Final Score Is:")
        if(guess<=10):
         print(f"Score:{11-guess+1}")
        elif(guess>10):
         print("Your score is 0.5")
        break

    elif choice=='n':
        print("Your Final Score Is:")
        if(guess<=10):
         print(f"Score:{11-guess+1}")
        elif(guess>10):
         print("Your score is 0.5")
        break

    else:
        print("Your Final Score Is:")
        if(guess<=10):
         print(f"Score:{11-guess+1}")
        elif(guess>10):
         print("Your score is 0.5")
        


choice='y'
guess=0
while(choice=='y'):
    your_guess=int(input("Enter Your Guess:"))

    if(your_guess==comp_choice and guess==0):
        
        print("That was a great guess!")
        
        print("You made the right guess in the first attempt!")
        
        guess+=1
        
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
        score()
        continue
    
    elif(choice=='n'):
        print("See you soon!")
        score()
        break
    
    else:
        print("Invalid choice!")
        score()
        break










