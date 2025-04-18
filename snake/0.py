import psycopg2
import pygame
import random

# Настройка подключения к базе данных PostgreSQL
conn = psycopg2.connect(
    dbname="tomiriszarylkasyn",  # Имя базы данных
    user="postgres",             # Имя пользователя
    password="123",              # Пароль
    host="localhost",            # Хост
    port="5432"                  # Порт
)
conn.autocommit = True

# Создание таблиц
create_user_table = """
CREATE TABLE IF NOT EXISTS "user" (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE
);
"""

create_user_score_table = """
CREATE TABLE IF NOT EXISTS user_score (
    score_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES "user"(user_id),
    score INT,
    level INT,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

# Создание таблиц в базе данных
cur = conn.cursor()
cur.execute(create_user_table)
cur.execute(create_user_score_table)

# Инициализация pygame
pygame.init()

# Размеры экрана
WIDTH, HEIGHT = 600, 600
CELL = 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 24)
FPS = 5

# Цвета
BACKGROUND_COLOR = (30, 30, 30)
LIGHT_TILE = (170, 220, 255)
DARK_TILE = (100, 170, 220)
SNAKE_COLOR = (0, 255, 100)
FOOD_COLOR = (255, 100, 100)
TEXT_COLOR = (0, 0, 0)

# Жылан мен тамақ
snake = [[5, 10], [4, 10], [3, 10]]
dx, dy = 1, 0

food = [random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1)]

score = 0
level = 1
running = True

# Ввод имени пользователя
username = input("Введите имя пользователя: ")
cur.execute('SELECT user_id FROM "user" WHERE username = %s', (username,))
user = cur.fetchone()

# Если пользователя нет, создаём нового
if user is None:
    cur.execute('INSERT INTO "user" (username) VALUES (%s) RETURNING user_id', (username,))
    user_id = cur.fetchone()[0]
    print(f"Новый пользователь {username} создан.")
else:
    user_id = user[0]
    print(f"Добро пожаловать, {username}!")

# Получаем текущий уровень пользователя
cur.execute('SELECT level FROM user_score WHERE user_id = %s ORDER BY date DESC LIMIT 1', (user_id,))
current_level = cur.fetchone()
if current_level:
    level = current_level[0]
    print(f"Текущий уровень: {level}")
else:
    print("Это ваш первый запуск игры.")

while running:
    clock.tick(FPS)

    # Управление
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and dx != -1:
                dx, dy = 1, 0
            if event.key == pygame.K_LEFT and dx != 1:
                dx, dy = -1, 0
            if event.key == pygame.K_UP and dy != 1:
                dx, dy = 0, -1
            if event.key == pygame.K_DOWN and dy != -1:
                dx, dy = 0, 1
            if event.key == pygame.K_p:  # Пауза игры
                print("Игра приостановлена. Сохраняем текущий прогресс...")
                cur.execute('INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)',
                            (user_id, score, level))
                conn.commit()
                print("Прогресс сохранён.")
                running = False  # Пауза завершена

    # Новая позиция головы змеи
    new_head = [snake[0][0] + dx, snake[0][1] + dy]

    # Проверка на столкновение с границами
    if new_head[0] < 0 or new_head[0] >= WIDTH // CELL or new_head[1] < 0 or new_head[1] >= HEIGHT // CELL:
        running = False
        break

    # Проверка на столкновение с телом змеи
    if new_head in snake:
        running = False
        break

    snake.insert(0, new_head)

    # Поедание пищи
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

    # Отображение фона
    screen.fill(BACKGROUND_COLOR)
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            color = LIGHT_TILE if (i + j) % 2 == 0 else DARK_TILE
            pygame.draw.rect(screen, color, (j * CELL, i * CELL, CELL, CELL))

   


    # Отображение змеи
    for segment in snake:
        pygame.draw.rect(screen, SNAKE_COLOR, (segment[0] * CELL, segment[1] * CELL, CELL, CELL))

    # Отображение еды
    pygame.draw.rect(screen, FOOD_COLOR, (food[0] * CELL, food[1] * CELL, CELL, CELL))

    # Отображение счета и уровня
    text_score = font.render(f"Score: {score}", True, TEXT_COLOR)
    text_level = font.render(f'Level: {level}', True, TEXT_COLOR)
    screen.blit(text_score, (10, 10))
    screen.blit(text_level, (WIDTH - 140, 10))

    pygame.display.flip()

# Сохранение результатов в базе данных при завершении игры
cur.execute('INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)',
            (user_id, score, level))
conn.commit()

pygame.quit()
cur.close()
conn.close()
