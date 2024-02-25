from pygame import *
from random import randint

# ! Основные переменные для проекта
FPS = 60
GAME_FINISHED, GAME_RUN = False, True
WINDOW_WIDTH, WINDOW_HEIGHT = 640, 480
CLOCK = time.Clock()

# ! Создание окна игры
WINDOW = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display.set_caption("Maze (Labyrinth (Лабиринт))")

# ! Звуки
mixer.init()

mixer.music.load("music.mp3")
mixer.music.play()

# ! Текст
font.init()

num_walls=randint(10,25)
font1 = font.SysFont("Arial", 72, True)

win_text = font1.render("Ты победил!", True, (0, 128, 0))
lose_text = font1.render("Ты проиграл!", True, (255, 0, 0))

# ! Классы
class GameSprite(sprite.Sprite):
    def __init__(self, img, position, size, speed):
        super().__init__()
        
        self.image = transform.smoothscale(
            image.load(img),
            size
        )
        
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        
        self.speed = speed
        self.width, self.height = size
        
    def reset(self):
        WINDOW.blit(self.image, (self.rect.x, self.rect.y))
        
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < WINDOW_HEIGHT - self.height:
            self.rect.y += self.speed
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < WINDOW_WIDTH - self.width:
            self.rect.x += self.speed
    
class Enemy(GameSprite):
    def __init__(self, img, position, size, speed):
        super().__init__(img, position, size, speed)
        
        self.direction_x, self.direction_y = "RIGHT", "TOP"
        self.start_x, self.end_x = None, None
        self.start_y, self.end_y = None, None
    
    def set_track_x(self, start_x, end_x):
        self.start_x, self.end_x = start_x, end_x
    
    def set_track_y(self, start_y, end_y):
        self.start_y, self.end_y = start_y, end_y
    
    def update(self):
        # ! Движение по Х
        if self.start_x != None and self.end_x != None:
            if self.direction_x == "RIGHT":
                if self.rect.x < self.end_x:  
                    self.rect.x += self.speed
                else: 
                    self.direction_x = "LEFT"
            else: 
                if self.rect.x > self.start_x:
                    self.rect.x -= self.speed
                else: 
                    self.direction_x = "RIGHT"
        
        # ! Движение по У
        if self.start_y != None and self.end_y != None:
            if self.direction_y == "TOP":
                if self.rect.y < self.end_y:  
                    self.rect.y += self.speed
                else:
                    self.direction_y = "BOTTOM"
            else: 
                if self.rect.y > self.start_y: 
                    self.rect.y -= self.speed
                else:
                    self.direction_y = "TOP"
    
class Wall(sprite.Sprite):
    def __init__(self, position, size, color):
        super().__init__()
        
        self.image = Surface(size)
        self.image.fill(color)
        
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        
        self.width, self.height = size
        
    def draw(self):
        WINDOW.blit(self.image, (self.rect.x, self.rect.y))

    def draw(self):
        WINDOW.blit(self.image, (self.rect.x, self.rect.y))

class Treasure(GameSprite):
    def __init__(self, img, position, size, speed):
        super().__init__(img, position, size, speed)
    
bg = GameSprite(img="bg.jpg",
                position=(0, 0),
                size=(WINDOW_WIDTH, WINDOW_HEIGHT),
                speed=0)

player = Player(img="player.jpg",
                position=(0, 0),
                size=(24, 48),
                speed=5)

enemy1 = Enemy(img="enemy.jpg",
               position=(400, 400),
               size=(24, 48),
               speed=5)

treasure = Treasure(img="treasure.jpg",
               position=(400, 400),
               size=(48, 48),
               speed=0)


enemy2 = Enemy(img="enemy.jpg",
               position=(400, 200),
               size=(24, 48),
               speed=5)

