import random

def playersName():
    name = input("Who are you? ")
    helloPlayer(name)

def helloPlayer(name):
    print("Fuck you. Just kidding, welcome " + name)

def locationPoops():
    for i in range(20):
        poop1 = random.randint(0,20)
        poop2 = random.randint(0,20)
        
        print("The coordinates of your poop is: (" + poop1 + "," + poop2)
        

playersName()
locationPoops()
