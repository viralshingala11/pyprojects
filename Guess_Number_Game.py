import random

secret_number = random.randint(1,101)
user = int(input("roll the number: "))
count = 1
game_over = False                      

while not game_over:               #perform below steps this till game does not over

    if user == secret_number:
        print("hurray ! you have won")
        print("counts(time) taken",count)
        game_over = True
        print("Game finished")
        
    else:
        if user > secret_number:
            print("rolled number is greater, so roll smaller than this")
            count += 1
            user = int(input("roll the number again: "))
            
        else:
            print("roll out higher than this")
            count += 1
            user = int(input("roll the number again: ")) 
            





        
        
        
        
       
    


