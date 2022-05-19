import helper

guesses = 0
guess = 0
target = helper.target()

while (guess != target):
    
    guess = int(input("Enter a number between 1 and 100: "))
    guesses += 1
    helper.output_message(guess)
    
    if (guess == target):
        print ("It took you",guesses, "tries.\n")
        guess = 0
        guesses = 0
