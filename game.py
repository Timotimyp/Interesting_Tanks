import os
import pygame
import random

NORTH = 0
WEST = 1
WEST1 = 3
SOUTH = 2
EAST = 3
EAST1 = 1

kills = 0


def load_image(name):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    return image


class Tank:
    def __init__(self, speed, rotation_speed, hp, bullet_type, design, ammunition, recharge, pos_x=5, pos_y=5):
        self.rotation_complete = True
        self.course = NORTH
        self.speed = speed
        self.normal_speed = speed
        self.rotation_speed = rotation_speed
        self.hp = hp
        self.max_hp = hp
        self.bullet_type = bullet_type
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.tank = load_image(design)
        self.now_shots = []
        self.max_ammunition = ammunition
        self.ammunition = ammunition
        self.recharge = recharge

        self.move_count = 0
        self.rotation = 0

    def move(self):
        self.move_count += 1
        if self.move_count == self.speed:
            self.move_count = 0
            return True
        return False

    def turn(self):
        self.rotation += 1
        if self.rotation == self.rotation_speed:
            self.rotation = 0
            return True
        return False

    def get_pos(self):
        return self.pos_x * 10, self.pos_y * 10

    def get_rect(self):
        return self.pos_x * 10, self.pos_y * 10, 30, 30

    def shot(self):
        if self.ammunition != 0:
            sound1.play()
            if self.course == NORTH:
                x = self.pos_x * 10 + 10
                y = self.pos_y * 10 - 11
            elif self.course == SOUTH:
                x = self.pos_x * 10 + 10
                y = self.pos_y * 10 + 31
            elif self.course == EAST:
                x = self.pos_x * 10 + 31
                y = self.pos_y * 10 + 10
            else:
                x = self.pos_x * 10 - 11
                y = self.pos_y * 10 + 10

            speed = 0
            design = 'bullet.png'

            if self.bullet_type == 0.5:
                speed = 0.5
                design = 'que.png'
            elif self.bullet_type == 2:
                speed = 2
                design = 'bullet.png'
            elif self.bullet_type == 4:
                speed = 4
                design = 'bullet.png'
            Bullet(speed, self.course, design, x, y, all_sprites)
            self.ammunition -= 1

    def move_north(self):
        if self.course != NORTH:
            self.rotation_complete = False

            if self.course == SOUTH and self.turn():
                self.tank = pygame.transform.rotate(self.tank, 90)
                self.course = EAST

            if self.course == EAST and self.turn():
                self.tank = pygame.transform.rotate(self.tank, 90)
                self.course = NORTH
                self.rotation_complete = True

            if self.course == WEST and self.turn():
                self.tank = pygame.transform.rotate(self.tank, 270)
                self.course = NORTH
                self.rotation_complete = True

        if self.move() and self.is_move_possibly():
            self.pos_y -= 1

    def move_east(self):
        if self.course != EAST:
            self.rotation_complete = False

            if self.course == WEST and self.turn():
                self.tank = pygame.transform.rotate(self.tank, 90)
                self.course = SOUTH

            if self.course == SOUTH and self.turn():
                self.tank = pygame.transform.rotate(self.tank, 90)
                self.course = EAST
                self.rotation_complete = True

            if self.course == NORTH and self.turn():
                self.tank = pygame.transform.rotate(self.tank, 270)
                self.course = EAST
                self.rotation_complete = True

        if self.move() and self.is_move_possibly():
            self.pos_x += 1

    def move_south(self):
        if self.course != SOUTH:
            self.rotation_complete = False

            if self.course == NORTH and self.turn():
                self.tank = pygame.transform.rotate(self.tank, 90)
                self.course = WEST

            if self.course == WEST and self.turn():
                self.tank = pygame.transform.rotate(self.tank, 90)
                self.course = SOUTH
                self.rotation_complete = True

            if self.course == EAST and self.turn():
                self.tank = pygame.transform.rotate(self.tank, 270)
                self.course = SOUTH
                self.rotation_complete = True

        if self.move() and self.is_move_possibly():
            self.pos_y += 1

    def move_west(self):
        if self.course != WEST:
            self.rotation_complete = False

            if self.course == EAST and self.turn():
                self.tank = pygame.transform.rotate(self.tank, 90)
                self.course = NORTH

            if self.course == NORTH and self.turn():
                self.tank = pygame.transform.rotate(self.tank, 90)
                self.course = WEST
                self.rotation_complete = True

            if self.course == SOUTH and self.turn():
                self.tank = pygame.transform.rotate(self.tank, 270)
                self.course = WEST
                self.rotation_complete = True

        if self.move() and self.is_move_possibly():
            self.pos_x -= 1

    def is_move_possibly(self):
        if self.rotation_complete:
            if self.course == NORTH:
                if ((map[self.pos_y - 1][self.pos_x] in (0, 4)) and
                        (map[self.pos_y - 1][self.pos_x + 1] in (0, 4)) and
                        (map[self.pos_y - 1][self.pos_x + 2] in (0, 4))):
                    return True
            elif self.course == SOUTH:
                if ((map[self.pos_y + 3][self.pos_x] in (0, 4)) and
                        (map[self.pos_y + 3][self.pos_x + 1] in (0, 4)) and
                        (map[self.pos_y + 3][self.pos_x + 2] in (0, 4))):
                    return True
            elif self.course == EAST:
                if ((map[self.pos_y][self.pos_x + 3] in (0, 4)) and
                        (map[self.pos_y + 1][self.pos_x + 3] in (0, 4)) and
                        (map[self.pos_y + 2][self.pos_x + 3] in (0, 4))):
                    return True
            elif self.course == WEST:
                if ((map[self.pos_y][self.pos_x - 1] in (0, 4)) and
                        (map[self.pos_y + 1][self.pos_x - 1] in (0, 4)) and
                        (map[self.pos_y + 2][self.pos_x - 1] in (0, 4))):
                    return True
        return False


