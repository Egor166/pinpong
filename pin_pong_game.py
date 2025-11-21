from pygame import *
import pygame_widgets
from pygame_widgets.textbox import TextBox
mixer.init()
font.init()

win_w = 700
win_h = 400
FPS = 60
finish = False
finish_num = 0
game = True
left_score = 0
right_score = 0
window = display.set_mode((win_w,win_h))
display.set_caption('Пинпонг')

sound = mixer.Sound('фоновая.ogg')
sound.set_volume(0.2)
sound.play()
kick = mixer.Sound('отскок.ogg')

def output():
    global finish_num
    finish_num += 1
    print(finish_num)


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
            kick.play()
        if sprite.collide_rect(self, object1,) or sprite.collide_rect(self, object2):
            kick.play()
            x_speed *= -1


    def back(self):
        global left_score
        global right_score
        if self.rect.x <= 0:
            right_score += 1
            self.rect.x = 310
            time.delay(500)
        if self.rect.x >= win_w-self.w:
            left_score += 1
            self.rect.x = 310
            time.delay(500)
        


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
        

background = GameSprite(win_w,win_h,0,0,'background2.png',0)
ball = Ball(40,40,310,100,'Ball.png',4)
left_player = Player(10,100,130,100,'пинпонг.png',5)
right_player = Player(10,100,560,100,'пинпонг.png',5)

right_name = TextBox(window, win_w-310, 100, 300, 80, fontSize=50,onSubmit=output)#input('имя правого игрока:')
left_name = TextBox(window, 10, 100, 300, 80, fontSize=50,onSubmit=output) #input('имя левого игрока:')

font1 = font.Font(None,35)
font2 = font.Font(None,70)

name_1 = font1.render('player1 name:', True, (0,0,0))
name_2 = font1.render('player2 name:', True, (0,0,0))

x_speed = ball.speed
y_speed = ball.speed

clock = time.Clock()


while game:
    events = event.get()
    for e in events:
        if e.type == QUIT:
            game = False

    if not  finish:
        window.fill((255, 255, 255))
        window.blit(name_2, (515,10))
        window.blit(name_1, (10,10))
        pygame_widgets.update(events)
        name1 = font1.render(right_name.getText(), True, (0,0,0))
        name2 = font1.render(left_name.getText(), True, (0,0,0))
        if finish_num == 2:
            finish = True

    if finish:
        background.reset()
        ball.reset()
        ball.move(left_player,right_player)
        ball.back()
        left_player.reset()
        left_player.move_left()
        right_player.reset()
        right_player.move_right()

        window.blit(name1, (605,10))
        window.blit(name2, (10,10))

        score1 = font1.render(str(right_score),True,(0,0,0))
        score2 = font1.render(str(left_score),True,(0,0,0))
        window.blit(score1,(605,40))
        window.blit(score2, (10,40))

        '''if right_score == 5:
            win = font2.render((right_name+' win!'),True,(225,0,0))
            window.blit(win,(260,150))
            Finish = False
        if left_score == 5:
            win = font2.render((left_name+' win!'),True,(225,0,0))
            window.blit(win,(260,150))
            finish = False'''
        
    display.update()
    clock.tick(FPS)
