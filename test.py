from pygame_widgets.textbox import *
from pygame import *
font.init()

font2 = font.Font(None,70)
text12 = True
text = False



def output():
    global text12
    global text
    text12 = False
    text = True


    


pygame.init()
win = pygame.display.set_mode((1000, 600))

textbox = TextBox(win, 100, 100, 800, 80, fontSize=50,
                  borderColour=(255, 0, 0), textColour=(0, 200, 0),
                  onSubmit=output, radius=10, borderThickness=5)
            
textbox2 = TextBox(win, 100, 200, 800, 80,onSubmit=output2,fontSize=50)     


clock = time.Clock()
run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()

    win.fill((255, 255, 255))
    
    score2 = font2.render(str(textbox.getText()),True,(0,0,0))
    win.blit(score2, (10,40))

    if text12:
        textbox2.hide()
        pygame_widgets.update(events)
    if text:
        textbox.hide()
        textbox2.show()
        pygame_widgets.update(events)
    
    pygame.display.update()
    clock.tick(50)
