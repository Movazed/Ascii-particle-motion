from src.Vector2D import Vector2D

class Particle():
    def __init__(self, position, matrix, lifespan = 255, size = 25):
        self.position = position
        self.velocity = Vector2D(0,0)
        self.acceleration = Vector2D(0,0)    
        self.lifespan = lifespan
        self.size = size
        self.max = matrix.size

    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity
        friction = 0.9
        if self.position.x > self.max.x-1:
            self.position.x = self.max.x-1
            self.velocity.x = self.velocity.x*-1*friction
        
        if self.position.y > self.max.y-1:
            self.position.y = self.max.y-1
            self.velocity.y = self.velocity.y*-1*friction
        
        if self.position.x < 0:
            self.position.x = 1
            self.velocity.x = self.velocity.x*-1*friction
        
        if self.position.y < 0:
            self.position.y = 1
            self.velocity.y = self.velocity.y*-1*friction

    def pre_render(self,matrix):
        matrix.place(self.size,self.position.round())
