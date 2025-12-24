import pygame
pygame.init()
class TextInput:
    def __init__(self, x, y, width,height,input_col=(50, 50, 50), border_col=(100, 100, 100), border_width=2,
                 font_style=None, font_size=None,font_col=(255, 255, 255), on_submit=None):
        self.input_col = input_col
        self.border_col = border_col
        self.border_width = border_width
        self.font_style = font_style
        if font_size is None:
            self.font_size = int(height*(4/3))
        else:
            self.font_size = font_size
        self.font_col = font_col
        self.on_submit = on_submit
        self.text = ""
        self.cursor_visible = True
        self.cursor_timer = 0
        self.active = False
        self.rect = pygame.Rect(x, y,width,height)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
                self.cursor_visible = True  # Сразу показываем курсор
                self.cursor_timer = 0
            else:
                self.active = False




        if self.active and event.type == pygame.KEYDOWN:  # Только события нажатия клавиш
            if event.key == pygame.K_RETURN:  # Клавиша Enter
                if self.text:  # Если есть текст
                    if self.on_submit != None:
                        self.on_submit(self.text)
                    else:
                        # Иначе используем стандартное поведение
                        print(self.text)
                        self.text = ""  # Очищаем поле
            elif event.key == pygame.K_BACKSPACE:  # Клавиша Backspace
                self.text = self.text[:-1]  # Удаляем последний символ                    
            elif event.unicode.isprintable():  # Любой печатный символ
                self.text += event.unicode  # Добавляем к тексту


    def update(self):
        # Мигание курсора
        if self.active:
            self.cursor_timer += 1
            if self.cursor_timer > 30:
                self.cursor_visible = not self.cursor_visible
                self.cursor_timer = 0
        else:
            self.cursor_visible = False
            

    def draw(self, screen):
        self.update()
        font = pygame.font.SysFont(self.font_style,self.font_size)                                                        
        pygame.draw.rect(screen, self.input_col, self.rect)             
        pygame.draw.rect(screen, self.border_col, self.rect, self.border_width)
        text_surface = font.render(self.text, True, self.font_col)
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y))             
        if self.cursor_visible:
            cursor_x = self.rect.x + 5 + text_surface.get_width()
            pygame.draw.line(screen, (255, 255, 255), 
                           (cursor_x, self.rect.y + 5), 
                           (cursor_x, self.rect.y + self.rect.height-5), 2)

    def set_text(self, text):
        self.text = text