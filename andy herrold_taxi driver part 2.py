#andyherrold_taxidriver
#slide and catch game part 1
import pygame, simpleGE, random
"""
taxidriver.py
slide and catch game
andy herrold
"""

class Molly(simpleGE.Sprite):
    def__init__(self, scene):
        super()__init__(scene)
        self.setImage("Molly.png")
        self.setSize(25, 25)
        self.minSpeed = 3
        self.maxSpeed = 8
        self.reset()
        
class Taxi(simpleGE.Sprite):
    def__init__(self, scene):
        super().__init__(scene)
        self.setImage("Taxi.png")
        self.setSize(50, 50)
        self.position = (320, 400)
        self.moveSpeed = 5
        
    def reset(self):
        self.y = 10
        self.x = random.randint(0, self.screenWidth)
        
        self.dy = random.randint(self.minSpeed, self.maxSpeed)
        
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()
        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_right):
            self.x += self.moveSpeed
            
Class LblScore(impleGE.Label):
    def__init__(self):
        super().__init__()
        self.text = "Score: 0"
        
        self.center (100, 30)
        
class LblTime(simpleGE.Label):
    def__init__(self):
        super().__init__()
        self.text = "Time left: 10"
        self.center = (500, 30)
            
        
class Game(simpleGE.scene):
    def__init__(self):
        super().__init__()
        self.setImage("cityscape.png")
        self.sndMolly = simpleGE.Sound("molly.wav")
        self.numMollys = 5
        self.score = 0
        self.lblScore = LblScore()
        
        self.timer = simpleGE.Timer()
        self.timer.totalTime = 10
        self.lblTime = LblTime()
        
        self.taxi = Taxi(self)
        self.mollys = []
        for i in range(self.numMollys):
            self.mollys.append(Molly(self))
        
        
        self.sprites = [self.taxi,self.mollys, self.lblScore, self.lblTime]
        
    def process(self):
        for molly in self.mollys:
            
            if molly.collidesWith(self.taxi):
                molly.reset()
                self.sndMolly.play()
                self.score += 1
                self.lblScore.text = f"Score: {self.score}"
                self.lblScore.text = f"Score: {self.score}"
                
        self.lblTime.text = f"Time Left: {self.timer.getTimeLeft(): .2f}"
        if self.timer.getTimeLeft() < 0:
            print(f"Score: {self.score}")
            self.stop()
            
class Instructions(simpleGE.Scene):
    def__init__(self, prevScore):
        super().__init__()
        
        self.prevScore = prevScore
        self.setImage("cityscape.png")
        self.response = "Quit"
        
        self.directions = simpleGE.MultiLabel()
        self.directions.textlines = [
        "You are the Taxi driver",
        "Move with the left and right arrow keys.",
        "Dodge as many Molotov cocktails as you can",
        "in the time provided"
        "",
        "Good Luck!"]
        
        self.directions.center = (320, 200)
        self.directions.size = (500, 250)
        
        self.btnPlay = simpleGE.Button()
        self.btnPlay.text = "Play"
        self.btnPlay.center = (100, 400)
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "Quit"
        self.btnQuit.center = (550, 400)
        
        self.lblScore = simplGE.Label()
        self.lblScore.text = "Last score: 0"
        self.lblScore.center = (320, 400)
        
        self.lblScore.text = f"Last score: {self.prevScore}"
        
        self.sprites = [self.directions, self.btnPlay, self.btnQuit, self.lblScore]
    
        
    def process(self):
        if self.btnPlay.clicked:
            self.response = "Play"
            self.stop()
            
        if self.btnQuit.clicked:
            self.response = "Quit"
            self.stop()
        
        
        
        
        
                

        
    
def main():
    
    keepGoing = True
    lastScore = 0
    while keepGoing:
        instructions = Instructions(lastScore)
        instructions.start()
        
        
        
        if instructions.response == "Play":
            game = Game()
            game.start()
            LastScore = game.score
        else:
            keepGoing = False
        
        
        
        

if __name__==__ "main__":
    main()

