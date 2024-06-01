#Створи власний Шутер!
from random import*
from typing import Any
from pygame import *

# клас-батько для інших спрайтів
class GameSprite(sprite.Sprite):
    # конструктор класу
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # викликаємо конструктор класу (Sprite):
        sprite.Sprite.__init__(self)
        # кожен спрайт повинен зберігати властивість image - зображення
        self.image = transform.scale(
            image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
        # кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    # метод, що малює героя на вікні
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


    


# клас головного гравця
class Player(GameSprite):
    def update(self, ):
        keys = key.get_pressed()

        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 650:
            self.rect.x += self.speed
    def shoot():
        pass

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 450:
            x = randint(5,645)
            self.rect.x = x 
            self.rect.y = 5 
x = randint(5,645)
speed = randint(1,7)
enemy = Enemy("ufo.png",x,5,50,50,speed)
enemy1 = Enemy("ufo.png",x,5,50,50,speed)
enemy2 = Enemy("ufo.png",x,5,50,50,speed)
enemy3 = Enemy("ufo.png",x,5,50,50,speed)
enemy4 = Enemy("ufo.png",x,5,50,50,speed)
enemy5 = Enemy("ufo.png",x,5,50,50,speed)

win_w = 700
win_h = 500

ship = Player("rocket.png",0,440,50,70,10)


window = display.set_mode((win_w,win_h))
display.set_caption("SHOOTER")
background = transform.scale(image.load("galaxy.jpg"),(win_w,win_h))

mixer.init()
mixer.music.load("space.ogg")
mixer.music.play()


clock = time.Clock()
FPS = 60


game = True
finish = False
while game :
    for e in event.get():
        if e.type == QUIT:
            game = False
    #while not finish:
    window.blit(background,(0,0))
    enemy.reset()
    enemy.update()
    enemy1.reset()
    enemy1.update()
    enemy2.reset()
    enemy2.update()
    enemy3.reset()
    enemy3.update()
    enemy4.reset()
    enemy4.update()
    enemy5.reset()
    enemy5.update()
    ship.reset()
    ship.update()
    clock.tick(FPS)
    display.update()


