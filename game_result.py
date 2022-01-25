import pygame
from levels_selection import get_level


def men(score, level, win):
    pygame.init()
    pygame.display.set_caption('Танки')

    size = 700, 570
    screen = pygame.display.set_mode(size)
    screen.fill("brown")

    if win == 1:
        font = pygame.font.SysFont('', 145)
        screen.blit(font.render('Вы выйграли', True, "pink"), (10, 10))
    else:
        font = pygame.font.SysFont('', 140)
        screen.blit(font.render('Вы проиграли', True, "pink"), (10, 10))
    font = pygame.font.SysFont('', 110)
    screen.blit(font.render(f'Ваш счёт:{score}', True, "pink"), (15, 120))

    font = pygame.font.SysFont('', 145)
    pygame.draw.rect(screen, (0, 100, 0), pygame.Rect(80, 250, 540, 120), 2)
    pygame.draw.rect(screen, (0, 100, 0), pygame.Rect(60, 400, 580, 90), 2)
    screen.blit(font.render('Повторить', True, "pink"), (95, 260))
    font = pygame.font.SysFont('', 90)
    screen.blit(font.render('Вернуться в меню', True, "pink"), (75, 410))

    pygame.display.flip()
    running_for_levels = True
    while running_for_levels:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 1, None, None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect(90, 250, 520, 120).collidepoint(event.pos):
                    return 2, get_level(level)[0], get_level(level)[1]
                if pygame.Rect(60, 400, 580, 90).collidepoint(event.pos):
                    return 1, None, None