enemy_group = sprite.Group()
enemy_group.add([enemy1, enemy2])
"""
wall1 = Wall(position=(0, 50),
             size=(100, 24),
             color=(100, 100, 100))

wall2 = Wall(position=(100, 250),
             size=(24, 100),
             color=(100, 100, 100))

wall3 = Wall(position=(100, 400),
             size=(24, 24),
             color=(100, 100, 100))

wall4 = Wall(position=(400, 100),
             size=(100, 24),
             color=(100, 100, 100))

wall5 = Wall(position=(300, 250),
             size=(24, 100),
             color=(100, 100, 100))

wall6 = Wall(position=(200, 400),
             size=(24, 24),
             color=(100, 100, 100))

wall7 = Wall(position=(500, 100),
             size=(100, 24),
             color=(100, 100, 100))

wall8 = Wall(position=(600, 250),
             size=(24, 100),
             color=(100, 100, 100))

wall9 = Wall(position=(500, 400),
             size=(24, 24),
             color=(100, 100, 100))

wall10 = Wall(position=(100, 100),
             size=(100, 24),
             color=(100, 100, 100))

wall11 = Wall(position=(100, 250),
             size=(24, 100),
             color=(100, 100, 100))

wall12 = Wall(position=(100, 400),
             size=(24, 24),
             color=(100, 100, 100))

wall13 = Wall(position=(400, 100),
             size=(100, 24),
             color=(100, 100, 100))

wall14 = Wall(position=(300, 250),
             size=(24, 100),
             color=(100, 100, 100))

wall15 = Wall(position=(200, 400),
             size=(24, 24),
             color=(100, 100, 100))

wall16 = Wall(position=(500, 100),
             size=(100, 24),
             color=(100, 100, 100))

wall17 = Wall(position=(600, 250),
             size=(24, 100),
             color=(100, 100, 100))

wall18 = Wall(position=(500, 400),
             size=(24, 24),
             color=(100, 100, 100))
"""
walls_group = sprite.Group()
a=200
b=5

enemy_trackx1=randint(0,640)
enemy_trackx2=randint(0,640)
enemy_tracky1=randint(0,480)
enemy_tracky2=randint(0,480)

for _ in range(num_walls):
   
    x = randint(0, WINDOW_WIDTH - 100)  
    y = randint(0, WINDOW_HEIGHT - 100)  
    width = randint(1, 100) 
    height = randint(1, 100)  
    
    
    wall = Wall(position=(x, y), size=(width, height), color=(100, 100, 100))
    walls_group.add(wall)

# ! Игровой цикл
while GAME_RUN:
    
    for ev in event.get():
        if ev.type == QUIT:
            GAME_RUN = False  
    # ? Отрисовка
    bg.reset()
    player.reset()
    treasure.reset()
    enemy_group.draw(WINDOW)
    walls_group.draw(WINDOW)
    

    enemy1.set_track_x(enemy_trackx1, enemy_trackx2)
    enemy1.set_track_y(enemy_tracky1, enemy_tracky2)
    # ? 1. sprite.collide_rect : спрайт - спрайт
    # ? 2. sprite.spritecollide : спрайт - группа
    # ? 3. sprite.groupcollide : группа - группа
            
    if sprite.spritecollide(player, enemy_group, False):
        WINDOW.blit(lose_text, (WINDOW_WIDTH / 2 - lose_text.get_width() / 2, 
                                WINDOW_HEIGHT / 2 - lose_text.get_height() / 2))
        GAME_FINISHED = True
        
    if sprite.spritecollide(player, walls_group, False):
        WINDOW.blit(lose_text, (WINDOW_WIDTH / 2 - lose_text.get_width() / 2, 
                                WINDOW_HEIGHT / 2 - lose_text.get_height() / 2))
        GAME_FINISHED = True

    if sprite.collide_rect(player, treasure):
        WINDOW.blit(win_text, (WINDOW_WIDTH / 2 - lose_text.get_width() / 2, 
                                WINDOW_HEIGHT / 2 - lose_text.get_height() / 2))
        GAME_FINISHED = True
    
    # ? Логика игры (работает пока не проиграем/выиграем)
    if not GAME_FINISHED:
        player.update()
        enemy_group.update()
        treasure.update()
        for _ in range(b):
            if a == 0:
                enemy_trackx1=randint(0,640)
                enemy_trackx2=randint(0,640)
                enemy_tracky1=randint(0,480)
                enemy_tracky2=randint(0,480)
                a=200
                b=5
            else:
                a-=1
    display.update()
    CLOCK.tick(FPS)



