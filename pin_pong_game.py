from pygame import *
from My_TextBox import *
mixer.init()
font.init()

win_w = 700
win_h = 400
FPS = 60
finish = False
game = True
left_score = 0
right_score = 0
window = display.set_mode((win_w,win_h))
display.set_caption('Пинпонг')

sound = mixer.Sound('фоновая.ogg')
sound.set_volume(0.2)
sound.play()
kick = mixer.Sound('отскок.ogg')



# Функция TextBox

    
def output(text):
    global finish
    if right_name.text != '' and left_name.text != '':
        finish = True






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
            #x_speed *= -1 просто смена направления
            x_speed = (abs(x_speed)+1)/(x_speed/abs(x_speed)) * -1
            y_speed = (abs(y_speed)+1)/(y_speed/abs(y_speed))

            #left_player.speed += m_speed
            #right_player.speed += m_speed



    def back(self):
        global left_score
        global right_score
        global x_speed
        global y_speed
        if self.rect.x <= 0:
            right_score += 1
            self.rect.x = 310
            #x_speed = s_speed
            #y_speed = s_speed
            #left_player.speed = s_speed
            #right_player.speed = s_speed
            time.delay(500)
        if self.rect.x >= win_w-self.w:
            left_score += 1
            self.rect.x = 310
            #x_speed = s_speed
            #y_speed = s_speed
            #left_player.speed = s_speed
            #right_player.speed = s_speed
            #time.delay(500)
        


class Player(GameSprite):
     def move(self,key1,key2):
        key_pressed = key.get_pressed()
        if key_pressed[key1] and self.rect.y >0:
            self.rect.y -= self.speed
        if key_pressed[key2] and self.rect.y < win_h-self.h:
            self.rect.y += self.speed


        

background = GameSprite(win_w,win_h,0,0,'background2.png',0)
ball = Ball(40,40,310,100,'Ball.png',2)
left_player = Player(10,100,130,100,'пинпонг.png',5)
right_player = Player(10,100,560,100,'пинпонг.png',5)

# Объекты TextBox
right_name = TextInput(100,100,200,50,on_submit=output)
left_name = TextInput(100,200,200,50,on_submit=output)



font1 = font.Font(None,35)
font2 = font.Font(None,70)
# Поясняющие надписи к вводу имени
name_1 = font1.render('имя левого игрока:', True, (0,0,0))
name_2 = font1.render('имя правого игрока:', True, (0,0,0))
FAQ = font1.render('Введите имена игроков и нажмите enter', True, (0,0,0))

x_speed = ball.speed
y_speed = ball.speed


time.delay(2000)
clock = time.Clock()
while game:
    all_events = event.get()
    for events in all_events:
        if events.type == QUIT:
            game = False

        right_name.handle_event(events)
        left_name.handle_event(events)


    # Заполнение окна цветом и запрос имени
    if not finish:
        window.fill((130, 235, 255))
        window.blit(name_2, (425,65))
        window.blit(name_1, (35,65))
        window.blit(FAQ, (90,250))
        right_name.draw(window)
        left_name.draw(window)
        name1 = font1.render(right_name.text, True, (0,0,0))
        name2 = font1.render(left_name.text, True, (0,0,0))


            

  
    if finish:
        background.reset()
        ball.reset()
        ball.move(left_player,right_player)
        ball.back()
        left_player.reset()
        left_player.move(K_w,K_s)
        right_player.reset()
        right_player.move(K_UP,K_DOWN)

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
