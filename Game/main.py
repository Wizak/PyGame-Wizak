import pygame


#General initializing
window_size = 900, 600
window_title = 'My Game'

#Start main window
pygame.init()
window = pygame.display.set_mode(window_size)
pygame.display.set_caption(window_title)

#Objects initializing
fps = 1000
color = [0]*3

#Object enemy
e_pos_xy = [1]*2
e_resolution_wh = [40]*2
e_speed = [1.5]*2
e_color = [255, 0, 0]

#Object hero
h_pos_xy = [int(window_size[i]/2) for i in [0,1]]
h_resolution_wh = [20]*2
h_speed = [2]*2
h_color = [0, 0, 255]
h_health = 5

#Object border
b_pos_xy = [10]*2
b_width = 20
b_resolution = [window_size[i]-b_width for i in [0, 1]]
b_color = (0, 0, 0)

b1_pos_xy = [0]*2
b1_resolution = [window_size[i] for i in [0, 1]]
b1_color = (0, 255, 0)


#Start display window
while 1:

    #Display objects
    pygame.draw.rect(window, b1_color, b1_pos_xy+b1_resolution)
    pygame.draw.rect(window, b_color, b_pos_xy+b_resolution)
    pygame.draw.rect(window, e_color, e_pos_xy+e_resolution_wh)
    pygame.draw.rect(window, h_color, h_pos_xy+h_resolution_wh)

    pygame.display.update()

    #Enemy move
    e_pos_xy[0] += e_speed[0]
    e_pos_xy[1] += e_speed[1]

    #Reflection enemy from border
    if e_pos_xy[0]+e_resolution_wh[0] >= window_size[0] or e_pos_xy[0] <= 0:
        e_speed[0] = -e_speed[0]

    if e_pos_xy[1]+e_resolution_wh[1] >= window_size[1] or e_pos_xy[1] <= 0:
        e_speed[1] = -e_speed[1]

    #Hero move
    keys = pygame.key.get_pressed()

    # #Check hit
    # e_sx = set(range(int(e_pos_xy[0]), int(e_pos_xy[0]+e_resolution_wh[0])+1))
    # e_sy = set(range(int(e_pos_xy[1]), int(e_pos_xy[1]+e_resolution_wh[1])+1))
    #
    # h_sx = set(range(int(h_pos_xy[0]), int(h_pos_xy[0]+h_resolution_wh[0])+1))
    # h_sy = set(range(int(h_pos_xy[1]), int(h_pos_xy[1]+h_resolution_wh[1])+1))
    #
    # if not e_sx.isdisjoint(h_sx) and not e_sy.isdisjoint(h_sy):
    #     h_pos_xy[0]

    if keys[pygame.K_LEFT] and h_pos_xy[0] >= h_speed[0]+b_width:
        h_pos_xy[0] -= h_speed[0]

    if keys[pygame.K_RIGHT] and h_pos_xy[0] <= window_size[0]-h_speed[1]-b_width-h_resolution_wh[0]:
        h_pos_xy[0] += h_speed[0]

    if keys[pygame.K_UP] and h_pos_xy[1] >= h_speed[0]+b_width:
        h_pos_xy[1] -= h_speed[1]

    if keys[pygame.K_DOWN] and h_pos_xy[1] <= window_size[1]-h_speed[1]-b_width-h_resolution_wh[1]:
        h_pos_xy[1] += h_speed[1]

    # print(h_health)
    # #Cheak end Game
    # if h_health == 0:
    #     print('End Game!')

    #Delay display
    pygame.time.delay(int(1000/fps))

    #Exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
