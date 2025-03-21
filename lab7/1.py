import pygame 
from datetime import datetime

pygame.init()

width = 1000
height = 1000
COLOR_WHITE = (255,255,255)
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Clock Mickey')

mickeys_body = pygame.image.load('/Users/tomiriszarylkasyn/Documents/labpp2/labs/lab7/images/clock.png').convert_alpha()
mickeys_right_hand = pygame.image.load('/Users/tomiriszarylkasyn/Documents/labpp2/labs/lab7/images/rightarm.png').convert_alpha()
mickeys_left_hand = pygame.image.load('/Users/tomiriszarylkasyn/Documents/labpp2/labs/lab7/images/leftarm.png').convert_alpha()

# Уменьшаем размер рук (50% от исходного размера)
scaled_mickeys_right_hand = pygame.transform.scale(mickeys_right_hand, (mickeys_right_hand.get_width() // 2, mickeys_right_hand.get_height() // 2))
scaled_mickeys_left_hand = pygame.transform.scale(mickeys_left_hand, (mickeys_left_hand.get_width() // 2, mickeys_left_hand.get_height() // 2))

mickeys_body_rect = mickeys_body.get_rect(center = (width//2,height//2))

clock = pygame.time.Clock()
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    # Update time
    now = datetime.now()
    minutes = now.minute
    seconds = now.second

    screen.fill(COLOR_WHITE)
    min_angle = minutes * 6 + seconds * 0.1 
    sec_angle = seconds * 6 

    # MINUTE 
    rotated_mickeys_right_hand = pygame.transform.rotate(scaled_mickeys_right_hand, -min_angle - 90)
    rotated_mickeys_right_hand_rect = rotated_mickeys_right_hand.get_rect(center = (width//2,height//2))

    # SECOND 
    rotated_mickeys_left_hand = pygame.transform.rotate(scaled_mickeys_left_hand, -sec_angle - 90)
    rotated_mickeys_left_hand_rect = rotated_mickeys_left_hand.get_rect(center = (width//2,height//2))

    screen.blit(mickeys_body, mickeys_body_rect)
    screen.blit(rotated_mickeys_right_hand, rotated_mickeys_right_hand_rect)
    screen.blit(rotated_mickeys_left_hand, rotated_mickeys_left_hand_rect)

    pygame.display.flip()
    clock.tick(60)
