import random

def playersName():
    name = input("Who are you? ")
    helloPlayer(name)

def helloPlayer(name):
    print("Fuck you. Just kidding, welcome " + name)

def locationPoops():
    coords = []
    for i in range(20):
        poop1 = random.randint(0,20)
        poop2 = random.randint(0,20)
        coords.append([poop1,poop2])
        print(coords)
def pickPlanet():
        balls = random.randint(0,7)
        planet = "You are on Planet: " + balls
        
        egg = 1
        poos = 2
        gorl = 3
        cheeks = 4
        girthy = 5
        helpme = 6
        fuck = 7
        if(balls == 1):
            balls = "egg"
        if(balls == 2):
            balls = "poos"
        if(balls == 3):
            balls = "gorl"
        if(balls == 4):
            balls = "cheeks"
        if(balls == 5):
            balls = "girthy"
        if(balls == 6):
            balls = "helpme"
        if(balls == 7):
            balls = "fuck"
        print(planet)
    
    
    

        

playersName()
locationPoops()
pickPlanet()
