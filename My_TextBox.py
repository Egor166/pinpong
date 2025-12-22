import pygame
pygame.init()

'''
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Консольный ввод")
clock = pygame.time.Clock()
game = True
'''




class TextInput:
    def __init__(self, x, y, width,height,input_col = (50, 50, 50),border_col = (255, 0, 0),border_width = 2,
                 font_style = None,font_size = None,font_col = (255, 255, 255),on_submit=None):
        
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        #! допы
        self.input_col = input_col
        self.border_col = border_col
        self.border_width = border_width
        self.font_style = font_style
        if font_size is None:
            # Автоматический расчет
            self.font_size = int(height*(4/3))
        else:
            self.font_size = font_size
        self.font_col = font_col
        self.on_submit = on_submit



        #! константы
        self.text = ""
        self.cursor_visible = True
        self.cursor_timer = 0




        

        


    def handle_event(self, event):           
        if event.type == pygame.KEYDOWN:  # Только события нажатия клавиш
            if event.key == pygame.K_RETURN:  # Клавиша Enter
                if self.text:  # Если есть текст
                    if self.on_submit != None:
                        self.on_submit(self.text)
                        print(self.text)  # Передаем текст в функцию
                    else:
                        # Иначе используем стандартное поведение
                        print(f"> {self.text}")
                    self.text = ""  # Очищаем поле


            elif event.key == pygame.K_BACKSPACE:  # Клавиша Backspace
                self.text = self.text[:-1]  # Удаляем последний символ

                    
            elif event.unicode.isprintable():  # Любой печатный символ
                self.text += event.unicode  # Добавляем к тексту



                    

    def update(self):
        # Мигание курсора
        self.cursor_timer += 1
        if self.cursor_timer > 30:
            self.cursor_visible = not self.cursor_visible
            self.cursor_timer = 0
            
    def draw(self, screen):
        font = pygame.font.SysFont(self.font_style,self.font_size)
        
        # Рисуем фон                                                        
        pygame.draw.rect(screen, self.input_col, (self.x, self.y, self.width, self.height))             
        pygame.draw.rect(screen, self.border_col, (self.x, self.y, self.width, self.height), self.border_width)
        
        # Рисуем текст
        text_surface = font.render(self.text, True, self.font_col)
        screen.blit(text_surface, (self.x + 5, self.y))             
        
        # Рисуем курсор
        if self.cursor_visible:
            cursor_x = self.x + 5 + text_surface.get_width()
            pygame.draw.line(screen, (255, 255, 255), 
                           (cursor_x, self.y + 5), 
                           (cursor_x, self.y + self.height-5), 2)

# Создаем поле ввода
#console = TextInput(50, 500, 700, 80)



'''
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        
        console.handle_event(event)
    
    console.update()
    
    # Очистка экрана
    screen.fill((20, 20, 20))
    
    # Рисуем историю команд
    font = pygame.font.Font(None, 28)

    
    console.draw(screen)
    
    # Инструкция
    info = font.render("Введите команду и нажмите Enter", True, (200, 200, 0))
    screen.blit(info, (50, 460))
    
    pygame.display.flip()
    clock.tick(60)
'''





























