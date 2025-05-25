import pygame
from Costants import WIDTH, HEIGHT, CAR_WIDTH, CAR_HEIGHT, WHITE, RED, ORANGE
def menu(screen):

    #Difficoltà delle auto
    car_diff = ["Molto Facile", "Facile", "Media", "Difficile", "Molto Difficile"] 
    
    # Macchinina del giocatore
    player_images = [
    pygame.image.load("5_player.png").convert_alpha(),
    pygame.image.load("1_player.png").convert_alpha(),
    pygame.image.load("3_player.png").convert_alpha(),
    pygame.image.load("4_player.png").convert_alpha(),
    pygame.image.load("2_player.png").convert_alpha()
    ]

    # Ridimensiona le immagini
    player_images = [pygame.transform.scale(img, (CAR_WIDTH, CAR_HEIGHT)) for img in player_images]   

    # Font per il testo
    title_font = pygame.font.SysFont(None, 80)      # Font grande per "MENU PRINCIPALE"
    subtitle_font = pygame.font.SysFont(None, 36)   # Fon per "Scegli la tua macchina"
    name_font = pygame.font.SysFont(None, 28)       # Font per i nomi delle macchine

    bgs = [pygame.image.load("erba_fiori.png").convert_alpha(),
      pygame.image.load("erba_verde.png").convert_alpha(),
      pygame.image.load("erba_marrone.png").convert_alpha(),
      pygame.image.load("erba_fiori2.png").convert_alpha(),
      pygame.image.load("erba_gialla.png").convert_alpha()
    ]

    # Frecce
    right_arrow = pygame.image.load("freccia.png").convert_alpha()
    right_arrow = pygame.transform.scale(right_arrow, (50, 50))
    left_arrow = pygame.transform.flip(right_arrow, True, False)

    selected_index = 0
    selecting = True

    while selecting:
        screen.fill((30, 30, 30))

        main_title = title_font.render("MENU PRINCIPALE", True, RED)
        screen.blit(main_title, (WIDTH // 2 - main_title.get_width() // 2, 30))

        title_text = subtitle_font.render("Scegli la tua macchina - Invio per confermare", True, WHITE)
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 100))

        selected_image = player_images[selected_index]
        image_x = WIDTH // 2 - CAR_WIDTH // 2
        image_y = HEIGHT // 2 - CAR_WIDTH // 2

        car_diff_text = name_font.render(car_diff[selected_index], True, ORANGE)
        screen.blit(car_diff_text, (WIDTH // 2 - car_diff_text.get_width() // 2, image_y + CAR_HEIGHT + 15))

        pygame.draw.rect(screen, WHITE, (image_x - 5, image_y - 5, CAR_WIDTH + 10, CAR_HEIGHT + 10), 2)
        screen.blit(left_arrow, (image_x - 80, image_y + CAR_HEIGHT // 2 - 15))
        screen.blit(right_arrow, (image_x + CAR_WIDTH + 30, image_y + CAR_HEIGHT // 2 - 15))
        screen.blit(selected_image, (image_x, image_y))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    selected_index = (selected_index - 1) % len(player_images)
                if event.key == pygame.K_RIGHT:
                    selected_index = (selected_index + 1) % len(player_images)
                if event.key == pygame.K_RETURN:
                    bg = bgs[selected_index]
                    if selected_index == 0:
                        return player_images[selected_index], bg, 5, 9, 3.5, 40 # Molto Facile
                    elif selected_index == 1:
                        return player_images[selected_index], bg, 7, 11, 4.5, 35 # Facile
                    elif selected_index == 2:
                        return player_images[selected_index], bg, 9, 13, 6, 30 # Media
                    elif selected_index == 3:
                        return player_images[selected_index], bg, 11, 15, 7.5, 25 # Difficile
                    else:
                        return player_images[selected_index], bg, 13, 17, 9, 20 # Molto Difficile
    return None, None, None, None, None, None, None 