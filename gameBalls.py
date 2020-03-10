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
    planetName = int(input("Pick a number 1-7: "))
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
    print("You are on planet: ")
    print(balls)

def dentonWhitesideIsSuchApussy():
    dentonsCoochie = int(input("On a scale of 1-10, how gay is BIG D??"))
    biglankyFuck = "DENTON WHITESIDE "                     
    dentonsOneNut = "It is inexistent, why would God ever give Denton two testicles."
    if(dentonsCoochie == 1):
        biglankyFuck = "Give me the drugs you are on, like right now"
    if(dentonsCoochie == 2):
        biglankyFuck = "GO BACK TO DESOTO HAWGG, #dentonbegayashell"
    if(dentonsCoochie == 3):
        biglankyFuck = "You and Denton prolly hatch eggs together in Desoto"
    if(dentonsCoochie == 4):
        biglankyFuck = "Big Honcho Stanford should get worse then a 4, cmon stop drinking its early in the morning"
    if(dentonsCoochie < 5):
        biglankyFuck = "You had to have mistyped. Enter an honest number (anything below a 10 is very genrous"
    print(biglankyFuck)
              
playersName()
locationPoops()
doYouEnjoyPoop()
pickPlanet()
dentonWhitesideIsSuchApussy()
