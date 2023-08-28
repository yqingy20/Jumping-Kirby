from random import randrange
import pygame
from time import sleep
pygame.init()

game_width = 284
game_height = 512

game_frame = 0
FPS = 60

game_screen = pygame.display.set_mode((game_width, game_height))
game_background = pygame.image.load("/Users/yanqingyu/Desktop/Project/images/Untitled_Artwork.png")
kirby_close_mouth = pygame.image.load("/Users/yanqingyu/Desktop/Project/Untitled_Artwork_2.png")
kirby_open_mouth = pygame.image.load("/Users/yanqingyu/Desktop/Project/Untitled_Artwork_1.png")
pipes_body = pygame.image.load("/Users/yanqingyu/Desktop/Project/pipes_1.png")
pipes_buttom_and_top = pygame.image.load("/Users/yanqingyu/Desktop/Project/pipes_2.png")

clock = pygame.time.Clock()

pipes = [[200, 4]]

kirby = [40, game_height//2 - 50]
gravity = 0.1
velocity = 0

def initPipes():
    global pipes
    for n in range(len(pipes)):
        for m in range(pipes[n][1]):
            game_screen.blit(pipes_body, (pipes[n][0], m * 32))
        for m in range(pipes[n][1]+6, 16):
            game_screen.blit(pipes_body, (pipes[n][0], m * 32))
        
        game_screen.blit(pipes_buttom_and_top, (pipes[n][0], (pipes[n][1]) * 32))
        game_screen.blit(pipes_buttom_and_top, (pipes[n][0], (pipes[n][1] + 5) * 32))
        pipes[n][0] -= 1

def initKirby(x, y):
    global game_frame
    game_screen.blit(kirby_close_mouth, (x, y))

    if 0 <= game_frame <= 30:
        game_screen.blit(kirby_close_mouth, (x, y))
        game_frame = game_frame + 1
    
    elif 30 < game_frame <= 60:
        game_screen.blit(kirby_open_mouth, (x, y))
        game_frame = game_frame + 1
        if game_frame == 60:
            game_frame = 0

def isKirbySafe():
    if kirby[1] > game_height - 35:
        print("Hitting buttom floor")
        return False
    if kirby[1] < 0:
        print("Hitting top ceiling")
        return False
    if pipes[0][0] - 30 <  kirby[0] < pipes[0][0] + 79:
        if kirby[1] < (pipes[0][1] + 1) * 32 or kirby[1] > (pipes[0][1] + 4) * 32:
            print("Hitting pipe")
            return False
        
    return True

def reset_game():
    global game_frame, game_width, game_height, FPS, pipes, kirby, gravity, velocity

    game_frame = 0
    game_width = 284
    game_height = 512
    FPS = 60
    pipes.clear()
    kirby.clear()
    pipes = [[180, 4]]

    kirby = [40, game_height//2 - 50]
    gravity = 0.2
    velocity = 0


def main():
    while True:
        if len(pipes) < 4:
            x = pipes[-1][0] + 200
            open_pos = randrange(1, 9)
            pipes.append([x, open_pos])

        if pipes[0][0] < -100:
            pipes.pop(0)


        game_screen.blit(game_background, (0,0))

        global velocity

        # closing the game frame 
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                kirby[1] -= 40
                velocity= 0
            
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        velocity += gravity
        kirby[1] += velocity
        initPipes()
        initKirby(kirby[0], kirby[1])
        pygame.display.update()

        if not isKirbySafe():
            sleep(3)
            reset_game()

        clock.tick(FPS)

main()
