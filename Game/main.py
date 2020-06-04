import pygame
import pkg_resources.py2_warn

try:
    import pkg_resources.py2_warn
except ImportError:
    pass


#General initializing
window_size = 900, 600
window_title = 'AuTust'

#Start main window
pygame.init()
window = pygame.display.set_mode(window_size)
pygame.display.set_caption(window_title)
images = pygame.image.load('C:\\Users\\bogda\\Desktop\\Projects\\PyGame-Wizak\\Game\\icon.png')
pygame.display.set_icon(images)

gif = pygame.image.load('C:\\Users\\bogda\\Desktop\\Projects\\PyGame-Wizak\\Game\\enemy.png')
gif = pygame.transform.scale(gif, [350]*2)
gif1 = pygame.image.load('C:\\Users\\bogda\\Desktop\\Projects\\PyGame-Wizak\\Game\\sun.png')
gif1 = pygame.transform.scale(gif1, [350]*2)

clock = pygame.time.Clock()

#Menu
#Background
m_resolution_wh = int(window_size[0]/2) #[int(window_size[i]/2) for i in [0,1]]
m_pos_xy = [int(m_resolution_wh/2-50), int(m_resolution_wh/2)+75] #[int(m_resolution_wh[i]/2) for i in [0,1]]
m_color = [255]*3

#Text play
t_size = 80
t_pox_xy = [675, 225]
t_color = [255, 0, 0]

#Text start
t1_size = 35
t1_pox_xy = [620, 523]
t1_color = [255, 0, 0]

#Text autust
t2_size = 50
t2_pox_xy = [25, 10]
t2_color = [0, 0, 0]

#Text setting
t3_size = 35
t3_pox_xy = [610, 20]
t3_color = [255, 0, 0]

#Objects initializing
game = False
fps = 60
color = [0]*3
key_sound = False

#Object border
b_width = 20
b_pos_xy = [0]*2
b_resolution = list(window_size)
b_color = (255, 0, 0)

# b1_pos_xy = [0]*2
# b1_resolution = [window_size[i] for i in [0, 1]]
# b1_color = (0, 255, 0)

#Object enemy
e_resolution_wh = 40
e_pos_xy = [100-int(e_resolution_wh/2)]*2
e_speed = [0]*2
e_color = [255, 0, 0]

#Object hero
h_resolution_wh = 20
h_pos_xy = [int((window_size[i]-h_resolution_wh)/2) for i in [0,1]]
h_speed = [2]*2
h_color = [0, 0, 255]
h_health = 5

#Object boss
boss_pos_xy = [175, 75]
boss_speed = [2]*2

pygame.mouse.set_visible(False)
MANUAL_CURSOR = pygame.image.load('C:\\Users\\bogda\\Desktop\\Projects\\PyGame-Wizak\\Game\\cursor.png')
MANUAL_CURSOR = pygame.transform.scale(MANUAL_CURSOR, [50, 50])

pygame.mixer.music.load('C:\\Users\\bogda\\Desktop\\Projects\\PyGame-Wizak\\Game\\lil.mp3')
pygame.mixer.music.play()

