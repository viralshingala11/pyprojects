import random
a = ["stone", "paper", "scissor"]
secret_weapon = a[random.randint(0,2)]
count = 1
user = False

while user == False:
    user = input("enter any weapon: ")
    if user == secret_weapon:
        print("TIE")
    elif user == "stone":
        if secret_weapon == "paper":
            print("You LOSE")
        else:
            count += 1
            print("You WIN")
            
    elif user == "paper":
        if secret_weapon == "scissor":
            print("You LOSE")
        else:
            count += 1
            print("You WIN")
            
    elif user == "scissor":
        if secret_weapon == "stone":
            print("You LOSE")
        else:
            count += 1
            print("You WIN")
    else:
        print("enter is invalid")
    user = True
    secret_weapon = a[random.randint(0,2)]



