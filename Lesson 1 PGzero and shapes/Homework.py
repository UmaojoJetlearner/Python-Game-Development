import pgzrun
import pygame

WIDTH = 400
HEIGHT = 400

def draw():
    
    screen.fill("white")
    
    # Head
    screen.draw.filled_circle((200, 200), 100, "yellow")
    screen.draw.circle((200, 200), 100, "black") 
    
    # Eyes
    screen.draw.filled_circle((165, 170), 12, "black")
    screen.draw.filled_circle((235, 170), 12, "black")
    
    mouth_rect = pygame.Rect(150, 210, 100, 50)
    
    pygame.draw.arc(screen.surface, (0, 0, 0), mouth_rect, 3.14, 0, 3)

pgzrun.go()