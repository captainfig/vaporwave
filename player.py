import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.rect.width
        self.height = self.rect.height
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.ax = 0.25
        self.ay = -0.25
        

    def moveX(self, velocity, direction):
        if direction == "left":
            self.dx = -velocity
        elif direction == "right":
            self.dx = velocity

    def moveY(self, velocity):
        if self.checkGround():
            self.ay = -0.25
            self.dy = -velocity
            self.rect.y -= 2
        

    def stop(self):
        moving = True
        if self.dx > 0:
            while moving:
                self.dx -= self.ax
                if self.dx == 0:
                    moving = False
        elif self.dx < 0:
            while moving:
                self.dx += self.ax
                if self.dx == 0:
                    moving = False

    def checkGround(self):
        onGround = False
        if self.rect.y + self.height >= 179:
            onGround = True
        return onGround
            

    def update(self):
        self.rect.x += self.dx
        
        if self.checkGround():
            self.ay = 0
            self.dy = 0
            self.rect.y = 180 - self.height
        
        self.rect.y += self.dy
        self.dy -= self.ay

            
        

