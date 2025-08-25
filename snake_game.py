import pygame, random, sys


pygame.init()
width, height = 600, 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game 🐍")
clock = pygame.time.Clock()


black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)


snake = [[100, 50]]
snake_change_x, snake_change_y = 10, 0
food_position = [200, 150]
score = 0


font = pygame.font.SysFont("Arial", 24)



def show_text(text, color, x, y):
    label = font.render(text, True, color)
    window.blit(label, (x, y))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_change_y == 0:
                snake_change_x, snake_change_y = 0, -10
            if event.key == pygame.K_DOWN and snake_change_y == 0:
                snake_change_x, snake_change_y = 0, 10
            if event.key == pygame.K_LEFT and snake_change_x == 0:
                snake_change_x, snake_change_y = -10, 0
            if event.key == pygame.K_RIGHT and snake_change_x == 0:
                snake_change_x, snake_change_y = 10, 0

    
    head = [snake[0][0] + snake_change_x, snake[0][1] + snake_change_y]
    snake.insert(0, head)

    if head == food_position:
        food_position = [random.randrange(0, width, 10), random.randrange(0, height, 10)]
        score += 1
    else:
        snake.pop()


    if (
        head in snake[1:]
        or head[0] < 0 or head[1] < 0
        or head[0] >= width or head[1] >= height
    ):
        window.fill(black)
        show_text("Game Over! Final Score: " + str(score), red, width//4, height//2)
        pygame.display.flip()
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()


    window.fill(black)
    for block in snake:
        pygame.draw.rect(window, green, (block[0], block[1], 10, 10))
    pygame.draw.rect(window, red, (food_position[0], food_position[1], 10, 10))

    show_text("Score: " + str(score), white, 10, 10)

    pygame.display.flip()
    clock.tick(7)
