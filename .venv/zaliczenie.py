import pygame
import time
import random
from pyexpat.errors import messages


pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

szerokosc = 1200
wysokosc = 600

screen = pygame.display.set_mode((szerokosc,wysokosc))
pygame.display.set_caption('Zaliczenie')

snake_blok = 10
snake_speed = 15

clock = pygame.time.Clock()

styl_czcionki = pygame.font.SysFont('comicsans', 30)

def our_snake(snake_blok, snake_list):
        for x in snake_list:
            pygame.draw.rect(screen, green, (x[0], x[1], snake_blok, snake_blok))

def wiadomosc(msg,kolor, x, y):
    mesg = styl_czcionki.render(msg, True, kolor)
    screen.blit (mesg, (x, y))

def punktacja(score, screen):
    value =  styl_czcionki.render(f"Punktacja:  {score}", True, red)
    screen.blit(value, (szerokosc -250, 10))


def gameloop():
    game_over = False
    game_close = False
    game_pause = False
    game_start = False


    x1 = szerokosc /2
    y1 = wysokosc /2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, szerokosc -  snake_blok) / 10.0) * 10
    foody = round(random.randrange(0, wysokosc - snake_blok) / 10.0) * 10




    while not game_start:

        wiadomosc("nacisnij S aby rozpoaczac, pod klawiszem P masz pauze ", red, szerokosc / 6, wysokosc / 3,)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    game_start = True

    while not game_over:
        while game_close:
            screen.fill(black)
            wiadomosc("Przegrałeś! Naciśnij G- aby wyjsc albo O- aby zagrac ponownie ", red, szerokosc / 6, wysokosc / 3)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_g:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_o:
                        game_close = False
                        x1, y1 = szerokosc //2, wysokosc //2
                        x1_change, y1_change = 0, 0
                        snake_list = []
                        score = 0
                        foodx = round (random.randrange (0, szerokosc - snake_blok) / 10.0) * 10
                        foody = round (random.randrange (0, wysokosc - snake_blok) / 10.0) * 10

                        gameloop()

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_blok
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_blok
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_blok
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_blok
                        x1_change = 0
                    elif event.key == pygame.K_p:
                        game_pause = not game_pause

        if game_pause:
            pygame.display.update()
            continue


        if x1 > szerokosc or x1 < 0 or  y1 > wysokosc or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(black)
        pygame.draw.rect(screen, blue, (foodx, foody, snake_blok, snake_blok))

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_blok, snake_list)
        pygame.display.update()

        punktacja (length_of_snake -1, screen)
        pygame.display.update ()


        if x1 == foodx and y1 == foody:
            foodx =  round(random.randrange(0, szerokosc - snake_blok) / 10.0) * 10
            foody = round(random.randrange(0, wysokosc - snake_blok) / 10.0) * 10
            length_of_snake += 1


        if length_of_snake >= 50:
            wiadomosc("Gratulacje wygrałeś", red , szerokosc / 6, wysokosc / 3)
            pygame.display.update()
            game_close = True


        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameloop()
