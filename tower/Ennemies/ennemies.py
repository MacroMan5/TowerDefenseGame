import os
import pygame as pg
import math

# Constants for debug drawing
LINE_COLOR = (0, 255, 0)
TARGET_COLOR = (255, 0, 0)

class Ennemies(pg.sprite.Sprite):
    """
    A base class for enemy sprites in the game, providing common attributes and behaviors.
    
    Attributes:
        path (list): A list of tuples representing the points along which the enemy moves.
        path_index (int): The current index of the path the enemy is following.
        images (list): A list of pygame.Surface objects for animation frames.
        current_frame (int): The index of the current frame in the animation.
        image (pygame.Surface): The current image of the sprite.
        rect (pygame.Rect): The sprite's rectangle that defines its position and bounds.
        animation_speed (int): How fast the animation cycles through frames.
        frame_counter (int): A counter to manage animation timing.
        speed (int): The speed at which the enemy moves along its path.
        health (int): The health of the enemy.
        is_dying (bool): Whether the enemy is in the dying state.
    
    Methods:
        move_to(x, y): Moves the sprite towards a target position. Algorithm is
    """

    def __init__(self):
        super().__init__()
        self.path = []              # A list of tuples representing the points along which the enemy moves
        self.path_index = 0         # The current index of the path the enemy is following
        self.images = []            # This will be set by subclasses
        self.current_frame = 0      # Index of the current frame in the animation
        self.image = None           # This will be set by subclasses
        self.rect = None            # This will be defined when the image is set
        self.animation_speed = 10   # Adjust this as needed for smoother animation
        self.frame_counter = 0      # Counter to manage animation timing
        self.speed = 1              # Adjust this as needed for smoother movement
        self.health = 100           # adjust in subclasses as needed for different enemies 
        self.is_flipped = False     # Flip or not depending on the direction of the enemy
        self.is_dying = False       





    def move_to(self):
        """Move the sprite towards the next target position based on its speed,
        and proceed to the next target once reached, with a smooth arrival."""
        if self.path_index < len(self.path):
            target_x, target_y = self.path[self.path_index]
            center_x, center_y = self.rect.center  # Use center for both x and y

            dx = target_x - center_x
            dy = target_y - center_y
            distance = (dx ** 2 + dy ** 2) ** 0.5

            if distance > self.speed:
                # Normalize the direction vector
                dir_x, dir_y = dx / distance, dy / distance
                # Move towards the target
                self.rect.x += dir_x * self.speed
                self.rect.y += dir_y * self.speed
                # Determine if the image needs to be flipped
                self._is_moving_left(dir_x)

               
            else:
                # Snap to the target and move to the next one
                self.rect.center = (target_x, target_y)  # Update to use the center
                self.path_index += 1

            # Debug output
            #print(f"Moving to: {target_x}, {target_y} | Current pos: {self.rect.center}")

            if self.path_index >= len(self.path):
                self.is_dying = True



    def update(self):
        """
        Update the knight's animation and position along a path.
        """
        if not self.is_dying:
            self.animate(self.images)
            self.move_to()
        else:
            self.animate(self.dying_images)
            if self.current_frame == len(self.dying_images) - 1:  # Last frame of dying animation 
                self.kill()  # Remove the sprite after the animation finishes


    def animate(self, animation_images):
        """
        Handles the animation of the knight by cycling through a given list of images.
        Flip the image if the knight is moving to the left.

        Args:
            animation_images (list): A list of pygame.Surface objects for the animation frames.

        """
        # Increment the frame counter
        self.frame_counter += 1
        # Cycle through the animation images based on the animation speed
        if self.frame_counter >= self.animation_speed:
            self.current_frame = (self.current_frame + 1) % len(animation_images)
            self.image = animation_images[self.current_frame]
            # Flip the image based on the direction before setting it to the current image
            if self.is_flipped:
                self.image = pg.transform.flip(animation_images[self.current_frame], True, False)
            else:
                self.image = animation_images[self.current_frame]
            # Reset the frame counter
            self.frame_counter = 0
    def _is_moving_left(self, dir_x):
         # Determine if the image needs to be flipped
            moving_left = dir_x < 0
            if moving_left and not self.is_flipped:
                self.is_flipped = True
            elif not moving_left and self.is_flipped:
                self.is_flipped = False

    def die(self):
        """
        Handle the knight's death animation and remove it from the game once the animation is complete.
        """
        self.is_dying = True
        self.images = self.dying_images
        self.animation_speed = 8
        self.animate()  # Reuse the animate function for dying animation
        if self.current_frame == len(self.dying_images) - 1:
            self.kill()















        # def move_to(self, x, y):
    #     """Move the sprite towards a target position, based on its speed."""
    #     center_x = self.rect.x + self.rect.width / 2    
    #     center_y = self.rect.y + self.rect.height       
    #     dx = x - center_x   # Calculate the distance between the sprite's center and the target                          
    #     dy = y - center_y   # Calculate the distance between the sprite's center and the target

    #     distance = (dx ** 2 + dy ** 2) ** 0.5  # Pythagorean theorem to calculate the distance between two points           
    #     print(f"distance: {distance}")

    #     if distance > self.speed: # If the distance is greater than the sprite's speed, move the sprite towards the target
    #         self.rect.x += dx / distance * self.speed
    #         self.rect.y += dy / distance * self.speed
    #     else: # If the sprite is close enough to the target, adjust its position to align exactly with the target point 
    #         self.rect.x = x - self.rect.width / 2
    #         self.rect.y = y - self.rect.height

        

    # def follow_path(self):
    #     """Make the knight follow a predefined path."""
    #     if self.path_index < len(self.path) - 1:
    #         target = self.path[self.path_index]
    #         self.move_to(target[0], target[1])
            
    #         center_x = self.rect.x + self.rect.width / 2
    #         center_y = self.rect.y + self.rect.height
    #         if abs(center_x - target[0]) < self.speed and abs(center_y - target[1]) < self.speed:
    #             self.path_index += 1

    #         if self.path_index == len(self.path) - 1:
    #             self.is_dying = True
    #             self.animate(self.dying_images)  # Reuse the animate function for dying animation