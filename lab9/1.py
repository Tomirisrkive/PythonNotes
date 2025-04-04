import pygame, random

pygame.init()

# Терезе өлшемі
WIDTH, HEIGHT = 600, 600
CELL = 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake ойыны")

clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 24)
FPS = 5

# Түстер
BACKGROUND_COLOR = (30, 30, 30)        # Қою сұр
LIGHT_TILE = (170, 220, 255)           # Ашық көк
DARK_TILE = (100, 170, 220)            # Сәл қою көк
SNAKE_COLOR = (0, 255, 100)            # Жасыл
FOOD_COLOR = (255, 100, 100)           # Қызғылт
TEXT_COLOR = (0, 0, 0)           # Ақ

# Жылан мен тамақ
snake = [[5, 10], [4, 10], [3, 10]]
dx, dy = 1, 0

food = [random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1)]

score = 0
level = 1
running = True

while running:
    clock.tick(FPS)

    # Басқару
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and dx != -1:
                dx, dy = 1, 0
            if event.key == pygame.K_LEFT and dx != 1:
                dx, dy = -1, 0
            if event.key == pygame.K_UP and dy != 1:
                dx, dy = 0, -1
            if event.key == pygame.K_DOWN and dy != -1:
                dx, dy = 0, 1

    # Жаңа бас координаты
    new_head = [snake[0][0] + dx, snake[0][1] + dy]

    # Қабырғаға соғылса — өледі
    if new_head[0] < 0 or new_head[0] >= WIDTH // CELL or new_head[1] < 0 or new_head[1] >= HEIGHT // CELL:
        running = False
        break

    # Өзіне соғылса — өледі
    if new_head in snake:
        running = False
        break

    snake.insert(0, new_head)

    # Тағам жесе
    if new_head == food:
        score += 1
        if score % 5 == 0:
            level += 1
            FPS += 2
        while True:
            food = [random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1)]
            if food not in snake:
                break
    else:
        snake.pop()

    # Фон салу
    screen.fill(BACKGROUND_COLOR)
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            color = LIGHT_TILE if (i + j) % 2 == 0 else DARK_TILE
            pygame.draw.rect(screen, color, (j * CELL, i * CELL, CELL, CELL))

    # Жыланды салу
    for segment in snake:
        pygame.draw.rect(screen, SNAKE_COLOR, (segment[0]*CELL, segment[1]*CELL, CELL, CELL))

    # Тағам салу
    pygame.draw.rect(screen, FOOD_COLOR, (food[0]*CELL, food[1]*CELL, CELL, CELL))

    # Ұпай мен деңгей
    text_score = font.render(f"Ұпай: {score}", True, TEXT_COLOR)
    text_level = font.render(f'Деңгей: {level}', True, TEXT_COLOR)
    screen.blit(text_score, (10, 10))
    screen.blit(text_level, (WIDTH - 140, 10))

    pygame.display.flip()

# Ойын аяқталғанда
pygame.quit()
