import pygame
import sys
from player import Player
from marceau import Marceau
from boost import Boost

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ARM_SIZE = 80
M_SIZE = 50
BOOST_SIZE = 40

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("HIHIHAHA")
clock = pygame.time.Clock()

armoire_image = pygame.transform.scale(pygame.image.load("assets/armoire.png"), (ARM_SIZE, ARM_SIZE))
marceau_image = pygame.transform.scale(pygame.image.load("assets/marceau.jpeg"), (M_SIZE, M_SIZE))
boost_image = pygame.transform.scale(pygame.image.load("assets/boost.png"), (BOOST_SIZE, BOOST_SIZE))
ARCADE_FONT = "assets/arcade.ttf"

def show_start_screen():
    font = pygame.font.Font(ARCADE_FONT, 74)
    small_font = pygame.font.Font(ARCADE_FONT, 36)
    level = 1   # Niveau par defaut

    while True: 
        screen.fill(WHITE)
        title_text = font.render("Attrape Marceau", True, BLACK)
        screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 100))

        # Boutons
        level1_button = small_font.render("Niveau 1", True, BLACK)
        level2_button = small_font.render("Niveau 2", True, BLACK)
        start_button = small_font.render("Commencer", True, BLACK)

        screen.blit(level1_button, (SCREEN_WIDTH // 2 - 200, 300))
        screen.blit(level2_button, (SCREEN_WIDTH // 2 + 50, 300))
        screen.blit(start_button, (SCREEN_WIDTH // 2 - start_button.get_width() // 2, 400))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:        # Quitter avec esc
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:    # Gerer souris
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 300 <= mouse_y <= 336:
                    if SCREEN_WIDTH // 2 - 200 <= mouse_x <= SCREEN_WIDTH // 2 - 200 + level1_button.get_width():
                        level = 1
                    elif SCREEN_WIDTH // 2 + 50 <= mouse_x <= SCREEN_WIDTH // 2 + 50 + level2_button.get_width():
                        level = 2
                elif 400 <= mouse_y <= 436 and SCREEN_WIDTH // 2 - start_button.get_width() // 2 <= mouse_x <= SCREEN_WIDTH // 2 + start_button.get_width() // 2:
                    return level                        # Commence le jeu

def show_end_screen(score):
    font = pygame.font.Font(ARCADE_FONT, 74)
    small_font = pygame.font.Font(ARCADE_FONT, 36)

    while True:
        screen.fill(WHITE)

        # Texte du score final
        end_text = font.render(f"Score final: {score}", True, RED)
        replay_button = small_font.render("Rejouer", True, BLACK)
        quit_button = small_font.render("Quitter", True, BLACK)

        screen.blit(end_text, (SCREEN_WIDTH // 2 - end_text.get_width() // 2, 200))
        screen.blit(replay_button, (SCREEN_WIDTH // 2 - 200, 400))
        screen.blit(quit_button, (SCREEN_WIDTH // 2 + 50, 400))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:    # Quitter avec esc
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 400 <= mouse_y <= 436:
                    if SCREEN_WIDTH // 2 - 200 <= mouse_x <= SCREEN_WIDTH // 2 - 200 + replay_button.get_width():
                        main()
                    elif SCREEN_WIDTH // 2 + 50 <= mouse_x <= SCREEN_WIDTH // 2 + 50 + quit_button.get_width():
                        pygame.quit()
                        sys.exit()

def main():
    level = show_start_screen()
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - ARM_SIZE - 10, ARM_SIZE)
    marceaux = [Marceau(SCREEN_WIDTH, SCREEN_HEIGHT, M_SIZE, horizontal_movement=(level == 2)) for _ in range(5)]
    boosts = [Boost(SCREEN_WIDTH, SCREEN_HEIGHT, BOOST_SIZE)]
    score = 0
    font = pygame.font.Font(ARCADE_FONT, 36)
    game_time = 60      # Temps limite en secondes
    max_score = 100     # Score maximum pour gagner
    start_ticks = pygame.time.get_ticks()

    while True:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: # Quitter avec esc
                    pygame.quit()
                    sys.exit()

        keys = pygame.key.get_pressed()
        player.move(keys, SCREEN_WIDTH, SCREEN_HEIGHT)
        player.update()

        for marceau in marceaux:
            marceau.fall(SCREEN_WIDTH)
            if marceau.y > SCREEN_HEIGHT: # Si un marceau sort de l'écran
                marceaux.remove(marceau)
                marceaux.append(Marceau(SCREEN_WIDTH, SCREEN_HEIGHT, M_SIZE, horizontal_movement=(level == 2)))
            if marceau.is_caught(player): # Si un marceau est attrape
                score += 1
                marceaux.remove(marceau)
                marceaux.append(Marceau(SCREEN_WIDTH, SCREEN_HEIGHT, M_SIZE, horizontal_movement=(level == 2)))

        for boost in boosts:
            boost.fall()    
            if boost.y > SCREEN_HEIGHT: # Si un boost sort de l'écran
                boosts.remove(boost)
                boosts.append(Boost(SCREEN_WIDTH, SCREEN_HEIGHT, BOOST_SIZE))
            if boost.is_caught(player): # Si un boost est attrape
                player.apply_boost()
                boosts.remove(boost)
                boosts.append(Boost(SCREEN_WIDTH, SCREEN_HEIGHT, BOOST_SIZE))

        player.draw(screen, armoire_image)
        for marceau in marceaux:
            marceau.draw(screen, marceau_image)
        for boost in boosts:
            boost.draw(screen, boost_image)

        # Afficher le score et le temps restant
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
        remaining_time = max(0, game_time - elapsed_time)
        time_text = font.render(f"Time: {int(remaining_time)}", True, WHITE)
        screen.blit(time_text, (10, 50))

        if remaining_time <= 0 or score >= max_score: # Verifier les conditions de fin
            break

        pygame.display.flip()
        clock.tick(30)

    show_end_screen(score)


if __name__ == "__main__":
    main()
