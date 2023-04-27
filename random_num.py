#1. write a program to guess the random number
import random
scrt_num = random.randint(0,20)

for i in range(5):
    num = int(input("Enter the number: "))
    if num < 0 and num >= 20:
        print("Try the number within ")
    if num == scrt_num:
        print("You guessed it right, it is {}",scrt_num)
        break
    elif num > scrt_num:
        print("Guess smaller number")
    elif num < scrt_num:
        print("Guess Bigger number")
    if i == 5:
        print("Game over")