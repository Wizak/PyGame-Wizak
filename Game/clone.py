import pygame

MENU_CLOUD = None
SCREEN = None
KEYS = None
CLOCK = None
MENU_AVATAR = None
MENU_SUN = None
CURSOR = None
TEXT = []

MENU_ACTIVATE = True
SETTING_ACTIVAT = False
GAME_ACTIVATE = False
END_ACTIVATE = False
MENU_SETTING_SLIDE = False
INTRO = False
SOUND = False
SETTING = False

SCREEN_SIZE = 900, 600
MENU_AVATAR_RESOLUTION = 350, 350
MENU_SUN_RESOLUTION = 350, 350
MENU_CLOUD_RESOLUTION = 600, 600
MENU_CLOUD_POS = [-40, -100]
CURSOR_RESOLUTION = 50, 50
SETTING_SLIDE_POS = [-450, 100]
SETTING_SLIDE_RESOLUTION = [200, 200]
SETTING_SLIDE_SPEED = [10]*2
CIRCLE_SIZE = int(SCREEN_SIZE[0]/2)
CIRCLE_POS = [int(CIRCLE_SIZE/2-50), int(CIRCLE_SIZE/2)+75]
CIRCLE_COLOR = 255, 255, 255
AVATAR_POS = [150, 75]
AVATAR_SPEED = [2]*2
AVATAR_SPEED_1 = [10]*2
TEXT_POS = [[675, 230], [620, 530], [150, 15], [155, 15], [620, 20]]
BACKGROUND = 0, 0, 0
TEXT_SIZE = 80, 35, 50, 50, 35
TEXT_COLOR = [(255, 0, 0), (255, 0, 0), (0, 0, 0), (255, 0, 0), (255, 0, 0)]
INTRO_RESOLUTION = [300, 300]
INTRO_1_POS = [-200, 200]
INTRO_2_POS = [-200, 200]
INTRO_3_POS = [-200, 200]

TEXT_TYPE = ['Comic Sans MS']*5
TEXT_NAME = 'PLAY', 'SOUND', 'AUTUST', 'AUTUST', 'SETTING'
SCREEN_CAPTION = 'AuTust'
SETTING_SLIDE_FILENAME = 'keys.png'
MENU_AVATAR_FILENAME = 'enemy.png'
MENU_SUN_FILENAME = 'sun.png'
MENU_CLOUD_FILENAME = 'cloud.png'
ICON_FILENAME = 'icon.png'
CURSOR_FILENAME = 'cursor.png'
BACKGROUND_MUSIC_FILENAME = 'lil.mp3'
INTRO_1_FILENAME = 'intro_1.png'
INTRO_2_FILENAME = 'intro_2.png'
INTRO_3_FILENAME = 'intro_3.png'


def game_init():
    global SCREEN, MENU_AVATAR, MENU_SUN, CURSOR, CLOCK, KEYS, MENU_CLOUD, SETTING_SLIDE, INTRO_1, INTRO_2, INTRO_3

    pygame.init()
    pygame.font.init()

    SCREEN = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(SCREEN_CAPTION)
    pygame.display.set_icon(pygame.image.load(ICON_FILENAME))

    MENU_AVATAR = pygame.transform.scale(pygame.image.load(MENU_AVATAR_FILENAME), MENU_AVATAR_RESOLUTION)
    MENU_SUN = pygame.transform.scale(pygame.image.load(MENU_SUN_FILENAME), MENU_SUN_RESOLUTION)
    MENU_CLOUD = pygame.transform.scale(pygame.image.load(MENU_CLOUD_FILENAME), MENU_CLOUD_RESOLUTION)
    INTRO_1 = pygame.transform.scale(pygame.image.load(INTRO_1_FILENAME), INTRO_RESOLUTION)
    INTRO_2 = pygame.transform.scale(pygame.image.load(INTRO_2_FILENAME), INTRO_RESOLUTION)
    INTRO_3 = pygame.transform.scale(pygame.image.load(INTRO_3_FILENAME), INTRO_RESOLUTION)
    SETTING_SLIDE = pygame.transform.scale(pygame.image.load(SETTING_SLIDE_FILENAME), SETTING_SLIDE_RESOLUTION)

    CURSOR = pygame.transform.scale(pygame.image.load(CURSOR_FILENAME), CURSOR_RESOLUTION)
    CLOCK = pygame.time.Clock()
    KEYS = pygame.key.get_pressed()

    for type, size, name, color in zip(TEXT_TYPE, TEXT_SIZE, TEXT_NAME, TEXT_COLOR):
        TEXT.append(pygame.font.SysFont(type, size).render(name, False, color))

    pygame.mouse.set_visible(False)
    pygame.mixer.music.load(BACKGROUND_MUSIC_FILENAME)
    pygame.mixer.music.play()

