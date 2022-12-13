from pydoc import importfile
import pygame
import random


pygame.init()

 #colors
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)



#    creating a window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

 #     title of any game
pygame.display.set_caption("My snake Game")
# clock
clock = pygame.time.Clock()
# font of text
font = pygame.font.SysFont(None, 55)

#it helps to update window
pygame.display.update()
# printing text in screen
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, (x,y))


# for increasing snake length
def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

#    game loop
def gameloop():
    # variable of game
    exit_game = False
    game_over = False
    # frame per sec
    fps = 10
    snake_x = 45
    snake_y = 55
    
    
    snake_size = 30
    # velocity
    velocity_y = 0
    velocity_x = 0
    
    init_velocity = 5
    score = 0

    with open("hiscore.Txt", "r") as f:
        hiscore = f.read()

    # snake food or creating food for snake
    food_x = random.randint(20, screen_width/2)
    food_y = random.randint(20, screen_height/2)
   
    
    snk_list = []
    snk_length = 1

    #   creating a game loops
    while not exit_game:

        # for game over when cross screen
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(white)
            text_screen("Game over!!! Press Enter To Continue", red, 100, 250)

    #    event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game =True
                # print(event)
                
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
                
                # event handling here down mean press
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    
                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0
                    
                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0
                    
                    if event.key == pygame.K_DOWN:
                        # it is used for move y axis +10 and x axis 0
                        velocity_y = init_velocity
                        velocity_x = 0
            
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            # score increase abs is used of exact value
            if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
                score = score+10
                food_x = random.randint(20, screen_width/2)
                food_y = random.randint(20, screen_height/2)
                snk_length = snk_length+5
                if score>int(hiscore):
                    hiscore = score

            gameWindow.fill(white)
            # print score on screen by using function
            text_screen("screen: " + str(score) + "hiscore: " + str(hiscore), red, 5, 5)

            # apple or food
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            # for decreasing from last snake size
            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

            # when snake overlap itself
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                # print("Game Over")

                # display
                # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])

            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

                    #get type of Event
                    # if event.type == pygame.KEYDOWN:
                        #above discribe that key press or not

                        # if event.ket == pygame.K_RIGHT:
                            # print("you have pressed right arrow key")

    pygame.quit()
    quit ()
gameloop()