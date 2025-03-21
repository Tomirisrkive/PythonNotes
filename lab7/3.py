import pygame
pygame.init()

width = 1000
height = 1000
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()  # Таймер для управления FPS
color_white = (255, 255, 255)  
x_coord_circle = 100  # Н.п по X
y_coord_circle = 40  # Н.п по Y
running = True  # Переменная для основного цикла

while running:
    screen.fill(color_white)  # Заполняем экран белым цветом
    # Рисуем круг
    my_circle = pygame.draw.circle(screen, 'red', (x_coord_circle, y_coord_circle), 25)

    for event in pygame.event.get():  # Обрабатываем события
        if event.type == pygame.QUIT:  # Закрытие окна
            running = False
        if event.type == pygame.KEYDOWN:  # Обработка нажатия клавиш
            if event.key == pygame.K_UP:  # Перемещение вверх
                y_coord_circle -= 20
            if event.key == pygame.K_DOWN:  # Перемещение вниз
                y_coord_circle += 20
            if event.key == pygame.K_LEFT:  # Перемещение влево
                x_coord_circle -= 20
            if event.key == pygame.K_RIGHT:  # Перемещение вправо
                x_coord_circle += 20

            # Ограничиваем движение круга по экрану
            if x_coord_circle < 40:
                x_coord_circle = 40  # Не даем выходить за левый край
            if y_coord_circle < 40:
                y_coord_circle = 40  # Не даем выходить за верхний край
            if x_coord_circle > 960:
                x_coord_circle = 960  # Не даем выходить за правый край
            if y_coord_circle > 960:
                y_coord_circle = 960  # Не даем выходить за нижний край

    pygame.display.flip()  
    clock.tick(60) 