def game_event():
    global INTRO, SOUND, TEXT, TEXT_COLOR, SETTING

    for i in pygame.event.get():
        if i.type == pygame.MOUSEBUTTONDOWN:
            if TEXT_POS[0][0]+185 >= pygame.mouse.get_pos()[0] >= TEXT_POS[0][0] and TEXT_POS[0][1]+130 >= pygame.mouse.get_pos()[1] >= TEXT_POS[0][1]:
                if INTRO:
                    TEXT_COLOR[0] = 255, 0, 0
                    TEXT[0] = pygame.font.SysFont(TEXT_TYPE[0], TEXT_SIZE[0]).render(TEXT_NAME[0], False, TEXT_COLOR[0])
                    INTRO = False
                else:
                    TEXT_COLOR[0] = 255, 255, 255
                    TEXT[0] = pygame.font.SysFont(TEXT_TYPE[0], TEXT_SIZE[0]).render(TEXT_NAME[0], False, TEXT_COLOR[0])
                    INTRO = True

            if TEXT_POS[1][0]+155 >= pygame.mouse.get_pos()[0] >= TEXT_POS[1][0] and TEXT_POS[1][1]+75 >= pygame.mouse.get_pos()[1] >= TEXT_POS[1][1]:
                if SOUND:
                    pygame.mixer.music.unpause()
                    TEXT_COLOR[1] = 255, 0, 0
                    TEXT[1] = pygame.font.SysFont(TEXT_TYPE[1], TEXT_SIZE[1]).render(TEXT_NAME[1], False, TEXT_COLOR[1])
                    SOUND = False
                else:
                    pygame.mixer.music.pause()
                    TEXT_COLOR[1] = 255, 255, 255
                    TEXT[1] = pygame.font.SysFont(TEXT_TYPE[1], TEXT_SIZE[1]).render(TEXT_NAME[1], False, TEXT_COLOR[1])
                    SOUND = True

            if TEXT_POS[4][0]+155 >= pygame.mouse.get_pos()[0] >= TEXT_POS[4][0] and TEXT_POS[4][1]+75 >= pygame.mouse.get_pos()[1] >= TEXT_POS[4][1]:
                if SETTING:
                    TEXT_COLOR[4] = 255, 0, 0
                    SETTING = False
                else:
                    TEXT_COLOR[4] = 255, 255, 255
                    SETTING = True

                TEXT[4] = pygame.font.SysFont(TEXT_TYPE[4], TEXT_SIZE[4]).render(TEXT_NAME[4], False, TEXT_COLOR[4])

        if i.type == pygame.QUIT:
            pygame.quit()

