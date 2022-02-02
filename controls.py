import pygame
import sys
from bullet import Bullet
from ino import Ino
import time

def events(screen, gun, bullets):
    # Обработка событя
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # вправо
            if event.key == pygame.K_d:
                gun.mright = True
            elif event.key == pygame.K_a:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            # вправо
            if event.key == pygame.K_d:
                gun.mright = False
            elif event.key == pygame.K_a:
                gun.mleft = False

def update(bg_color, screen, gun, inos, bullets):
    # Обновления экрана
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    inos.draw(screen)
    pygame.display.flip()

def update_bullets(inos, bullets):
    # обновлять позиции пуль
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collections = pygame.sprite.groupcollide(bullets, inos, True, True)

def gun_kill(stats, screen, gun, inos, bullets):
    # столкновения пушки и армии
    stats.guns_left -= 1
    inos.empty()
    bullets.empty()
    create_army(screen, inos)
    gun.create_gun()
    time.sleep(1)


def update_inos(stats, screen, gun, inos, bullets):
    # обновляет позицию инопришельца
    inos.update()
    if pygame.sprite.spritecollideany(gun, inos):
        gun_kill(stats, screen, gun, inos, bullets)




def create_army(screen, inos):
    # создания армия пришельца
    ino = Ino(screen)
    ino_with = ino.rect.width
    number_ino_x = int((700 - 2 * ino_with) / ino_with)
    ino_height = ino.rect.height
    number_ino_y = int((800 - 500 - 2 * ino_height) / ino_height)

    for row_number in range(number_ino_y - 1):
        for ino_number in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_with + (ino_with * ino_number)
            ino.y = ino_height + (ino_height * row_number)
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + (ino.rect.height * row_number)
            inos.add(ino)



