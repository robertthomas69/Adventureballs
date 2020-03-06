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
    
    if(lower(enjoyPoo) == "yes"):
        print("I see you answered yes, you are a ceritified turd.")

              
playersName()
locationPoops()
doYouEnjoyPoop()
answerBack()
