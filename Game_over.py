import pygame 
from Costants import WIDTH, HEIGHT, WHITE, RED, YELLOW

def end_screen(screen, points, win):

    title_font = pygame.font.SysFont(None, 80)      # Font grande per "MENU PRINCIPALE"
    subtitle_font = pygame.font.SysFont(None, 36)   # Fon per "Scegli la tua macchina"

    # Schermo finale
    end_screen = True
    while end_screen:
        screen.fill((30, 30, 30))

        if not win:
            main_title = title_font.render("GAME OVER", True, RED)
            sub_text = subtitle_font.render(f"Punti: {points}", True, WHITE)
            image = pygame.image.load("image_loser.png").convert_alpha()
        else:
            main_title = title_font.render("HAI VINTO", True, RED)
            sub_text = subtitle_font.render("Punti: 100 Congratulazioni!", True, YELLOW)
            image = pygame.image.load("image_winner.png").convert_alpha()

        screen.blit(main_title, (WIDTH // 2 - main_title.get_width() // 2, 30))
        screen.blit(sub_text, (WIDTH // 2 - sub_text.get_width() // 2, 100))

        image = pygame.transform.scale(image, (200, 200))
        screen.blit(image, (WIDTH // 2 - image.get_width() // 2, HEIGHT // 2 - image.get_height() // 2))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_screen = False