#Start display window
while 1:
    window.fill([0]*3)
    keys = pygame.key.get_pressed()

    # try:
    if game == False:

        pygame.draw.circle(window, m_color, m_pos_xy, m_resolution_wh)
        window.blit(gif1, [boss_pos_xy[0]+3, boss_pos_xy[1]])
        window.blit(gif, boss_pos_xy)

        if boss_pos_xy[1] <= 55 or boss_pos_xy[1] >= 210:
            boss_speed[0] = -boss_speed[0]

        boss_pos_xy[1] += boss_speed[0]
        pygame.font.init()

        textsurface = pygame.font.SysFont('Comic Sans MS', t_size).render('PLAY', False, t_color)
        textsurface1 = pygame.font.SysFont('Comic Sans MS', t1_size).render('sound', False, t1_color)
        textsurface2 = pygame.font.SysFont('Comic Sans MS', t2_size).render('AuTust', False, [255, 0, 0])
        textsurface2_1 = pygame.font.SysFont('Comic Sans MS', t2_size).render('AuTust', False, t2_color)
        textsurface3 = pygame.font.SysFont('Comic Sans MS', t3_size).render('setting', False, t3_color)

        window.blit(textsurface, t_pox_xy)
        window.blit(textsurface1, t1_pox_xy)
        window.blit(textsurface2, t2_pox_xy)
        window.blit(textsurface2_1, [t2_pox_xy[0]+3, t2_pox_xy[1]+3])
        window.blit(textsurface3, t3_pox_xy)

        for i in pygame.event.get():
            if i.type == pygame.MOUSEBUTTONDOWN:
                if 675+185 >= pygame.mouse.get_pos()[0] >= 675 and 240+130 >= pygame.mouse.get_pos()[1] >= 240:
                    game = True

                if 635+155 >= pygame.mouse.get_pos()[0] >= 635 and 485+75 >= pygame.mouse.get_pos()[1] >= 485:
                    if key_sound:
                        pygame.mixer.music.unpause()
                        t1_color = [255, 0, 0]
                        key_sound = False
                    else:
                        pygame.mixer.music.pause()
                        t1_color = [255]*3
                        key_sound = True

            if i.type == pygame.QUIT:
                pygame.quit()
    else:
        #Display objects
        pygame.draw.rect(window, b_color, b_pos_xy+b_resolution, b_width)
        pygame.draw.circle(window, e_color, e_pos_xy, e_resolution_wh)
        pygame.draw.circle(window, h_color, h_pos_xy, h_resolution_wh)

        #Enemy move
        e_pos_xy[0] += e_speed[0]
        e_pos_xy[1] += e_speed[1]

        s1 = list(zip(range(e_pos_xy[0]-e_resolution_wh, e_pos_xy[0]+e_resolution_wh+1), range(e_pos_xy[1]-e_resolution_wh, e_pos_xy[1]+e_resolution_wh+1)))

        s2 = list(zip(range(h_pos_xy[0]-h_resolution_wh, h_pos_xy[0]+h_resolution_wh+1),range(h_pos_xy[1]-h_resolution_wh, h_pos_xy[1]+h_resolution_wh+1)))

        print(pygame.mouse.get_pos())
        for point in s2:
            if pygame.mouse.get_pos() in s1:
                print('Hit!')
                print('Point: ',point)

        #Reflection enemy from border
        if e_pos_xy[0]+e_resolution_wh >= window_size[0]-int(b_width/2) or e_pos_xy[0] <= 0+int(b_width/2)+e_resolution_wh:
            e_speed[0] = -e_speed[0]

        if e_pos_xy[1]+e_resolution_wh >= window_size[1]-int(b_width/2) or e_pos_xy[1] <= 0+int(b_width/2)+e_resolution_wh:
            e_speed[1] = -e_speed[1]

        #Hero move
        if keys[pygame.K_LEFT] and h_pos_xy[0]-int(h_resolution_wh/2) >= h_speed[0]+b_width:
            h_pos_xy[0] -= h_speed[0]

        if keys[pygame.K_RIGHT] and h_pos_xy[0]+int(h_resolution_wh/2) <= window_size[0]-h_speed[1]-b_width:
            h_pos_xy[0] += h_speed[0]

        if keys[pygame.K_UP] and h_pos_xy[1]-int(h_resolution_wh/2) >= h_speed[0]+b_width:
            h_pos_xy[1] -= h_speed[1]

        if keys[pygame.K_DOWN] and h_pos_xy[1]+int(h_resolution_wh/2) <= window_size[1]-h_speed[1]-b_width:
            h_pos_xy[1] += h_speed[1]


    window.blit(MANUAL_CURSOR, pygame.mouse.get_pos())
    pygame.display.update()

    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    # except:
    #     break
