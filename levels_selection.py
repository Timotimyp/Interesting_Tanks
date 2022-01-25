import json
import pygame


def get_level(number):
    with open('levels.json') as le:
        data = dict(json.load(le))
    return data[number][0], data[number][1]


def write_level(m, m1):
    with open('levels.json') as levels:
        data = dict(json.load(levels))
        data['4'] = (m, m1)
    with open('levels.json', 'w') as lv:
        json.dump(data, lv)


def lvl():
    pygame.init()
    pygame.display.set_caption('Танки')
    size = 700, 570
    screen = pygame.display.set_mode(size)

    font = pygame.font.SysFont('', 145)
    screen.fill("purple")
    pygame.draw.rect(screen, (0, 100, 0), pygame.Rect(10, 10, 520, 120), 2)
    pygame.draw.rect(screen, (0, 100, 0), pygame.Rect(170, 160, 520, 120), 2)
    pygame.draw.rect(screen, (0, 100, 0), pygame.Rect(10, 300, 520, 120), 2)
    pygame.draw.rect(screen, (0, 100, 0), pygame.Rect(170, 440, 520, 120), 2)
    screen.blit(font.render('Уровень 1', True, "pink"), (17, 20))
    screen.blit(font.render('Уровень 2', True, "pink"), (184, 170))
    screen.blit(font.render('Уровень 3', True, "pink"), (17, 310))
    screen.blit(font.render('Уровень 4', True, "pink"), (184, 450))

    pygame.display.flip()
    running_for_levels = True
    while running_for_levels:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 1, None, None, None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect(10, 10, 520, 120).collidepoint(event.pos):
                    return 2, get_level('1')[0], get_level('1')[1], '1'
                if pygame.Rect(170, 160, 520, 120).collidepoint(event.pos):
                    return 2, get_level('2')[0], get_level('2')[1], '2'
                if pygame.Rect(10, 300, 520, 120).collidepoint(event.pos):
                    return 2, get_level('3')[0], get_level('3')[1], '3'
                if pygame.Rect(170, 440, 520, 120).collidepoint(event.pos):
                    return 2, get_level('4')[0], get_level('4')[1], '4'
