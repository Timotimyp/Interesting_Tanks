import pygame


def pvp_end(win):
    pygame.init()
    pygame.display.set_caption('Танки')

    size = 700, 570
    screen = pygame.display.set_mode(size)
    screen.fill("grey")

    if win == 1:
        font = pygame.font.SysFont('', 145)
        screen.blit(font.render('ПОБЕДИЛ', True, "brown"), (80, 10))
        screen.blit(font.render('ИГРОК 1!', True, "brown"), (110, 100))
    else:
        font = pygame.font.SysFont('', 145)
        screen.blit(font.render('ПОБЕДИЛ', True, "brown"), (80, 10))
        screen.blit(font.render('ИГРОК 2!', True, "brown"), (110, 100))

    pygame.draw.rect(screen, (0, 100, 0), pygame.Rect(80, 250, 540, 120), 2)
    pygame.draw.rect(screen, (0, 100, 0), pygame.Rect(60, 400, 580, 90), 2)
    screen.blit(font.render('Повторить', True, "brown"), (95, 260))
    font = pygame.font.SysFont('', 90)
    screen.blit(font.render('Вернуться в меню', True, "brown"), (75, 410))

    pygame.display.flip()
    running_for_levels = True
    while running_for_levels:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect(90, 250, 520, 120).collidepoint(event.pos):
                    return 3
                if pygame.Rect(60, 400, 580, 90).collidepoint(event.pos):
                    return 1
