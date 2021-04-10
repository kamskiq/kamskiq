from pygame import *
import time
class GameSprite(sprite.Sprite):
    def __init__(self,wid,hei, player_image, player_x, player_y,player_speed):
        super().__init__()
        self.wid1 = wid
        self.hei1=hei
        self.image=transform.scale(image.load(player_image), (wid,hei))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def pad(self):
            self.rect.y+=self.speed 
    def update(self):
        
        
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x-= self.speed
        if keys[K_RIGHT] and self.rect.x < 600:
            
            self.rect.x+= self.speed
        
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y+= self.speed
        new_time=0
        start_time=0
        if sprite.groupcollide(players,osts, False, False):
            if keys[K_UP] and new_time-start_time < 2 :
                clock = time.clock()
                start_time = time.time()
                cur_time = start_time
                
                for i in range(20):
                    #new_time = time.time()
                    self.rect.y-= self.speed 
                new_time = time.time()
                print(new_time-start_time)
        else:
            self.pad()
        '''        
        elif keys[K_UP] and new_time-start_time < 2:
            clock = time.clock()
            start_time = time.time()
            cur_time = start_time
                
            for i in range(2):
                
                self.rect.y-= self.speed 
            new_time = time.time()
            print(new_time-start_time)
        '''
       
class Ship(GameSprite):
    def update(self):
        self.rect.x+=self.speed

#создай окно игры

player = Player(40,40,'hero1.png', 300, 150, 1)
xpl= player.rect.centerx
ypl = player.rect.top
player2 = Player(40,40, 'hero2.png',xpl, ypl, 1 )

ost= GameSprite(130,70,'os.png', 300, 200, 4)
ost1= GameSprite(130,70,'os.png', 100, 200, 4)
hr1= GameSprite(40,40,'heart.png', 20, 20, 4)
hr2= GameSprite(40,40,'heart.png', 60, 20, 4)
ship=Ship(200,400,'ship.png', -1000, 70, 1)
hr3= GameSprite(40,40,'heart.png', 100, 20, 4)
window = display.set_mode((700,500))

x1=200
y1=300
x2=100
y2=200
display.set_caption('test')
players=sprite.Group()
players.add(player)
osts=sprite.Group()
osts.add(ost1)
osts.add(ost)
hrs=sprite.Group()
hrs.add(hr1)
hrs.add(hr2)
hrs.add(hr3)
background = transform.scale(image.load('images.png'), (700,500))
#window.blit(background, (0,0))
#clock = time.Clock()
FPS = 120
jp= False
game = True
#start_time = time.time()
#cur_time = start_time
while game:

    window.blit(background, (0,0))
    #clock.tick(FPS)
    for e in event.get():
        if e.type == QUIT:
            game = False
    #время
    #new_time = time.time()
    #print(new_time-start_time)
    if sprite.spritecollide(ship,players, True):
        game = False
    if jp == True:
        player2.reset()
        player2.update()
        
        player.kill()
        
    
    ost.reset()
    #отображать сворд как группу
    
    ost1.reset()
    hrs.update()
    hrs.draw(window)
    ship.update()
    ship.reset()
    players.update()
    players.draw(window)
    display.update()

#обработай событие «клик по кнопке "Закрыть окно"»
