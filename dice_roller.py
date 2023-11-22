import random

response = input("Press y to roll and n to exit : ")

while response == "y":
    
    no = random.randint(1,6)
    print(no)
    response = input("Press y to roll and n to exit : ")
