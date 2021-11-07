import pygame
from pygame.draw import *
from random import *
from math import sqrt
import yaml
COLORS = ((0, 255, 0), (25, 116, 210), (255, 204, 0))
color_inactive = (100, 100, 100)
color_active = (255, 255, 255)
color = color_inactive
borders = (10, 590, 40, 590)
FPS = 20
score = 0
textscore = str(score)
screen = pygame.display.set_mode((800, 600))
pygame.font.init()
f1 = pygame.font.Font(None, 50)
f2 = pygame.font.Font(None, 250)
f3 = pygame.font.Font(None, 20)
text2 = f2.render("+2", True, (255, 255, 255))
text3 = f2.render("+1", True, (255, 255, 255))
name = ''
textname = f1.render(name, True, (0, 0 , 0))
text4 = f1.render('your name:', True, (255, 255, 255))
with open ("yamlu/OG_GARNIZON.yml", "r") as f:
    loaded = yaml.safe_load(f) 
rating_name = ['']*5
rating_score = ['']*5
for el in range(5):
    rating_name[el] = loaded['result'][el].get('name')
    if rating_name[el] == '':
        rating_name[el] = 'unnamed'
    rating_score[el] = str(loaded['result'][el].get('points'))
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
cultimgigachad_list = list()

for i in range(10):
    balls_list.append(Balls())

for i in range(10):
    cultimgigachad_list.append(cultimgigachad())

while not finished:
    input_box = rect(screen, color, (220, 10, 140, 32))
    clock.tick(FPS)
    text1 = f1.render(textscore, True, (255, 5, 5))
    screen.blit(text1, (400, 10))
    textname = f1.render(name, True, (0, 0 , 0))
    screen.blit(textname, (220, 10))
    screen.blit(text4, (20, 10))
    for el in range(5):
        rating_score_text = f1.render(rating_score[el], True, (255, 255, 255))
        screen.blit(rating_score_text, (750, 10 + 30*el))
        rating_name_text = f1.render(rating_name[el], True, (255, 255, 255))
        screen.blit(rating_name_text, (500, 10 + 30*el))
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
        if event.type == pygame.KEYDOWN:
            color = color_active
            if event.key == pygame.K_RETURN:
                color = color_inactive
            elif event.key == pygame.K_BACKSPACE:
                name = name[:-1]
            else:
                name += event.unicode
    for i, ball in enumerate(balls_list):
            ball.collisionx()
            ball.collisiony()
            ball.move()

    for i, gigachad in enumerate(cultimgigachad_list):
            gigachad.collisionx()
            gigachad.collisiony()
            gigachad.move()

    if event.type == pygame.QUIT:
        loaded['result'].append({'name': name, 'points': score})
        loaded['result'] = sorted(loaded['result'], key=lambda x: x['points'], reverse=True)
        finished = True
    textscore = str(score)
    pygame.display.update()
    screen.fill((0, 0, 0))

pygame.quit()
with open ("yamlu/OG_GARNIZON.yml", 'w') as f:
    yaml.dump(loaded, f)