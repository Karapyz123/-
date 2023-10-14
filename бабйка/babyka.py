import pygame  
pygame.init()  
  
back = (200,255,255)#колір фону (background)  
mw = pygame.display.set_mode((500,500))#Вікно програми (main window)  
mw.fill(back)  
clock = pygame.time.Clock()  
  
#прапорці, які відповідають за рух платформи вправо/ліворуч  
move_right =False  
move_left =False  
#прапор закінчення гри  
game_over =False  
#змінні, відповідальні за напрями переміщення м'яча  
dx =3  
dy =3  
  
class Area():  
    def __init__(self, x=0, y=0, width =10, height =10, color=None):  
        self.rect = pygame.Rect(x, y, width, height)  
        self.fill_color = back  
        if color:  
            self.fill_color = color  
    def color(self, new_color):  
        self.fill_color = new_color  
    def fill(self):  
        pygame.draw.rect(mw,self.fill_color,self.rect)  
    def collidepoint(self, x, y):  
        return self.rect.collidepoint(x, y)  
    def colliderect(self, rect):  
        return self.rect.colliderect(rect)  
#клас для об'єктів-картинок  
class Picture(Area):  
    def __init__(self, filename, x=0, y=0, width =10, height =10):  
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)  
        self.image = pygame.image.load(filename)  
  
    def draw(self):  
        mw.blit(self.image, (self.rect.x,self.rect.y))  
 
class Label(Area): 
    def set_text(self, text, fsize =12, text_color=(0,0,0)): 
        self.image = pygame.font.SysFont('verdana', fsize).render(text,True, text_color) 
 
    def draw(self, shift_x=0, shift_y=0): 
        self.fill() 
        mw.blit(self.image, (self.rect.x + shift_x,self.rect.y + shift_y)) 
 
  
racket_x =200 #координати платформи  
racket_y =330  
  
ball = Picture("Coat_of_Arms_Enerhodar (2).png",160,200,50,50)  
platform = Picture("platform.png",racket_x,racket_y,100,30)  
  
start_x = 5  
start_y = 5  
count = 9  
monsters = []  
for j in range(3):  
    x = start_x + (27.5 * j)  
    y = start_y + (55 * j)  
    for i in range (count):  
        d = Picture ("борщ (1).png", x , y, 50, 50)  
        monsters.append(d)  
        x = x + 55  
    count = count -1  
  
while not game_over:  
    ball.fill()  
    platform.fill()  
  
    for event in pygame.event.get():  
        if event.type== pygame.QUIT:  
            game_over =True  
        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_RIGHT:  
                move_right = True  
            if event.key == pygame.K_LEFT:  
                move_left = True  
        elif event.type== pygame.KEYUP:  
            if event.key == pygame.K_RIGHT:  
                move_right =False  
            if event.key == pygame.K_LEFT:  
                move_left =False  
  
    if move_right == True:#прапор руху вправо  
        platform.rect.x +=3  
    if move_left:#прапор руху вліво  
        platform.rect.x -=3  
  
    ball.rect.x += dx  
    ball.rect.y += dy  
  
    if ball.rect.x > 450 or ball.rect.x < 0:  
        dx *= -1  
    if ball.rect.y < 0:  
        dy *= -1  
  
    if ball.colliderect(platform.rect):  
        dy *= -1  
  
  
    ball.fill()  
    platform.fill()  
  
    for enemy in monsters:  
        enemy.draw() 
        if enemy.rect.colliderect(ball.rect): 
            monsters.remove(enemy) 
            enemy.fill() 
            dy *= -1  
     
    if ball.rect.y > 350: 
        time_text = Label(150,170,50,50,back) 
        time_text.set_text("Ти програв",60, (255,0,0)) 
        time_text.draw(0,0) 
        game_over = True 
     
    if len(monsters) == 0: 
        time_text = Label(150,170,50,50,back) 
        time_text.set_text("Ти виграв",60, (0,255,0)) 
        time_text.draw(0,0) 
        game_over = True 
  
    platform.draw()  
    ball.draw()  
    pygame.display.update()  
    clock.tick(40)