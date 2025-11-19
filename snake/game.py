#find a way to make the snake faster

# Example file showing a basic pygame "game loop"
import pygame
import random

# pygame setup
pygame.init()
pygame.mixer.init()
LENGTH = 800
HIGHT = 600
screen = pygame.display.set_mode((LENGTH, HIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
running = True
direction = "up"
GRADE = 20
points = 0
gameover = False

#load sounds
es = pygame.mixer.Sound("sounds/efs.mp3")
gos = pygame.mixer.Sound("sounds/gos.mp3")
bm = pygame.mixer.Sound("sounds/bgm.mp3")
bm.set_volume(0.5)
bm.play(-1)
pgos = False

#random position
def create_randm_position():
    x = random.randrange(0,LENGTH -20,GRADE)
    y = random.randrange(0,HIGHT -20,GRADE)
    return x,y

#snake setup
snake_x, snake_y =  create_randm_position()
print(f"snake {snake_x} and {snake_y}")
snake = [pygame.Rect(snake_x,snake_y,GRADE ,GRADE)]
snake_color = "blue"
wait_time = 175
last_movement = 0


#food setup
food_x, food_y =  create_randm_position()
print(f"food {food_x} and {food_y}")
food = pygame.Rect(food_x,food_y,GRADE,GRADE)
food_color = "red"

#text setup
gameovercolor = "black"
pointscolor = "black"
gameoverfont = pygame.font.SysFont("franklingothicmedium",150)
pointsfont = pygame.font.SysFont("comicsansms",20)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "down":
                direction = "up" 
            elif event.key == pygame.K_DOWN and direction != "up":
                direction = "down" 
            elif event.key == pygame.K_RIGHT and direction != "left":
                direction = "right" 
            elif event.key == pygame.K_LEFT and direction != "right":
                direction = "left" 

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("dark orange")

    # snake movement
    time = pygame.time.get_ticks()
    if time - last_movement >= wait_time and not gameover:
        newpart = snake[0].copy()
        if direction == "up":
            newpart.y -= GRADE
        elif direction == "down":
            newpart.y += GRADE
        elif direction == "left":
            newpart.x -= GRADE
        elif direction == "right":
            newpart.x += GRADE
        last_movement = time

        snake.insert(0,newpart)

        #collide 
        if snake[0].colliderect(food):
            food_x, food_y =  create_randm_position()
            print(f"food {food_x} and {food_y}")
            food.update(food_x,food_y,GRADE,GRADE)
            points = points + 1
            print(f"you have {points} points")
            es.play()
        else:
            snake.pop()

        if(snake[0].x <0 or snake[0].x > LENGTH or snake[0].y <0 or snake[0].y > HIGHT):
            gameover = True
            pgos = True
            if pgos:
                gos.play()
                pgos = False

        for part in snake [1:]:
            if newpart.colliderect(part):
                gameover = True
                pgos = True
                if pgos:
                    gos.play()
                    pgos = False




        if points == 5:
            wait_time = 150
        elif points == 10:
            wait_time = 100
        elif points == 15:
            wait_time = 50
        elif points == 20:
            wait_time = 25
        elif points == 30:
            wait_time = 50
        elif points == 35:
            wait_time = 150
        elif points == 40:
            wait_time = 1
        

    

    # RENDER YOUR GAME HERE
    for part in snake:
        pygame.draw.rect(screen,snake_color,part)
    pygame.draw.rect(screen,food_color,food)
    pointstext = pointsfont.render(f"you have {points} points", True, pointscolor)
    screen.blit(pointstext,(10,10))

    if gameover:
        gameovertext = gameoverfont.render(f"GAME  OVER", True, gameovercolor)
        textrect = gameovertext.get_rect(center = (LENGTH // 2, HIGHT // 2))
        screen.blit(gameovertext,textrect)
        bm.stop()





    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()