def display_menu():
    global AVATAR_POS, AVATAR_SPEED, MENU_SUN, MENU_SETTING_SLIDE, SETTING, INTRO, CIRCLE_SIZE, MENU_ACTIVATE, GAME_ACTIVATE

    MENU_DELAY = True
    while MENU_DELAY:
        SCREEN.fill(BACKGROUND)
        pygame.draw.circle(SCREEN, CIRCLE_COLOR, CIRCLE_POS, CIRCLE_SIZE)
        SCREEN.blit(MENU_SUN, AVATAR_POS)
        SCREEN.blit(MENU_AVATAR, AVATAR_POS)
        SCREEN.blit(MENU_CLOUD, MENU_CLOUD_POS)
        for i,j in zip(TEXT, TEXT_POS):
            SCREEN.blit(i, j)
        SCREEN.blit(CURSOR, pygame.mouse.get_pos())

        if SETTING == False:
            if MENU_SETTING_SLIDE:
                SCREEN.blit(SETTING_SLIDE, SETTING_SLIDE_POS)

                if AVATAR_POS[0] <= 120 and MENU_CLOUD_POS[0] <= 120:
                    AVATAR_POS[0] += -AVATAR_SPEED_1[0]
                    MENU_CLOUD_POS[0] += -AVATAR_SPEED_1[0]
                else:
                    if AVATAR_POS[1] <= 40 or AVATAR_POS[1] >= 240:
                        AVATAR_SPEED[1] = -AVATAR_SPEED[1]
                    AVATAR_POS[1] += AVATAR_SPEED[1]

                if SETTING_SLIDE_POS[0] >= -200:
                    SETTING_SLIDE_POS[0] += -SETTING_SLIDE_SPEED[0]
            else:
                if SOUND:
                    MENU_SUN = pygame.transform.rotate(MENU_SUN, 90)

                if AVATAR_POS[1] <= 40 or AVATAR_POS[1] >= 240:
                    AVATAR_SPEED[1] = -AVATAR_SPEED[1]
                AVATAR_POS[1] += AVATAR_SPEED[1]
        else:
            if AVATAR_POS[0] >= 0 and MENU_CLOUD_POS[0] >= 0:
                AVATAR_SPEED_1[0] = -AVATAR_SPEED_1[0]
                MENU_SETTING_SLIDE = False
            else:
                MENU_SETTING_SLIDE = True

            AVATAR_POS[0] += AVATAR_SPEED_1[0]
            MENU_CLOUD_POS[0] += AVATAR_SPEED_1[0]

            if MENU_SETTING_SLIDE:
                SCREEN.blit(SETTING_SLIDE, SETTING_SLIDE_POS)

            if SETTING_SLIDE_POS[0] <= 150:
                SETTING_SLIDE_POS[0] += SETTING_SLIDE_SPEED[0]

        if INTRO:
            STATUS = False

            if MENU_SETTING_SLIDE and SETTING_SLIDE_POS[0] >= -300:
                SETTING_SLIDE_POS[0] += -30
            if AVATAR_POS[0] >= -400:
                AVATAR_POS[0] += -5
            if MENU_CLOUD_POS[0] >= -700:
                MENU_CLOUD_POS[0] += -10
            if TEXT_POS[2][0] >= -215 and TEXT_POS[3][0] >= -215:
                TEXT_POS[2][0] += -5
                TEXT_POS[3][0] += -5
            if TEXT_POS[0][0] <= 900:
                TEXT_POS[0][0] += 3
            else:
                STATUS = True
                MENU_SETTING_SLIDE = False
                SETTING = False
            if TEXT_POS[1][0] <= 900:
                TEXT_POS[1][0] += 4
            if TEXT_POS[4][0]  <= 900:
                TEXT_POS[4][0] += 4
            if STATUS:
                if CIRCLE_SIZE <= 1000:
                    CIRCLE_SIZE += 5
                else:
                    MENU_SETTING_SLIDE = False
                    SETTING = False
                    if INTRO_3_POS[0] <= 900:
                        INTRO_3_POS[0] += 15
                        SCREEN.blit(INTRO_3, INTRO_3_POS)
                    else:
                        if INTRO_2_POS[0] <= 900:
                            INTRO_2_POS[0] += 15
                            SCREEN.blit(INTRO_2, INTRO_2_POS)
                        else:
                            if INTRO_1_POS[0] <= 900:
                                INTRO_1_POS[0] += 15
                                SCREEN.blit(INTRO_1, INTRO_1_POS)
                            else:
                                MENU_DELAY = False
                                MENU_ACTIVATE = False
                                GAME_ACTIVATE = True

        game_event()
        CLOCK.tick(60)
        pygame.display.update()

def display_game():
    while 1:
        SCREEN.fill(BACKGROUND)
        SCREEN.blit(CURSOR, pygame.mouse.get_pos())
        game_event()
        CLOCK.tick(60)
        pygame.display.update()

def display_script():
    while True:
        if MENU_ACTIVATE:
            display_menu()
        elif GAME_ACTIVATE:
            display_game()
        elif END_ACTIVATE:
            display_end()

def main():
    game_init()
    display_script()


if __name__ == '__main__':
    main()
