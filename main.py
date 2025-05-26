import pygame, sys
from pygame.locals import K_ESCAPE
from Game_over import end_screen, update_points 
from Menu import menu 
from Enemies import spawn_enemy, draw_enemy, update_enemies 
from Players import Player 
from Draw import draw_background, draw_lanes, draw_points, draw_speed 
from Costants import WIDTH, HEIGHT, FPS, CAR_WIDTH, CAR_HEIGHT, BG_WIDTH, MAX_POINTS, ACCELERATION, PLAYER_LANE

def main():

    # Inizializza pygame
    pygame.init()  

    # Schermo
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Gioco della Macchinina")

    # Clock
    clock = pygame.time.Clock()

    # Macchinina del giocatore
    road_x = BG_WIDTH 
    road_width = WIDTH - 2 * BG_WIDTH
    player_x = road_x + PLAYER_LANE * (road_width // 5) + ((road_width // 5) - CAR_WIDTH) // 2
    player_y = HEIGHT - CAR_HEIGHT - 20
    Win = True

    # Altri veicoli
    enemy_cars = []
    enemy_timer = 0

    # Menù
    player_image, bg, enemy_speed, max_speed, player_speed, enemy_delay = menu (screen) 

    # Player
    player = Player(player_image, player_x, player_y, player_speed)  

    # Main loop
    cicles = 0
    points = 0
    last_point_update = 0
    running = True

    while running:
        cicles += 1
        points = update_points(cicles, points)
        
        draw_background(screen, bg)

        # Eventi
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == K.ESCAPE:
                running = False
                Win = False
                pygame.quit()
                sys.exit()

        # Input
        keys = pygame.key.get_pressed()
        out_of_road = player.move(keys)
        if out_of_road:
            running = False
            Win = False 

    # Spawning nemici
        enemy_timer += 1

        if points % 20 == 0 and points != 0 and points != last_point_update and enemy_delay > 10:
            enemy_delay -= 1
            last_point_update = points
        if enemy_timer >= enemy_delay:
            spawn_enemy(road_x, road_width, enemy_cars)
            enemy_timer = 0

        # Muovi nemici
        enemy_cars = update_enemies(enemy_cars, enemy_speed)

        # Controllo collisioni
        if player.check_collision(enemy_cars):
            running = False
            Win = False

        # Disegna corsie
        draw_lanes(screen, road_x, road_width)

        # Disegna tutto
        player.draw(screen)
        for ex, ey, img in enemy_cars:
            draw_enemy(screen, ex, ey, img) 

        # Aggiorna la velocità
        if enemy_speed < max_speed:
            enemy_speed += (enemy_speed * ACCELERATION) 
        
        #Disegna punti
        draw_points(screen, points)
        #Disegna velocità
        draw_speed(screen, enemy_speed)

        #Controlla Vittoria
        if points == MAX_POINTS:
            running = False
        
        pygame.display.flip()
        clock.tick(FPS) 

    # Mostra schermata finale
    restart = end_screen(screen, points, Win)
    
    if restart:
        main() 

if __name__ == "__main__":
     # Musica
    pygame.mixer.init()
    pygame.mixer.music.load("musichetta.mp3")
    pygame.mixer.music.play(-1)
    main()
    pygame.mixer.music.stop()
    pygame.quit()
    sys.exit() 