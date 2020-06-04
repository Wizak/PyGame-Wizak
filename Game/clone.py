import pygame


SCREEN = None
KEYS = None
CLOCK = None
MENU_AVATAR = None
MENU_SUN = None
CURSOR = None
TEXT = []

SCREEN_SIZE = 900, 600

MENU_ACTIVATE = True
SETTING_ACTIVAT = False
GAME_ACTIVATE = False
END_ACTIVATE = False


def game_init():
    global KEYS, CLOCK, TEXT, SCREEN, MENU_AVATAR, MENU_SUN

    SCREEN_CAPTION = 'AuTust'
    MENU_AVATAR_FILENAME = 'enemy.png'
    MENU_SUN_FILENAME = 'sun.png'
    ICON_FILENAME = 'icon.png'
    CURSOR_FILENAME = 'cursor.png'
    BACKGROUND_MUSIC_FILENAME = 'lil.mp3'

    MENU_AVATAR_RESOLUTION = 500, 500
    MENU_SUN_RESOLUTION = 700, 700
    CURSOR_RESOLUTION = 50, 50

    TEXT_TYPE, TEXT_SIZE, TEXT_NAME, TEXT_COLOR = ['Comic Sans MS']*5, [100]*5, ['PLAY', 'SOUND', 'AUTUST', 'AUTUST', 'SEBTTING'], [[255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0]]

    pygame.init()
    pygame.font.init()

    SCREEN = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(SCREEN_CAPTION)
    pygame.display.set_icon(pygame.image.load(ICON_FILENAME))

    MENU_AVATAR = pygame.transform.scale(pygame.image.load(MENU_AVATAR_FILENAME), MENU_AVATAR_RESOLUTION)
    MENU_SUN = pygame.transform.scale(pygame.image.load(MENU_SUN_FILENAME), MENU_SUN_RESOLUTION)
    CURSOR = pygame.transform.scale(pygame.image.load(CURSOR_FILENAME), CURSOR_RESOLUTION)
    CLOCK = pygame.time.Clock()
    KEYS = pygame.key.get_pressed()

    for type, size, name, color in zip(TEXT_TYPE, TEXT_SIZE, TEXT_NAME, TEXT_COLOR):
        TEXT.append(pygame.font.SysFont(type, size).render(name, False, color))

    pygame.mouse.set_visible(False)
    pygame.mixer.music.load(BACKGROUND_MUSIC_FILENAME)
    # pygame.mixer.music.play()

def display_menu():
    CIRCLE_SIZE = int(SCREEN_SIZE[0]/2)
    CIRCLE_POS = [int(CIRCLE_SIZE/2-50), int(CIRCLE_SIZE/2)+75]
    CIRCLE_COLOR = [255]*3
    AVATAR_POS = [175, 75]
    AVATAR_SPEED = [1]*2

    while 1:
        SCREEN.fill([0, 0, 0])
        pygame.draw.circle(SCREEN, CIRCLE_COLOR, CIRCLE_POS, CIRCLE_SIZE)
        SCREEN.blit(MENU_SUN, AVATAR_POS)
        SCREEN.blit(MENU_AVATAR, AVATAR_POS)

        if AVATAR_POS[1] <= 55 or AVATAR_POS[1] >= 210:
            AVATAR_SPEED[0] = -AVATAR_SPEED[0]
        AVATAR_POS[1] += AVATAR_POS[0]

        for i in TEXT:
            SCREEN.blit(i, [50, 50])

        CLOCK.tick(60)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    #
    # for i in pygame.event.get():
    #     if i.type == pygame.MOUSEBUTTONDOWN:
    #         if 675+185 >= pygame.mouse.get_pos()[0] >= 675 and 240+130 >= pygame.mouse.get_pos()[1] >= 240:
    #             game = True
    #
    #         if 635+155 >= pygame.mouse.get_pos()[0] >= 635 and 485+75 >= pygame.mouse.get_pos()[1] >= 485:
    #             if key_sound:
    #                 pygame.mixer.music.unpause()
    #                 t1_color = [255, 0, 0]
    #                 key_sound = False
    #             else:
    #                 pygame.mixer.music.pause()
    #                 t1_color = [255]*3
    #                 key_sound = True

def display_script():
    if MENU_ACTIVATE:
        display_menu()
    elif SETTING_ACTIVATE:
        display_setting()
    elif GAME_ACTIVATE:
        display_game()
    elif END_ACTIVATE:
        display_end()

def main():
    game_init()
    display_script()



if __name__ == '__main__':
    main()
