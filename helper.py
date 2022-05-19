import random
# generate and return a random number between 1 and 100
def target():
    global target 
    target = random.randint(1,100)
    return target
    
# format and return the failure and congratulatory messages
def output_message(guess):

        if guess > target:
            print ("Too high, try again.\n")
        
        elif guess < target:
            print ("Too low, try again.\n")

        else:
            print ("\nCongratulations! That is correct.")
