import pygame


def start():

    pygame.init()
    pygame.display.set_caption('Танки')
    running_for_main_window = True
    size = 700, 500
    screen = pygame.display.set_mode(size)
    font = pygame.font.SysFont('', 150)
    screen.fill((200, 255, 200))
    pygame.draw.rect(screen, (0, 100, 0), pygame.Rect(90, 20, 520, 120), 2)
    pygame.draw.rect(screen, (0, 100, 0), pygame.Rect(90, 170, 520, 120), 2)
    pygame.draw.rect(screen, (0, 100, 0), pygame.Rect(90, 320, 520, 120), 2)
    screen.blit(font.render('Редактор', True, "dark green"), (100, 30))
    screen.blit(font.render('Уровни', True, "dark green"), (150, 180))
    screen.blit(font.render('PVP', True, "dark green"), (250, 330))
    pygame.display.flip()
    while running_for_main_window:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect(90, 20, 520, 120).collidepoint(event.pos):
                    return 4
                elif pygame.Rect(90, 170, 520, 120).collidepoint(event.pos):
                    return 5
                if pygame.Rect(90, 320, 520, 120).collidepoint(event.pos):
                    return 3
