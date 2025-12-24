from pygame import *
from My_TextBox import *
mixer.init()
font.init()

win_w = 700
win_h = 400
FPS = 60
game_mode_menu = False
main_menu = True
rules_menu = False
setting_menu = False
programm = True
left_score = 0
right_score = 0
window = display.set_mode((win_w,win_h))#,RESIZABLE)
display.set_caption('Пинпонг')

sound = mixer.Sound('фоновая.ogg')
sound.set_volume(0.2)
sound.play()
kick = mixer.Sound('отскок.ogg')



# Функция TextBox

    
def output(text):
    global game_mode_menu
    if right_name.text != '' and left_name.text != '':
        game_mode_menu = True


def start_play():
    global game_mode_menu
    game_mode_menu = True
    main_menu = False
    rules_menu = False
    setting_menu = False

def set_setting():
    global setting_menu
    setting_menu = True
    game_mode_menu = False
    main_menu = False
    rules_menu = False




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
    def __init__(self,sprite_w,sprite_h,sprite_x,sprite_y,sprite_image,sprite_speed):
        super().__init__(sprite_w=sprite_w, sprite_h=sprite_h, sprite_x=sprite_x, sprite_y=sprite_y, sprite_image=sprite_image, sprite_speed=sprite_speed)
        self.x_speed = sprite_speed
        self.y_speed = sprite_speed

    def move(self,object1,object2):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        if self.rect.y <=0 or self.rect.y >= win_h-self.h:
            self.y_speed *= -1
            kick.play()
        if sprite.collide_rect(self, object1,) or sprite.collide_rect(self, object2):
            kick.play()
            #x_speed *= -1 просто смена направления
            self.x_speed = (abs(self.x_speed)+1)/(self.x_speed/abs(self.x_speed)) * -1
            self.y_speed = (abs(self.y_speed)+1)/(self.y_speed/abs(self.y_speed))

            #left_player.speed += m_speed
            #right_player.speed += m_speed



    def back(self):
        global left_score
        global right_score
        if self.rect.x <= 0:
            right_score += 1
            self.rect.x = 310
            self.x_speed = self.speed
            self.y_speed = self.speed
            #left_player.speed = s_speed
            #right_player.speed = s_speed
            time.delay(500)
        if self.rect.x >= win_w-self.w:
            left_score += 1
            self.rect.x = 310
            self.x_speed = self.speed
            self.y_speed = self.speed
            #left_player.speed = s_speed
            #right_player.speed = s_speed
            time.delay(500)
        


class Player(GameSprite):
     def move(self,key1,key2):
        key_pressed = key.get_pressed()
        if key_pressed[key1] and self.rect.y >0:
            self.rect.y -= self.speed
        if key_pressed[key2] and self.rect.y < win_h-self.h:
            self.rect.y += self.speed

    
class Button():
    def __init__(self, x, y, width, height, text, color=(50, 50, 50), border_col=(100, 100, 100), border_width=2, font_style=None, font_size=None, font_col=(255, 255, 255), on_submit=None):
        self.color = color
        self.font_style = font_style
        if font_size is None:
            self.font_size = int(height*(4/3))
        else:
            self.font_size = font_size
        self.font_col = font_col
        self.on_submit = on_submit
        self.text = text
        self.border_col = border_col
        self.border_width = border_width

        self.rect = Rect(x, y,width,height)
        self.font = font.SysFont(self.font_style,self.font_size)

    def draw(self, screen):                                                      
        draw.rect(screen, self.color, self.rect)             
        draw.rect(screen, self.border_col, self.rect, self.border_width)
        text_surface = self.font.render(self.text, True, self.font_col)
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y))



    def clicked(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.on_submit()

      

background = GameSprite(win_w,win_h,0,0,'background2.png',0)
ball = Ball(40,40,310,100,'Ball.png',2)
left_player = Player(10,100,130,100,'пинпонг.png',5)
right_player = Player(10,100,560,100,'пинпонг.png',5)

# Объекты TextBox
right_name = TextInput(100, 100 ,200 ,50, on_submit=output)
left_name = TextInput(100, 200, 200, 50, on_submit=output)




# Объекты Button
rules_button = Button(35, 100, 250, 50, 'Справка', on_submit=None)
game_mode_button = Button(35, 200, 250, 50, 'Играть', on_submit=start_play)
setting_button = Button(35, 300, 250, 50, 'Настройки', on_submit=set_setting)



font1 = font.Font(None,35)
font2 = font.Font(None,70)
#! Поясняющие надписи к вводу имени
#name_1 = font1.render('имя левого игрока:', True, (0,0,0))
#name_2 = font1.render('имя правого игрока:', True, (0,0,0))
#FAQ = font1.render('Введите имена игроков и нажмите enter', True, (0,0,0))
programm_name = font2.render('Pingpong', True, (0,0,0))

x_speed = ball.speed
y_speed = ball.speed



clock = time.Clock()
while programm:
    all_events = event.get()
    for events in all_events:
        if events.type == QUIT:
            programm = False

        #right_name.handle_event(events)
        #left_name.handle_event(events)
        rules_button.clicked(events)
        game_mode_button.clicked(events)
        setting_button.clicked(events)

    if main_menu:
        window.fill((130, 235, 255))
        window.blit(programm_name,(45,15))
        rules_button.draw(window)
        game_mode_button.draw(window)
        setting_button.draw(window)

    if setting_menu:
        window.fill((130, 235, 255))







    # Заполнение окна цветом и запрос имени
    '''
    if not game_mode_menu:
        window.fill((130, 235, 255))
        #window.blit(name_2, (425,65))
        #window.blit(name_1, (35,65))
        #window.blit(FAQ, (90,250))
        right_name.draw(window)
        left_name.draw(window)
        name1 = font1.render(right_name.text, True, (0,0,0))
        name2 = font1.render(left_name.text, True, (0,0,0))


            

    '''
    if game_mode_menu:
        background.reset()
        ball.reset()
        ball.move(left_player,right_player)
        ball.back()
        left_player.reset()
        left_player.move(K_w,K_s)
        right_player.reset()
        right_player.move(K_UP,K_DOWN)

        #window.blit(name1, (605,10))
        #window.blit(name2, (10,10))

        score1 = font1.render(str(right_score),True,(0,0,0))
        score2 = font1.render(str(left_score),True,(0,0,0))
        window.blit(score1,(605,40))
        window.blit(score2, (10,40))
        '''
        if right_score == 5:
            win = font2.render((right_name+' win!'),True,(225,0,0))
            window.blit(win,(260,150))
            game_mode_menu = False
        if left_score == 5:
            win = font2.render((left_name+' win!'),True,(225,0,0))
            window.blit(win,(260,150))
            game_mode_menu = False
        '''
        
    display.update()
    clock.tick(FPS)
