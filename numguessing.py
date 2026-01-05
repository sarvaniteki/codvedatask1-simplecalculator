import random
max_att=7
secrete_num=random.randint(1,100)
attemps=0
print("Welocome to the number guessing game...")
print("i have selected a num between 1 and 100.")
print(f"you have {max_att} attempts to guess it.\n")
while attemps<max_att:
    guess=int(input("enter any number..."))
    attemps += 1
    if guess < secrete_num:
        print("Your guess is low")
    elif guess > secrete_num:
        print("your guess is high")
    else:
        print(f"Congratulations! you guess the number in {attemps}")
        break
else:
    print(f" Game over the secrete number is {secrete_num}.")
