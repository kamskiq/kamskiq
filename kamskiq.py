#создай игру "Лабиринт"!
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,player_speed):
        super().__init__()
        self.image=transform.scale(image.load(player_image), (70,70))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
#or sprite.collide_rect(player, wall2) or sprite.collide_rect(player, wall)) or sprite.collide_rect(player, wall3) or sprite.collide_rect(player, wall4) or sprite.collide_rect(player, wall5) or sprite.collide_rect(player, wall6) or sprite.collide_rect(player, wall7):
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x-= self.speed
        if keys[K_RIGHT] and self.rect.x < 600:
            self.rect.x+= self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y-= self.speed
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y+= self.speed

        if keys[K_LEFT] and sprite.collide_rect(player, wall) or sprite.collide_rect(player, wall1) or sprite.collide_rect(player, wall2) or sprite.collide_rect(player, wall3) or sprite.collide_rect(player, wall4) or sprite.collide_rect(player, wall5) or sprite.collide_rect(player, wall6) or sprite.collide_rect(player, wall7):
            self.rect.x+= self.speed
        if keys[K_RIGHT] and sprite.collide_rect(player, wall) or sprite.collide_rect(player, wall1) or sprite.collide_rect(player, wall2) or sprite.collide_rect(player, wall3) or sprite.collide_rect(player, wall4) or sprite.collide_rect(player, wall5) or sprite.collide_rect(player, wall6) or sprite.collide_rect(player, wall7) :
            self.rect.x-= self.speed
        if keys[K_UP] and sprite.collide_rect(player, wall) or sprite.collide_rect(player, wall1) or sprite.collide_rect(player, wall2) or sprite.collide_rect(player, wall3) or sprite.collide_rect(player, wall4) or sprite.collide_rect(player, wall5) or sprite.collide_rect(player, wall6) or sprite.collide_rect(player, wall7):
            self.rect.y+= self.speed
        if keys[K_DOWN] and sprite.collide_rect(player, wall) or sprite.collide_rect(player, wall1) or sprite.collide_rect(player, wall2) or sprite.collide_rect(player, wall3) or sprite.collide_rect(player, wall4) or sprite.collide_rect(player, wall5) or sprite.collide_rect(player, wall6) or sprite.collide_rect(player, wall7):
            self.rect.y-= self.speed

        
class Enemy(GameSprite):
    def update(self):
        if self.rect.x <= 200:
           self.side = 't1'
        elif self.rect.x>= 610:
            self.side = 't2'

        if self.side == 't2':
            self.rect.x -=self.speed
        else:
            self.rect.x +=self.speed
        if self.rect.y <= 300:
            self.e = True
        elif self.rect.y >= 20:
            self.e = False
        if self.e == True:
            self.rect.y +=self.speed
        else:
            self.rect.y -=self.speed
class Wall(sprite.Sprite):
    def __init__(self, color1,color2, color3,wall_x, wall_y, wall_width, wall_heith):
        self.color1=color1
        self.color2=color2
        self.color3=color3
        self.width=wall_width
        self.heith = wall_heith
        self.image = Surface((self.width, self.heith))
        self.image.fill((color1,color2, color3))
        self.rect = self.image.get_rect()
        self.rect.y=wall_y
        self.rect.x = wall_x
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        
finish=False 
#создай окно игры
win_width=500
window = display.set_mode((700,win_width))
display.set_caption('Лабиринт')
background = transform.scale(image.load('images.png'), (700,500))
#window.blit(background, (0,0))
#создай 2 спрайта и размести их на сцене
player = Player('hero.png', 30, 200, 4)
game = True
clock = time.Clock()
FPS = 60

font.init()
font = font.Font(None,70)
while game:
    window.blit(background, (0,0))
    clock.tick(FPS)
    for e in event.get():
        if e.type == QUIT:
            game = False
    '''
    if finish != True:
        if sprite.collide_rect(player,gold):
            pass
        if sprite.collide_rect(player,player1): 
            
            pass
    '''
        player.reset()
        player.update()
        display.update()
       
#обработай событие «клик по кнопке "Закрыть окно"»
