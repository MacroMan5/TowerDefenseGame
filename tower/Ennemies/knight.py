import time
import os
import pygame as pg
from ennemies import Ennemies


class Knight(Ennemies):
    """
    A specific type of Enemy that represents a knight, with unique animations and behaviors.
    
    Inherits from Enemy, with additional attributes for dying animations and path-following behavior.
    """

    def __init__(self):
        super().__init__()
        self.path = [(101, 324),(149, 314),(165, 292),(252, 269),(387, 219),(467, 252),(743, 371),(700, 397),(506, 472),(507, 502),(717, 585),(713, 612),(476, 699),(482, 726),(797, 846),(927, 785),(1035, 747),(1159, 701),(1174, 662),(1274, 632)]   # A list of tuples representing the points along which the knight moves

        self.images = [pg.transform.scale(pg.image.load(os.path.join("tower", "assets", "chevalier", "Walk", f"Walk_{i}.png")), (65, 65)) for i in range(1, 11)]
        self.dying_images = [pg.transform.scale(pg.image.load(os.path.join("tower", "assets", "chevalier", "Dead", f"Dead_{i}.png")), (100, 100)) for i in range(1, 11)]
        self.current_frame = 0
        self.image = self.images[self.current_frame]  # Initial image
        self.rect = self.image.get_rect()
        self.rect.x = -10
        self.rect.y = 215
        self.animation_speed = 10
        self.frame_counter = 0
        self.speed = 1
        self.health = 100
        self.is_dying = False

    # def update(self):
    #     """
    #     Update the knight's animation and position along a path.
    #     """2,
    #     if not self.is_dying:
    #         self.animate(self.images)
    #         self.move_to()
    #     else:
    #         self.animate(self.dying_images)
    #         if self.current_frame == len(self.dying_images) - 1:  # Last frame of dying animation 
    #             self.kill()  # Remove the sprite after the animation finishes


    # def animate(self, animation_images):
    #     """
    #     Handles the animation of the knight by cycling through a given list of images.

    #     Args:
    #         animation_images (list): A list of pygame.Surface objects for the animation frames.

    #     """
    #     self.frame_counter += 1
    #     if self.frame_counter >= self.animation_speed:
    #         self.current_frame = (self.current_frame + 1) % len(animation_images)
    #         self.image = animation_images[self.current_frame]
    #         self.frame_counter = 0


    # def die(self):
    #     """
    #     Handle the knight's death animation and remove it from the game once the animation is complete.
    #     """
    #     self.is_dying = True
    #     self.images = self.dying_images
    #     self.animation_speed = 8
    #     self.animate()  # Reuse the animate function for dying animation
    #     if self.current_frame == len(self.dying_images) - 1:
    #         self.kill()

if __name__ == "__main__":
    # CONSTANTS 
    WIDTH, HEIGHT = 1280, 900
    FPS = 60


    pg.init()

    # Game setup
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()
    background = pg.Surface(screen.get_size())

    # Load background image
    background_image = pg.image.load(os.path.join("tower", "assets", "levels", "background.png"))
    background_image = pg.transform.scale(background_image, (WIDTH, HEIGHT))
 

    # Initialize a sprite group for all sprites 
    all_sprites = pg.sprite.Group()

    # Time tracking for sprite spawning
    last_spawn_time = 0
    spawn_interval = 1500  # 2000 milliseconds (2 seconds)
    stop_time = 30000  # 30000 milliseconds (30 seconds)

    # Game loop
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        

        # FUTURE WAVE FUNCTION here to spawn knights at different times
        # Get the current time in milliseconds  # Spawn a new knight if enough time has passed #
        current_time = pg.time.get_ticks()
        if current_time - last_spawn_time > spawn_interval and current_time < stop_time:
            last_spawn_time = current_time
            knight = Knight()
            all_sprites.add(knight)

        # # Update and draw everything
        all_sprites.update()
        screen.blit(background_image, (0, 0))    # Draw the background


        # #Debug: Draw lines for paths and rectangles around sprites
        # for sprite in all_sprites:
        #     if hasattr(sprite, 'path'):  # Check if sprite has a 'path' attribute
        #     # Assuming 'path' is a list of (x, y) tuples
        #         for i in sprite.path:
        #             pg.draw.circle(screen, (255, 0, 0), i , 5)  # Red circles along the path
        #     #Draw a rectangle around the sprite
        #     pg.draw.rect(screen, (0, 255, 0), sprite.rect, 2)  # Green rectangle around sprite

        if pg.mouse.get_pressed()[0]:
            print(pg.mouse.get_pos())


        all_sprites.draw(screen)                 # Draw the knights
        pg.display.flip()                        # Update the display
        clock.tick(FPS)                          # Maintain the frame rate
        # debug 
        
    pg.quit()

   