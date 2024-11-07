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
            
        
class Game(simpleGE.scene):
    def__init__(self):
        super().__init__()
        self.setImage("cityscape.png")
        self.sndMolly = simpleGE.Sound("molly.wav")
        self.numMollys = 5
        self.score = 0
        
        self.lblbScore = LblScore()
        self.taxi = Taxi(self)
        self.mollys = []
        for i in range(self.numMollys):
            self.mollys.append(Molly(self))
        
        
        self.sprites = [self.taxi,self.mollys, self.lblScore]
        
    def process(self):
        for molly in self.mollys:
            
            if molly.collidesWith(self.taxi):
                molly.reset()
                self.sndMolly.play()
                self.score += 1
                self.lblScore.text = f"Score: {self.score}"

        
    
def main():
    game = Game()
    game.start()

if __name__==__ "main__":
    main()

