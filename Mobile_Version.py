import pygame
from pygame.constants import KEYDOWN, K_2, K_4, K_6, K_8, K_KP_2, K_KP_4, K_KP_6, K_KP_8, K_RIGHT, K_a, K_d, K_s, K_w, MOUSEBUTTONDOWN
from pygame.locals import Color
from pygame.time import Clock
import random
import os
# from pygame import mixer

pygame.init()


# Set Size For Game window

SCREEN_WIDTH = int(1080 / 2.5)  # 432
SCREEN_HEIGHT = int(1920 / 2.5)  # 768
# SCREEN_WIDTH = int(1920 / 1.1)
# SCREEN_HEIGHT = int(1080 / 1.1)


# Game Specific Varables
FOOD_SIZE_X = 10

# Creating Window
gameWindow = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set Title
# pygame.display.set_caption("Snake Game")
pygame.display.set_caption(
    "Snake Game 🐍")
pygame.display.update()
FONT = pygame.font.SysFont("Comic Sans MS", 30, bold=True, italic=False)

# Display Text on screen


def text_screen(text, color, x, y):
    SCREEN_TEXT = FONT.render(text, True, color)
    gameWindow.blit(SCREEN_TEXT, [x, y])


def plot_snake(gameWindow, color, SNAKE_LIST, ELEM_SIZE_X):
    for X, Y in SNAKE_LIST:
        pygame.draw.rect(gameWindow, color, [
            X, Y, ELEM_SIZE_X, ELEM_SIZE_X])
        # pygame.draw.circle(gameWindow, color, [
        #                        X, Y], ELEM_SIZE_X,ELEM_SIZE_X)


FPS = 120
# Home Screen
# GAME_EXIT = False


clock = pygame.time.Clock()
# Color
TEXT = (255, 255, 255)
MY_COLOR = (196, 223, 246)
MY_COLOR_2 = (34, 34, 34)
MY_COLOR_3 = (255, 76, 76)
MY_COLOR_4 = (10, 10, 10)
MY_COLOR_5 = (237, 27, 46)
EAT_FOOD = 0

# Game Function


def welcome_screen():

    GAME_EXIT = False

    while not GAME_EXIT:

        # create the display surface object
        # of specific dimension..e(X, Y).
        display_surface = pygame.display.set_mode(
            (SCREEN_WIDTH, SCREEN_HEIGHT))

        # create a surface object, image is drawn on it.
        image = pygame.image.load(
            r'Snake_Game_M_Img\welcome.png')

        display_surface.blit(image, (0, 0))

        # gameWindow.fill((233, 210, 229))
        # text_screen("Welcome to Snakes", MY_COLOR_3,
        #             SCREEN_WIDTH/4, SCREEN_HEIGHT/2)
        # text_screen("Press Space Bar To Play", MY_COLOR_3,
        #             SCREEN_WIDTH/4, SCREEN_HEIGHT/2.2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GAME_EXIT = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_KP_ENTER:
                    RUN_GAME()

        pygame.display.update()
        clock.tick(FPS)


# Game Running Function

