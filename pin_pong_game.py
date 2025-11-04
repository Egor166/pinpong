from pygame import *
mixer.init()
font.init()
#! Константы
win_w = 700
win_h = 400
FPS = 60
finish = True
game = True
#! Главное окно
window = display.set_mode((win_w,win_h))
display.set_caption('Пинпонг')
#! Музыка
mixer.music.load('фоновая.ogg')
#mixer.music.play()
kick = mixer.Sound('отскок.ogg')

#! Классы
class GameSprite(sprite.Sprite):
    def __init__(self,sprite_w,sprite_h,sprite_x,sprite_y,sprite_image,sprite_speed):
        super().__init__()
        self.w = sprite_w
        self.h = sprite_h
        self.image = transform.scale(image.load(sprite_image),(self.w,self.h))
        self.rect = self.image.get_rect()
        self.rect.x = sprite_x
        self.rect.y = sprite_y
        self.speed = sprite_speed

    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))


class Ball(GameSprite):
    def move(self,object1,object2):
        global x_speed
        global y_speed
        self.rect.x += x_speed
        self.rect.y += y_speed
        if self.rect.y <=0 or self.rect.y >= win_h-self.h:
            y_speed *= -1
            #kick.play()
        if sprite.collide_rect(self, object1,) or sprite.collide_rect(self, object2):
            kick.play()
            x_speed *= -1

class Player(GameSprite):
    def move_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >=0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y <= win_h-self.h:
            self.rect.y += self.speed
    def move_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y <= win_h-self.h:
            self.rect.y += self.speed
        
#! Основной код

background = GameSprite(win_w,win_h,0,0,'background2.png',0)
ball = Ball(40,40,170,100,'Ball.png',2)
x_speed = ball.speed
y_speed = ball.speed
left_player = Player(10,100,130,100,'пинпонг.png',5)
right_player = Player(10,100,560,100,'пинпонг.png',5)

#! Игровой цикл
clock = time.Clock()
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish:
        background.reset()
        ball.reset()
        ball.move(left_player,right_player)
        left_player.reset()
        left_player.move_left()
        right_player.reset()
        right_player.move_right()
        


        
    display.update()
    clock.tick(FPS)
