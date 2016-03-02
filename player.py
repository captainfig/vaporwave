import pygame, constants

class Player(pygame.sprite.Sprite):
    # constrctor class that takes x, y coordinates as parameters
    def __init__(self, x, y):
        # call parent constructor
        pygame.sprite.Sprite.__init__(self)
        # set sprite image and rectangle
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect()
        # set position
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y
        # set width and height
        self.width = self.rect.width
        self.height = self.rect.height
        # set velocity and acceleration
        self.dx = 0
        self.dy = 0
        self.ax = 0.25
        self.ay = -0.25
        

    def moveX(self, velocity, direction):
        # if moving left, move in negative direction
        if direction == "left":
            self.dx = -velocity
        # if moving right, move in positive direction
        elif direction == "right":
            self.dx = velocity

    def moveY(self, velocity):
        # if sprite is on the ground, jump
        if self.checkGround():
            self.ay = -0.25
            self.dy = -velocity
            self.rect.y -= 4
        

    def stop(self):
        # set x velocity to zero to stop movement
        self.dx = 0

    def checkGround(self):
        onGround = False
        # sum of top-left y-coord and sprite height equals bottom-left y-coord
        # if that y-coord is 1 pixel or less from bottom edge of the screen,
        # then the sprite is on the ground
        if self.rect.y + self.height >= constants.SCR_HEIGHT - 2:
            onGround = True
        return onGround
            

    def update(self):
        # move in x direction
        self.rect.x += self.dx

        # remove affect of gravity if player is on the ground
        if self.checkGround():
            self.ay = 0
            self.dy = 0
            self.rect.y = constants.SCR_HEIGHT - self.height
        # move in y direction
        self.rect.y += self.dy
        self.dy -= self.ay

            
        