def RUN_GAME():

    # Game Specific Variables

    GAME_OVER = False
    GAME_EXIT = False

    # FOOD_SIZE_Y = 25
    VELOCITY_X = 0.5
    VELOCITY_Y = 0
    SPEED = 0.5

    SNAKE_SIZE_X = 20
    # SNAKE_SIZE_Y = 10

    # File read for check high score
    with open("Hi-Score.txt", "r") as f:
        HI_SCORE = int(f.read())
    SCORE = 0
    SNAKE_LIST = []
    SNAKE_LENGTH = 1

    # Element Style
    POS_X = 200
    POS_Y = 150

    # Food
    FOOD_X = random.randint(90, int(SCREEN_WIDTH/2))
    FOOD_Y = random.randint(190, int(SCREEN_HEIGHT/2))
    EAT_FOOD = 0

    while not GAME_EXIT:

        if GAME_OVER:

            # gameWindow.fill(WHITE)
            # create the display surface object
            # of specific dimension..e(X, Y).
            display_surface = pygame.display.set_mode(
                (SCREEN_WIDTH, SCREEN_HEIGHT))

            # create a surface object, image is drawn on it.
            image = pygame.image.load(
                r'Snake_Game_M_Img\restart.png')

            display_surface.blit(image, (0, 0))
            text_screen(f"Your Score: {SCORE} High Score: {HI_SCORE}", MY_COLOR_2,
                        800, 100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    GAME_EXIT = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE or event.key == pygame.K_KP_ENTER:
                        RUN_GAME()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    GAME_EXIT = True

                if event.type == KEYDOWN:
                    # For Snake move
                    # Move X Axis Right
                    if event.key == pygame.K_RIGHT or event.key == K_d or event.key == K_KP_6:
                        VELOCITY_Y = 0
                        VELOCITY_X = 0
                        VELOCITY_X += SPEED

                    # Move X Axis Left
                    elif event.key == pygame.K_LEFT or event.key == K_a or event.key == K_KP_4:
                        VELOCITY_Y = 0
                        VELOCITY_X = 0
                        VELOCITY_X -= SPEED

                    # Move Y Axis UP
                    elif event.key == pygame.K_UP or event.key == K_w or event.key == K_KP_8:
                        VELOCITY_X = 0
                        VELOCITY_Y = 0
                        VELOCITY_Y -= SPEED

                    # Move Y Axis Down
                    elif event.key == pygame.K_DOWN or event.key == K_s or event.key == K_KP_2:
                        VELOCITY_X = 0
                        VELOCITY_Y = 0
                        VELOCITY_Y += SPEED

            POS_X = POS_X + VELOCITY_X

            POS_Y = POS_Y + VELOCITY_Y

            # If Else Condition for eat food and increase score
            if abs(POS_X - FOOD_X) < 30 and abs(POS_Y - FOOD_Y) < 30:
                SCORE += 100
                EAT_FOOD += 1
                SPEED += 0.2
                SNAKE_LENGTH += 5
                print(FOOD_X, FOOD_Y)
                FOOD_X = random.randint(25, 405)  # 1584, 380
                FOOD_Y = random.randint(
                    405, 730)  # 800, 730
                if SCORE > HI_SCORE:
                    with open("Hi-Score.txt", "w") as f:
                        f.write(str(SCORE))

            display_surface = pygame.display.set_mode(
                (SCREEN_WIDTH, SCREEN_HEIGHT))

            image = pygame.image.load(
                r'Snake_Game_M_Img\game_surface.png')

            display_surface.blit(image, (0, 0))

            text_screen("Score: " + str(SCORE), TEXT, 50, 4)
            # text_screen("High-Score: " + str(HI_SCORE), TEXT, 380, 4)
            # text_screen("Collect Food: " + str(EAT_FOOD), TEXT, 900, 4)

            # Draw Food
            pygame.draw.circle(gameWindow, MY_COLOR_3, [
                               FOOD_X, FOOD_Y], FOOD_SIZE_X, FOOD_SIZE_X) # Left X 25, Up Y 60 and 405, 

            SNAKE_HEAD = []
            SNAKE_HEAD.append(POS_X)
            SNAKE_HEAD.append(POS_Y)
            SNAKE_LIST.append(SNAKE_HEAD)

            # print(POS_X, POS_Y)
            # For increase snake length when snake ate food
            if len(SNAKE_LIST) > SNAKE_LENGTH:
                del SNAKE_LIST[0]

            # For Game over when snake touch wall
            if POS_X < 11 or POS_X > 399 or POS_Y < 41 or POS_Y > 728:
                GAME_OVER = True

            # For game over when snake touch himself
            if SNAKE_HEAD in SNAKE_LIST[:-1]:
                GAME_OVER = True

            # For Snake plotting
            plot_snake(gameWindow, MY_COLOR_5, SNAKE_LIST, SNAKE_SIZE_X)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()


welcome_screen()
