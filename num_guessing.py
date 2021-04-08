# Number Guessing
import random
dice_side=random.randint(1,9)
num=int(input("Rolls a 9-sided dice.Which number do you think it will be?"))
while num != dice_side:
    print("well, your answer is incorrect.Here is a new hint for you, if the right side is multiplied by a multiple of 2 the answer is "+str( dice_side*2))    
    num=int(input("new guess"))
if num==dice_side:
    print("congrats!!Your guess is correct.")
    

