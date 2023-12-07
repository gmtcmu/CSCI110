#guess the number
#game loop
    #genrarte a #
    # input prompt (loop 5)
    #compare #s (if)
    #outupt a hint
#play again?

import random

def num_gen():
    a = random.randrange(0,15)
    return a


def main():
    
    kr = True #keep running
    while (kr == True):
        rn = num_gen() #random nuber   
        for i in range (5):
            ui = int(input("Guess my number...")) #user input
            if rn == ui: #if rn =/><=ui
                print("You're right!")
                break
            elif rn > ui:
                print ("Your number is too low, try again.")
            elif rn < ui:
                print("Your number is too high, try again.")
        ask = input("Do you want to play again? (y/n) ")
        if ask == 'n':
            kr = False #stop loop
            print("Thanks for playing!")
    




if __name__ =="__main__":
    main()