class Bullet(pygame.sprite.Sprite):
    def __init__(self, speed, direction, design, pos_x, pos_y, *group):
        sound1.play()
        self.speed = speed
        self.direction = direction
        self.image = load_image(design)

        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        super().__init__(*group)

    def update(self):
        if self.direction == NORTH and (map[self.rect.y // 10 + int(bool(self.rect.x % 10)) - 1][
                                            self.rect.x // 10 + int(bool(self.rect.x % 10))] in (0, 4)):
            self.rect = self.rect.move(0, -self.speed)
        elif self.direction == SOUTH and (map[self.rect.y // 10 + int(bool(self.rect.x % 10)) - 1][
                                              self.rect.x // 10 + int(bool(self.rect.x % 10))] in (0, 4)):
            self.rect = self.rect.move(0, self.speed)
        elif self.direction == WEST and (map[self.rect.y // 10 + int(bool(self.rect.x % 10)) - 1][
                                             self.rect.x // 10 + int(bool(self.rect.x % 10))] in (0, 4)):
            self.rect = self.rect.move(-self.speed, 0)
        elif self.direction == EAST and (map[self.rect.y // 10 + int(bool(self.rect.x % 10)) - 1][
                                             self.rect.x // 10 + int(bool(self.rect.x % 10))] in (0, 4)):
            self.rect = self.rect.move(self.speed, 0)

        else:
            y = (self.rect.y // 10 + int(bool(self.rect.x % 10)) - 6) // 3
            x = (self.rect.x // 10 + int(bool(self.rect.x % 10)) - 5) // 3
            x1 = (x * 3) + 5
            y1 = (y * 3) + 5
            if (5 <= x1 < 65) and (5 <= y1 < 65):
                if map_for_build[y][x] == 3:
                    map_for_build[y][x] = 0
                    for i in range(3):
                        for j in range(3):
                            map[y1 + i][x1 + j] = 0
            Detonation(self.rect.x - 70, self.rect.y - 70)
            self.kill()
        for index, i in enumerate(enemies):
            if self.rect.colliderect(i.rect):
                i.hp -= 1
                Detonation(self.rect.x - 70, self.rect.y - 70)
                self.kill()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__(all_sprites)
        self.frames = []
        self.image = load_image('tank.png')
        self.rect = self.image.get_rect()
        self.rect.x = x * 10
        self.rect.y = y * 10
        self.speed = speed
        self.course = NORTH
        self.bullet_type = 2
        self.count = 0
        self.count1 = 0
        self.hp = 2

    def update(self):
        global kills
        self.count += 1
        if self.count % 10 == 0:
            if self.rect[1] != tank.get_pos()[-1] and not self.rect.colliderect(tank.get_rect()):
                if self.rect[1] > tank.get_pos()[-1]:
                    self.move_north()
                    if self.rect[0] == tank.get_pos()[0]:
                        self.shot()
                else:
                    self.move_south()
                    if self.rect[0] == tank.get_pos()[0]:
                        self.shot()
            elif not self.rect.colliderect(tank.get_rect()):
                if self.rect[0] > tank.get_pos()[0]:
                    self.move_east()
                    if self.rect[1] == tank.get_pos()[-1]:
                        self.shot()
                else:
                    if self.rect[0] < tank.get_pos()[0]:
                        self.move_west()
                        if self.rect[1] == tank.get_pos()[-1]:
                            self.shot()
        if self.hp == 0:
            kills += 1
            enemies[0].kill()
            del enemies[0]
            enemies.append(Enemy(50, 50, 15))
            self.kill()

    def shot(self):
        if self.course == NORTH:
            x = self.rect[0] + 10
            y = self.rect[1] - 11
        elif self.course == SOUTH:
            x = self.rect[0] + 10
            y = self.rect[1] + 31
        elif self.course == WEST1:
            x = self.rect[0] + 31
            y = self.rect[1] + 10
        else:
            x = self.rect[0] - 11
            y = self.rect[1] + 10

        speed = 0
        design = 'bullet.png'

        if self.bullet_type == 0.5:
            speed = 0.5
            design = 'que.png'
        elif self.bullet_type == 2:
            speed = 2
            design = 'bullet.png'
        elif self.bullet_type == 4:
            speed = 4
            design = 'bullet.png'

        self.count1 += 1
        if self.count1 % 3 == 0:
            Bullet_Enemy(speed, self.course, design, x, y, all_sprites)
        self.count1 += 1

    def move_north(self):
        if self.course != NORTH:

            if self.course == SOUTH:
                self.image = pygame.transform.rotate(self.image, 90)
                self.course = WEST1

            if self.course == WEST1:
                self.image = pygame.transform.rotate(self.image, 90)
                self.course = NORTH

            if self.course == EAST1:
                self.image = pygame.transform.rotate(self.image, 270)
                self.course = NORTH

        if self.is_move_possibly():
            self.rect = self.rect.move(0, -10)

    def move_west(self):
        if self.course != WEST1:

            if self.course == EAST1:
                self.image = pygame.transform.rotate(self.image, 90)
                self.course = SOUTH

            if self.course == SOUTH:
                self.image = pygame.transform.rotate(self.image, 90)
                self.course = WEST1

            if self.course == NORTH:
                self.image = pygame.transform.rotate(self.image, 270)
                self.course = WEST1

        if self.is_move_possibly():
            self.rect = self.rect.move(+10, 0)

    def move_south(self):
        if self.course != SOUTH:

            if self.course == NORTH:
                self.image = pygame.transform.rotate(self.image, 90)
                self.course = EAST1

            if self.course == EAST1:
                self.image = pygame.transform.rotate(self.image, 90)
                self.course = SOUTH

            if self.course == WEST1:
                self.image = pygame.transform.rotate(self.image, 270)
                self.course = SOUTH
        if self.is_move_possibly():
            self.rect = self.rect.move(0, +10)

    def move_east(self):
        if self.course != EAST1:
            if self.course == WEST1:
                self.image = pygame.transform.rotate(self.image, 90)
                self.course = NORTH

            if self.course == NORTH:
                self.image = pygame.transform.rotate(self.image, 90)
                self.course = EAST1

            if self.course == SOUTH:
                self.image = pygame.transform.rotate(self.image, 270)
                self.course = EAST1

        if self.is_move_possibly():
            self.rect = self.rect.move(-10, 0)

    def is_move_possibly(self):
        if self.course == NORTH:
            if ((map[self.rect[1] // 10 - 1][self.rect[0] // 10] in (0, 4)) and
                    (map[self.rect[1] // 10 - 1][self.rect[0] // 10 + 1] in (0, 4)) and
                    (map[self.rect[1] // 10 - 1][self.rect[0] // 10 + 2] in (0, 4))):
                return True
        elif self.course == SOUTH:
            if ((map[self.rect[1] // 10 + 3][self.rect[0] // 10] in (0, 4)) and
                    (map[self.rect[1] // 10 + 3][self.rect[0] // 10 + 1] in (0, 4)) and
                    (map[self.rect[1] // 10 + 3][self.rect[0] // 10 + 2] in (0, 4))):
                return True
        elif self.course == WEST1:
            if ((map[self.rect[1] // 10][self.rect[0] // 10 + 3] in (0, 4)) and
                    (map[self.rect[1] // 10 + 1][self.rect[0] // 10 + 3] in (0, 4)) and
                    (map[self.rect[1] // 10 + 2][self.rect[0] // 10 + 3] in (0, 4))):
                return True

        elif self.course == EAST1:
            if ((map[self.rect[1] // 10][self.rect[0] // 10 - 1] in (0, 4)) and
                    (map[self.rect[1] // 10 + 1][self.rect[0] // 10 - 1] in (0, 4)) and
                    (map[self.rect[1] // 10 + 2][self.rect[0] // 10 - 1] in (0, 4))):
                return True
        return False


class Bullet_Enemy(pygame.sprite.Sprite):
    def __init__(self, speed, direction, design, pos_x, pos_y, *group):

        self.speed = speed
        self.direction = direction
        self.image = load_image(design)
        self.damage = 50
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        sound1.play()
        super().__init__(*group)

    def update(self):
        if self.direction == NORTH and (map[self.rect.y // 10 + int(bool(self.rect.x % 10))][
                                            self.rect.x // 10 + int(bool(self.rect.x % 10))] in (0, 4)):
            self.rect = self.rect.move(0, -self.speed)
        elif self.direction == SOUTH and (map[self.rect.y // 10 + int(bool(self.rect.x % 10))][
                                              self.rect.x // 10 + int(bool(self.rect.x % 10))] in (0, 4)):
            self.rect = self.rect.move(0, self.speed)
        elif self.direction == EAST1 and (map[self.rect.y // 10 + int(bool(self.rect.x % 10)) - 1][
                                              self.rect.x // 10 + int(bool(self.rect.x % 10))] in (0, 4)):
            self.rect = self.rect.move(-self.speed, 0)
        elif self.direction == WEST1 and (map[self.rect.y // 10 + int(bool(self.rect.x % 10)) - 1][
                                              self.rect.x // 10 + int(bool(self.rect.x % 10))] in (0, 4)):
            self.rect = self.rect.move(self.speed, 0)
        else:
            Detonation(self.rect.x - 70, self.rect.y - 70)
            self.kill()
        if self.rect.colliderect(tank.get_rect()):
            tank.hp -= self.damage
            Detonation(self.rect.x - 70, self.rect.y - 70)
            self.kill()


class Detonation(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.frames = []
        sound2.play()
        sheet = load_image('sprite.png')
        self.cut_sheet(sheet)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)
        self.detonation_count = 0

    def cut_sheet(self, sheet):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // 7,
                                sheet.get_height() // 1)
        for j in range(1):
            for i in range(7):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.detonation_count += 1
        if self.detonation_count % 7 == 0:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]
        if self.cur_frame == 6:
            self.kill()


class Bonus(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_bonus)
        self.type = random.randint(0, 2)
        design = ['bonus1.png', 'bonus2.png', 'bonus3.png']
        self.image = load_image(design[self.type])

        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, 620)
        self.rect.y = random.randint(50, 620)

    def update(self):
        self.rect = self.rect.move(random.randrange(3) - 1, random.randrange(3) - 1)
        if self.rect.colliderect(tank.get_rect()):
            if self.type == 2:
                tank.hp = tank.max_hp
            elif self.type == 0 and tank.speed - 5 > 1:
                tank.speed -= 5
            elif self.type == 1:
                tank.ammunition += 20
            self.kill()


wall2 = load_image('wall2.png')
wall3 = load_image('wall3.png')
wall4 = load_image('wall4.png')


def create_map(screen):
    for index_i, i in enumerate(map_for_build):
        for index_j, j in enumerate(i):
            if map_for_build[index_i][index_j] == 2:
                screen.blit(wall2, (index_j * 30 + 50, index_i * 30 + 50))

            if map_for_build[index_i][index_j] == 3:
                screen.blit(wall3, (index_j * 30 + 50, index_i * 30 + 50))


def create_leaves(screen):
    for index_i, i in enumerate(map_for_build):
        for index_j, j in enumerate(i):
            if map_for_build[index_i][index_j] == 4:
                screen.blit(wall4, (index_j * 30 + 50, index_i * 30 + 50))


frame = load_image('frame.png')
pygame.init()

sound1 = pygame.mixer.Sound('blast_sound.mp3')
sound2 = pygame.mixer.Sound('blast_sound1.mp3')


def game(m, m1, lvl):
    global enemies, tank, all_bonus, all_sprites, map, map_for_build, kills
    pygame.display.set_caption('Танки')

    map = m
    map_for_build = m1
    all_sprites = pygame.sprite.Group()
    all_bonus = pygame.sprite.Group()
    enemies = []
    for i in enemies:
        i.kill()
    pygame.init()
    tank = Tank(10, 10, 100, 2, 'tank1.png', 100, 10)

    size = 700, 700
    screen = pygame.display.set_mode(size)

    create_map(screen)

    running = True
    fps = 120

    all_bonus = pygame.sprite.Group()

    now_press = 0
    button = False

    RECHARGE = pygame.USEREVENT + 1
    BONUS_GIVE = pygame.USEREVENT + 2
    pygame.time.set_timer(RECHARGE, tank.recharge * 1000)
    pygame.time.set_timer(BONUS_GIVE, 20000)

    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 50)
    shots = 0
    enemies.append(Enemy(50, 50, 15))
    while running:
        screen.fill(pygame.Color('gray'))
        screen.blit(frame, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mouse.set_visible(True)
                return 1, None, None, None

            if event.type == RECHARGE:
                if tank.max_ammunition != tank.ammunition:
                    tank.ammunition += 1

            if event.type == BONUS_GIVE:
                tank.speed = tank.normal_speed
                all_bonus = pygame.sprite.Group()
                Bonus()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    now_press = event.key
                elif event.key == pygame.K_a:
                    now_press = event.key
                elif event.key == pygame.K_s:
                    now_press = event.key
                elif event.key == pygame.K_d:
                    now_press = event.key

            if event.type == pygame.KEYUP:
                if event.key == now_press:
                    now_press = 0
                if event.key == pygame.K_SPACE:
                    button = True

        if now_press == 100:
            tank.move_east()

        if now_press == 115:
            tank.move_south()

        if now_press == 97:
            tank.move_west()

        if now_press == 119:
            tank.move_north()

        if button:
            shots += 1
            tank.shot()
            button = False

        create_map(screen)

        if tank.hp <= 0:
            pygame.mouse.set_visible(True)
            return 6, str(shots // (kills + 3) * 500), lvl, 2
        screen.blit(tank.tank, tank.get_pos())

        if kills == 10:
            pygame.mouse.set_visible(True)
            return 6, str((kills + shots) * 1127), lvl, 1

        all_sprites.draw(screen)
        all_sprites.update()
        all_bonus.draw(screen)
        all_bonus.update()

        create_leaves(screen)
        text = font.render(str(tank.hp) + '/' + str(tank.max_hp), True, pygame.Color('red'))
        screen.blit(text, (100, 10))
        text = font.render(str(tank.ammunition) + '/' + str(tank.max_ammunition), True, pygame.Color('brown'))
        screen.blit(text, (300, 10))

        clock.tick(fps)
        pygame.mouse.set_visible(False)

        pygame.display.flip()
