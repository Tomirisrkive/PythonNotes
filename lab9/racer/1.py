import pygame
from pygame.locals import *
import random
import sys
import os

# Инициализация
pygame.init()

# Путь к домашнему каталогу пользователя
user_home = os.path.expanduser("~")

# Түстер
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)

# Экран өлшемі
screen_width = 400
screen_height = 600
displaysurf = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("F1 Tomka Game")

# Машиналар үшін суреттерді жүктеу
player_img = pygame.image.load(os.path.join(user_home, "Documents", "labpp2", "labs", "lab8", "picture", "IMG_9082 4.jpg"))  # ойыншының машинасының суреті
enemy_img = pygame.image.load(os.path.join(user_home, "Documents", "labpp2", "labs", "lab8", "picture", "IMG_9082 2.jpg"))  # қарсыластың машинасының суреті

pygame.mixer.init()  # Музыка жүйесін қосу

# Музыканың жолы
music_path = os.path.join(user_home, "Downloads", "Fleetwood Mac - The Chain - 2004 Remaster.mp3")

# Музыканы жүктеу және ойнау
pygame.mixer.music.load(music_path)
pygame.mixer.music.play(-1)  # -1 = қайталанып ойнатылады

# Машиналар өлшемі
player_width = 50
player_height = 100
enemy_width = 50
enemy_height = 100



# Изменяем размер изображений
player_img = pygame.transform.scale(player_img, (player_width, player_height))
enemy_img = pygame.transform.scale(enemy_img, (enemy_width, enemy_height))

# Ойыншы және қарсылас
player = pygame.Rect(200, 500, player_width, player_height)
enemy = pygame.Rect(random.randint(0, 350), 0, enemy_width, enemy_height)
enemy_speed = 5

# Шрифт және ұпайлар
font = pygame.font.SysFont("Verdana", 20)
score = 0

# FPS (кадр жиілігі)
FPS = pygame.time.Clock()

# Game Over функциясы
def game_over():
    pygame.mixer.music.stop()
    go_font = pygame.font.SysFont("Verdana", 40)
    go_surf = go_font.render("Game Over", True, red)
    go_rect = go_surf.get_rect(center=(screen_width // 2, screen_height // 2))
    displaysurf.blit(go_surf, go_rect)
    pygame.display.update()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

# Негізгі ойын циклы
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Ойыншының қозғалысы
    keys = pygame.key.get_pressed()
    if keys[K_LEFT] and player.left > 0:
        player.move_ip(-5, 0)
    if keys[K_RIGHT] and player.right < screen_width:
        player.move_ip(5, 0)

    # Қарсыластың қозғалысы
    enemy.move_ip(0, enemy_speed)
    if enemy.top > screen_height:
        enemy.top = 0
        enemy.left = random.randint(0, screen_width - enemy.width)
        score += 1  # Ұпайлар қосылады

    # Столкновение тексерісі
    if player.colliderect(enemy):
        game_over()

    # Экранды жаңарту
    displaysurf.fill(white)  # Экранды таза қылу
    displaysurf.blit(player_img, player)  # Ойыншыны көрсету
    displaysurf.blit(enemy_img, enemy)  # Қарсыласты көрсету

    # Ұпайларды көрсету
    score_text = font.render("Score: " + str(score), True, black)
    displaysurf.blit(score_text, (10, 10))

    pygame.display.update()
    FPS.tick(60)

pygame.quit() 