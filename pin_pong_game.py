from pygame import *
mixer.init()
font.init()

win_w = 700
win_h = 400
FPS = 60
finish = True
game = True
window = display.set_mode((win_w,win_h))
display.set_caption('Пинпонг')
mixer.music.load('фоновая.ogg')
mixer.music.play()

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
    def move(self):
        q = 1
        w = 2
        self.rect.x += q
        self.rect.y += w
        if self.rect.y <=0 or self.rect.y >= win_h-self.h:
            w *= -1

background = GameSprite(win_w,win_h,0,0,'background2.png',0)
ball = Ball(50,50,100,100,'Ball.png',2)


clock = time.Clock()
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish:
        background.reset()
        ball.reset()
        ball.move()


        
    display.update()
    clock.tick(FPS)
