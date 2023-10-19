#создай игру "Лабиринт"!
from pygame import *

mixer.init()
font.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

finish = False
clock = time.Clock()
window = display.set_mode((700, 500))
display.set_caption('Догонялки')
background = transform.scale(image.load('background.jpg'), (700, 500))


class GameSprite(sprite.Sprite):
    def __init__(self, p_image, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(p_image), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Wall(sprite.Sprite):
    def __init__(self, wall_width, wall_height, wall_x, wall_y):
        super().__init__()
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed

        if keys_pressed[K_d] and self.rect.x < 630:
            self.rect.x += self.speed

        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys_pressed[K_s] and self.rect.y < 430:
            self.rect.y += self.speed
        

class Enemy(GameSprite):
    def update(self):
            if self.rect.y == 350:
                self.rect.x += self.speed
            if self.rect.x > 350:
                self.rect.y += self.speed
            if self.rect.y == 360:
                self.rect.x -= self.speed
            if self.rect.x < 260:
                self.rect.y -= self.speed

    






sprite1 = Player('hero.png',20, 250, 5)
sprite2 = Enemy('cyborg.png',280, 350, 2)
final = GameSprite('treasure.png',500, 350, 0)
wall1 = Wall(13, 380, 100, 10)
wall2 = Wall(500, 13, 100, 10)
wall3 = Wall(13, 380, 400, 10)
wall4 = Wall(500, 13, 100, 460)
wall5 = Wall(13, 380, 250, 80)
font = font.Font(None, 70)
false = font.render('GAME OVER', True, (255, 0, 0))
win = font.render('YOU WIN', True, (0, 255, 0))




game = True
while game:
    if finish != True:
        window.blit(background,(0, 0))
        sprite1.reset()
        sprite2.reset()
        sprite1.update()
        sprite2.update()
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        final.reset()

        if sprite.collide_rect(sprite1, final):
            finish = True
            money.play()
            window.blit(win, (200,200))
        
        if sprite.collide_rect(sprite1, sprite2):
            finish = True
            kick.play()
            window.blit(false, (200,200))
            
        
        if sprite.collide_rect(sprite1, wall1):
            finish = True
            kick.play()
            window.blit(false, (200,200))
        
        if sprite.collide_rect(sprite1, wall2):
            finish = True
            kick.play()
            window.blit(false, (200,200))
        
        if sprite.collide_rect(sprite1, wall3):
            finish = True
            kick.play()
            window.blit(false, (200,200))
        
        if sprite.collide_rect(sprite1, wall4):
            finish = True
            kick.play()
            window.blit(false, (200,200))
        
        if sprite.collide_rect(sprite1, wall5):
            finish = True
            kick.play()
            window.blit(false, (200,200))
        

    for e in event.get():
        if e.type == QUIT:
            game = False
    
    clock.tick(60)
    display.update()