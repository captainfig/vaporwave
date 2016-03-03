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
        # set width and height
        self.width = self.rect.width
        self.height = self.rect.height
        # set velocity and acceleration
        self.dx = 0
        self.dy = 0
        self.ay = constants.GRAV
        # set variable to retrieve platforms from main
        self.walls = None
        
        

    def moveLeft(self):
        # Move in negative x direction
        self.dx = -constants.X_VEL

    def moveRight(self):
        # Move in positive x direction
        self.dx = constants.X_VEL

    def jump(self):
        # Move down 2 pixels and check for collision, then move back up 2 pixels
        self.rect.y += 2
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        self.rect.y -=2
        # jump if sprite is on the ground, or collided with a platform
        if self.checkGround() or len(block_hit_list)>0:
            self.dy = -constants.Y_VEL
            self.rect.y -= 4
        
    def stop(self):
        # set x velocity to zero to stop movement
        self.dx = 0

    def checkGround(self):
        onGround = False
        # if bottom of rectangle is greater than or equal to the screen height,
        # then the sprite is on the ground
        if self.rect.bottom >= constants.SCR_HEIGHT:
            onGround = True
        return onGround

    def addGrav(self):
        # If platform moves, this ensures player moves with it
        if self.dy == 0:
            self.dy = 1
        else:
            self.dy -= constants.GRAV

        if self.checkGround():
            # If on the ground, negate gravity
            self.dy = 0
            self.rect.y = constants.SCR_HEIGHT - self.height

    def update(self):
        # Account for gravity
        self.addGrav()
        
        # move in x direction
        self.rect.x += self.dx

        # check if x movement resulted in collision
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            if self.dx > 0:
                self.rect.right = block.rect.left
            if self.dx < 0:
                self.rect.left = block.rect.right

        # check if x movement goes off screen
        if self.rect.right >= constants.SCR_WIDTH:
            self.rect.right = constants.SCR_WIDTH
        elif self.rect.x <= 0:
            self.rect.x = 0

        # move in y direction
        self.rect.y += self.dy

        # check if y movement resulted in collision
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            if self.dy > 0:
                self.rect.bottom = block.rect.top
            if self.dy < 0:
                self.rect.top = block.rect.bottom
            self.dy=0
            
        

            
        

