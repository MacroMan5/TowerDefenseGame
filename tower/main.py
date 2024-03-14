import pygame as pg
import os
from Game.game import Game

# CONSTANTS 
WIDTH, HEIGHT = 1280, 900
FPS = 60
# game loop 

towerDefense = Game(WIDTH,HEIGHT)   
towerDefense.run()