# install pygame, used to create video games as it consists of computer graphics

import pygame

# initialize pygame module
pygame.init()

# creating colors using constants, constants are written in all capital letters
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
GREEN = (0, 255, 0)

# creating bricks(rectangular shapes)
# creating rectangle using pygame RECT class, it represents rectangle
brick1=[pygame.Rect(10+i*100,60,80,30) for i in range(6)]
brick2=[pygame.Rect(10+i*100,100,80,30) for i in range(6)]
brick3=[pygame.Rect(10+i*100,140,80,30) for i in range(6)]

# drawing brick on screen
def drawBrick(bricks):
    for i in bricks:
        pygame.draw.rect(screen, RED, i)

score = 0
velocity = [1,1]
size=(600,600)
screen = pygame.display.set_mode(size)  # window of size 600*600
pygame.display.set_caption("Brick Game --byTanviSharma") # title of the window

paddle=pygame.Rect(100,550,200,10)
ball=pygame.Rect(50,250,10,10)

gameContinue = True
while gameContinue: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameContinue = False

    screen.fill(DARKBLUE)
    pygame.draw.rect(screen, LIGHTBLUE, paddle)
    
    #creating font for score
    font=pygame.font.Font(None, 34)
    text=font.render("SCORE: " + str(score), 1, WHITE)
    
    # showing text on screen
    screen.blit(text, (20,10))

    # move paddle
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            if paddle.x < 540:
                paddle.x = paddle.x + 5
            
        if event.key == pygame.K_LEFT:
            if paddle.x > 0:
                paddle.x = paddle.x - 5

    drawBrick(brick1)
    drawBrick(brick2)
    drawBrick(brick3)

    # ball movement
    ball.x = ball.x + velocity[0]
    ball.y = ball.y + velocity[1]

    if ball.x > 590 or ball.x < 0:
        velocity[0] = -velocity[0]
    
    if paddle.collidepoint(ball.x, ball.y):
        velocity[1] = -velocity[1]
    
    if ball.y >= 590:
        font=pygame.font.Font(None, 74)
        text=font.render("GAME OVER", 1, RED)
        screen.blit(text, (150,300))
        pygame.display.flip() # updating display
        pygame.time.wait(2000) # wait till 2sec
        break

    if ball.y <= 3:
        velocity[1] = -velocity[1]

    pygame.draw.rect(screen, WHITE, ball)

    for i in brick1:
        if i.collidepoint(ball.x, ball.y):
            brick1.remove(i)
            velocity[0] = -velocity[0]
            velocity[1] = -velocity[1]
            score = score + 5
    
    for i in brick2:
        if i.collidepoint(ball.x, ball.y):
            brick2.remove(i)
            velocity[0] = -velocity[0]
            velocity[1] = -velocity[1]
            score = score + 5
    
    for i in brick3:
        if i.collidepoint(ball.x, ball.y):
            brick3.remove(i)
            velocity[0] = -velocity[0]
            velocity[1] = -velocity[1]
            score = score + 5

    if score == 90:
        font=pygame.font.Font(None, 74)
        text=font.render("YOUU WON!", 1, GREEN)
        screen.blit(text, (150,300))
        pygame.display.flip()
        pygame.time.wait(2000)
        break

    pygame.time.wait(1)
    pygame.display.flip()

pygame.quit()
    

