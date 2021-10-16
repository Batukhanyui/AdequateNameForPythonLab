import pygame
from pygame.draw import *
from random import*
from math import sqrt

COLORS = ((0, 255, 0), (25, 116, 210), (255, 204, 0))
borders = (10, 590, 40, 590)
FPS = 10
score = 0
textscore = str(score)
screen = pygame.display.set_mode((600, 600))
pygame.font.init()
f1 = pygame.font.Font(None, 50)
f2 = pygame.font.Font(None, 250)
text2 = f2.render("+2", True, (255, 255, 255))
text3 = f2.render("+1", True, (255, 255, 255))

class Balls: 
    def __init__(self):
        self.x = randint(100, 500)
        self.y = randint(100, 500)
        self.r = randint(20, 30)
        self.vx = randint(15, 30)
        self.vy = randint(15, 30)
        self.color = choice(COLORS)

    def draw(self, surface=screen):
        circle(surface, self.color, (self.x, self.y), self.r)

    def move(self):
        self.y += self.vy
        self.x += self.vx

    def collisionx(self):
        if self.x < borders[0] + 1.2*self.r:
            self.vx *= -1
        elif self.x > borders[1] - 1.2*self.r:
            self.vx *= -1
            
    def collisiony(self):
        if self.y < borders[2] + self.r:
            self.vy *= -1
        elif self.y > borders[3] - self.r:
            self.vy *= -1

    def distance(self, clicker):
        return sqrt((clicker[0] - self.x)**2 + (clicker[1] - self.y)**2)

class cultimgigachad: 
    def __init__(self):
        self.x = randint(100, 500)
        self.y = randint(100, 500)
        self.r = randint(40, 60)
        self.vx = randint(15, 30)
        self.vy = randint(15, 30)
        self.color = choice(COLORS)

    def draw(self, surface=screen):
        rect(surface, self.color, (self.x, self.y, self.r, self.r))

    def move(self):
        self.y += self.vy
        self.x += self.vx

    def collisionx(self):
        if self.x < borders[0] + 0.2*self.r:
            self.vx *= -1
        elif self.x > borders[1] - 1.2*self.r:
            self.vx *= -1
            
    def collisiony(self):
        if self.y < borders[2] + 0.2*self.r:
            self.vy *= -1
        elif self.y > borders[3] - 1.2*self.r:
            self.vy *= -1

    def distance(self, clicker):
        return sqrt((clicker[0] - self.x - 0.5*self.r)**2 + (clicker[1] - self.y - 0.5*self.r)**2)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

balls_list = list()
for i in range(10):
    balls_list.append(Balls())

cultimgigachad_list = list()
for i in range(10):
    cultimgigachad_list.append(cultimgigachad())

while not finished:
    clock.tick(FPS)
    text1 = f1.render(textscore, True, (255, 255, 255))
    screen.blit(text1, (300, 10))
    for i, ball in enumerate(balls_list):
            ball.draw()

    for i, gigachad in enumerate(cultimgigachad_list):
            gigachad.draw()
    for event in pygame.event.get():
        for i, ball in enumerate(balls_list):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ball.distance(event.pos) < 1.1*ball.r:
                    balls_list.pop(i)
                    screen.blit(text2, (200, 100))
                    score += 2
        for i, gigachad in enumerate(cultimgigachad_list):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if gigachad.distance(event.pos) < 1.5*gigachad.r:
                    cultimgigachad_list.pop(i)
                    screen.blit(text3, (200, 400))
                    score += 1

    for i, ball in enumerate(balls_list):
            ball.collisionx()
            ball.collisiony()
            ball.move()

    for i, gigachad in enumerate(cultimgigachad_list):
            gigachad.collisionx()
            gigachad.collisiony()
            gigachad.move()

    if event.type == pygame.QUIT:
        finished = True
    textscore = str(score)
    pygame.display.update()
    screen.fill((0, 0, 0))

pygame.quit()