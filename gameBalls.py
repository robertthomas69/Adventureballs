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
        print("The coordinates of your poop is ")
        print(poop1, poop2)
        
def doYouEnjoyPoop():
    enjoyPoo = input("Do you like to drop dookies on land? ")
    answerBack(enjoyPoo)
    
def answerBack(enjoyPoo):
    
    if(enjoyPoo == "yes"):
        print("I see you answered yes, you are a ceritified turd.")

def pickPlanet():
    picky = int(input("Pick a number 1-7: "))
    planetName = random.randint(0,7)
    balls = "Not on a planet"
    if(planetName == 1):
        balls = "egg"
    if(planetName == 2):
        balls = "poos"
    if(planetName == 3):
        balls = "gorl"
    if(planetName == 4):
        balls = "cheeks"
    if(planetName == 5):
        balls = "girthy"
    if(planetName == 6):
        balls = "helpme"
    if(planetName == 7):
        balls = "Fuck"
    print"You are on planet: "
    print(balls)


              
playersName()
locationPoops()
doYouEnjoyPoop()

pickPlanet()
