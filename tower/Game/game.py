import pygame as pg 
import os
import time



# CONSTANTS 
WIDTH, HEIGHT = 900, 600
FPS = 60




#C:\Users\Therouxe\Desktop\TowerDefenseGame\tower\assets\chevalier\Walk\Walk (1).png

class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.win = pg.display.set_mode((WIDTH,HEIGHT))
        self.enemies = []
        self.towers = []
        self.rounds = 0
        self.lives = 10
        self.money = 100
        self.nameDisplay = pg.display.set_caption("Tower Defense")
        #self.bg = pg.image.load(os.path.join("", ""))
        #self.bg = pg.transform.scale(self.bg, (WIDTH, HEIGHT))
        self.clicks = []



    def run(self):
        run = True
        clock = pg.time.Clock()
        while run:
            clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
        self.draw_window()
        pg.quit()

    def create_enemy(self):
        pass
        

    def draw(self, img):
        pass
      

    def draw_window(self):
        self.win.fill((255,255,255))



    def create_tower(self, x, y):
        pass
    def sell_tower(self, x, y):
        pass

    def increase_round(self):
        pass

    def reset_game(self):
        pass

    def generate_enemy(self):
        pass
    
    def collision(self, x, y):
        pass



import pygame as pg
import os

pg.init()

# Constants
WIDTH, HEIGHT = 1280, 900
FPS = 60


class Knight(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.path = [
                        (18, 287),(115, 330),(384, 222),(547, 286),(730, 350),(728, 386),(500, 466),(502, 503),(705, 577),(724, 608),(462, 713),(618, 776),(792, 845),(1030, 742),(1168, 688),(1273, 631)
                                    ]
        self.path_index = 0
        self.images = [pg.transform.scale(pg.image.load(os.path.join("tower", "assets", "chevalier", "Walk", f"Walk_{i}.png")), (75, 75)) for i in range(1, 11)]
        self.dying_images = [pg.transform.scale(pg.image.load(os.path.join("tower", "assets", "chevalier", "Dead", f"Dead_{i}.png")), (75, 75)) for i in range(1, 11)]
        self.current_frame = 0
        self.image = self.images[self.current_frame]  # Initial image
        self.rect = self.image.get_rect()
        self.rect.x = -10
        self.rect.y = 215
        self.animation_speed = 10
        self.frame_counter = 0
        self.speed = 1  # Adjust this as needed for smoother movement
        self.health = 100
        self.is_dying = False

    def update(self):
        # Animation
        self.frame_counter += 1
        if self.frame_counter >= self.animation_speed:
            self.current_frame = (self.current_frame + 1) % len(self.images)
            self.image = self.images[self.current_frame]
            self.frame_counter = 0
        
        # Dying
        # if self.is_dying:
        #     self.die()
    
    def follow_path(self):
        if self.path_index < len(self.path) - 1:
            target = self.path[self.path_index]
            self.move_to(target[0], target[1])
            
            # Calculate the center bottom of the knight's rect for accurate path following
            center_x = self.rect.x + self.rect.width / 2
            center_y = self.rect.y + self.rect.height 
            
            # Adjust the condition to check if the center bottom has reached the target
            if abs(center_x - target[0]) < self.speed and abs(center_y - target[1]) < self.speed:
                self.path_index += 1  # Move to the next point
        
    
    def move_to(self, x, y):
        # Calculate the center botton of the knight rect 
        center_x = self.rect.x + self.rect.width / 2
        center_y = self.rect.y + self.rect.height 

        dx = x - center_x
        dy = y - center_y
        distance = (dx ** 2 + dy ** 2) ** 0.5 # Pythagorean theorem to calculate the distance between two points 

        if distance > self.speed:
            # Update the sprite's position based on its center bottom
            self.rect.x += dx / distance * self.speed
            self.rect.y += dy / distance * self.speed
        else:
            # When the sprite is close enough to the target, adjust its position to align exactly
            # This adjustment is to ensure the center bottom of the sprite aligns with the target point
            self.rect.x = x - self.rect.width / 2
            self.rect.y = y - self.rect.height 
        

            
    def die(self):
        self.is_dying = True
        self.images = self.dying_images
        self.animation_speed = 15
        if self.current_frame == 9:
            time.sleep(0.4)
            self.kill()

    def print_mouse_pos(self):
        print(pg.mouse.get_pos())
    






# Game setup
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
background = pg.Surface(screen.get_size())


# Load background image
background_image = pg.image.load(os.path.join("tower", "assets", "levels", "background.png"))
background_image = pg.transform.scale(background_image, (WIDTH, HEIGHT))


all_sprites = pg.sprite.Group()
knight = Knight()
all_sprites.add(knight)

# Game loop
running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            print(pg.mouse.get_pos())

    screen.blit(background_image, (0, 0))
    # Update
    all_sprites.update()
    # move the knight along the path
    knight.follow_path()
    #pg.draw.rect(screen, (255, 0, 0), (knight.rect.x, knight.rect.y, 100, 100))

    # Draw line path (for testing)
    #pg.draw.lines(screen, (255, 0, 0), False, knight.path, 2)
    # Draw / render
    all_sprites.draw(screen)
   
    # After drawing everything, flip the display
    pg.display.flip()

pg.quit()

