#Programmer: Timothy Pickering
#Date: 2/27/2025
#Title: 100 Dice pair average

#Required library
import random

#Logic to generate 2 numbers between 1 and 6
def randDice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)

#Sum 2 die rolls and return
    return die1 + die2

#Mainline program
if __name__ == "__main__":
#Initalize total
    total = 0

#Roll the dice 100 times
    for count in range(100):
        roll = randDice()
        total = total+roll

#Calculate the average rounded to 2 decimal places
    average = total / 100
    rounded_average = round(average, 2)

#Print the rounded average
    print(f"Average of 100 dice rolls: {rounded_average}")
