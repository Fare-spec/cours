import pygame
import sys
import random
import math

# Initialisation de Pygame
pygame.init()

# Définition des dimensions de la fenêtre
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

# Définition des couleurs (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Création de la fenêtre de jeu
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Casse-Brique Auto-Play")

clock = pygame.time.Clock()
FPS = 100


# Fonction d'affichage du menu de démarrage
def show_menu():
    menu_running = True
    title_font = pygame.font.SysFont("Arial", 72)
    button_font = pygame.font.SysFont("Arial", 36)
    button_width = 200
    button_height = 50
    button_rect = pygame.Rect(0, 0, button_width, button_height)
    button_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    while menu_running:
        clock.tick(FPS)
        screen.fill(BLACK)

        # Affichage du titre
        title_surface = title_font.render("Casse-Brique", True, WHITE)
        title_rect = title_surface.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3)
        )
        screen.blit(title_surface, title_rect)

        # Dessiner le bouton "Jouer"
        pygame.draw.rect(screen, BLUE, button_rect)
        button_text = button_font.render("Jouer", True, WHITE)
        button_text_rect = button_text.get_rect(center=button_rect.center)
        screen.blit(button_text, button_text_rect)

        # Gestion des événements du menu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Détection d'un clic sur le bouton "Jouer"
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button_rect.collidepoint(event.pos):
                    menu_running = False

        pygame.display.flip()


# Fonction principale du jeu
def game_loop():
    # Paramètres de la raquette
    PADDLE_WIDTH = 100
    PADDLE_HEIGHT = 15
    paddle_x = (SCREEN_WIDTH - PADDLE_WIDTH) / 2  # centré horizontalement
    paddle_y = SCREEN_HEIGHT - PADDLE_HEIGHT - 10  # position verticale en bas
    paddle_speed = 7

    # Paramètres de la balle
    ball_radius = 10
    # Liste de balles (initialement une seule)
    balls = [
        {
            "x": SCREEN_WIDTH / 2,
            "y": SCREEN_HEIGHT / 2,
            "radius": ball_radius,
            "speed_x": 9 * random.choice([-1, 1]),
            "speed_y": -9,
        }
    ]

    # Paramètres des briques
    BRICK_ROWS = 5  # nombre de lignes de briques
    BRICK_COLUMNS = 10  # nombre de colonnes de briques
    BRICK_WIDTH = SCREEN_WIDTH // BRICK_COLUMNS
    BRICK_HEIGHT = 20
    brick_padding = 5

    # Création de la grille de briques (liste de listes)
    bricks = []
    for row in range(BRICK_ROWS):
        brick_row = []
        for col in range(BRICK_COLUMNS):
            brick_x = col * BRICK_WIDTH + brick_padding
            brick_y = row * (BRICK_HEIGHT + brick_padding) + brick_padding
            brick_rect = pygame.Rect(
                brick_x, brick_y, BRICK_WIDTH - brick_padding * 2, BRICK_HEIGHT
            )
            brick_row.append(brick_rect)
        bricks.append(brick_row)

    running = True
    while running:
        clock.tick(FPS)
        screen.fill(BLACK)

        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # --- Déplacement automatique de la raquette ---
        # On cherche une balle qui descend (speed_y > 0), sinon on prend la première balle
        target_ball = None
        for ball in balls:
            if ball["speed_y"] > 0:
                target_ball = ball
                break
        if target_ball is None:
            target_ball = balls[0]
        # Calcul du centre de la raquette
        paddle_center = paddle_x + PADDLE_WIDTH / 2
        # Si le centre est trop à gauche ou à droite de la balle cible, on déplace la raquette
        if paddle_center < target_ball["x"] - 5:
            paddle_x += paddle_speed
        elif paddle_center > target_ball["x"] + 5:
            paddle_x -= paddle_speed

        # Limiter la raquette à l'intérieur de l'écran
        paddle_x = max(0, min(paddle_x, SCREEN_WIDTH - PADDLE_WIDTH))
        # Création du rectangle de la raquette pour la collision
        paddle_rect = pygame.Rect(paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)

        # Liste pour stocker les nouvelles balles créées lors des collisions avec la raquette
        nouvelles_balles = []

        # Mise à jour de la position des balles
        for ball in balls:
            ball["x"] += ball["speed_x"]
            ball["y"] += ball["speed_y"]

            # Collision avec les murs latéraux
            if (
                ball["x"] - ball["radius"] <= 0
                or ball["x"] + ball["radius"] >= SCREEN_WIDTH
            ):
                ball["speed_x"] *= -1

            # Collision avec le haut de l'écran
            if ball["y"] - ball["radius"] <= 0:
                ball["speed_y"] *= -1

            # Création du rectangle de la balle pour la détection des collisions
            ball_rect = pygame.Rect(
                ball["x"] - ball["radius"],
                ball["y"] - ball["radius"],
                ball["radius"] * 2,
                ball["radius"] * 2,
            )

            # Collision entre la balle et la raquette (uniquement si la balle descend)
            if ball_rect.colliderect(paddle_rect) and ball["speed_y"] > 0:
                ball["speed_y"] *= -1  # Inversion de la vitesse verticale
                offset = (ball["x"] - (paddle_x + PADDLE_WIDTH / 2)) / (
                    PADDLE_WIDTH / 2
                )
                ball["speed_x"] = 4 * offset

                # Création d'une nouvelle balle lors de la collision
                new_ball = ball.copy()
                new_ball["speed_x"] *= -1
                new_ball["speed_x"] += random.choice([-1, 1])
                nouvelles_balles.append(new_ball)

            # Collision entre la balle et les briques
            hit_brick = None
            for row in bricks:
                for brick in row:
                    if brick and ball_rect.colliderect(brick):
                        hit_brick = brick
                        ball["speed_y"] *= -1  # Inversion de la vitesse verticale
                        break
                if hit_brick:
                    row[row.index(hit_brick)] = None
                    break

        # Ajout des nouvelles balles générées
        balls.extend(nouvelles_balles)

        # Gestion des collisions entre balles
        for i in range(len(balls)):
            for j in range(i + 1, len(balls)):
                dx = balls[i]["x"] - balls[j]["x"]
                dy = balls[i]["y"] - balls[j]["y"]
                distance = math.sqrt(dx * dx + dy * dy)
                if distance < balls[i]["radius"] + balls[j]["radius"]:
                    # Échange des vitesses pour simuler une collision élastique
                    balls[i]["speed_x"], balls[j]["speed_x"] = (
                        balls[j]["speed_x"],
                        balls[i]["speed_x"],
                    )
                    balls[i]["speed_y"], balls[j]["speed_y"] = (
                        balls[j]["speed_y"],
                        balls[i]["speed_y"],
                    )
                    # Ajustement des positions pour éviter la superposition
                    overlap = balls[i]["radius"] + balls[j]["radius"] - distance
                    if distance != 0:
                        nx = dx / distance
                        ny = dy / distance
                    else:
                        nx, ny = 1, 0
                    balls[i]["x"] += nx * overlap / 2
                    balls[i]["y"] += ny * overlap / 2
                    balls[j]["x"] -= nx * overlap / 2
                    balls[j]["y"] -= ny * overlap / 2

        # Suppression des balles qui sortent par le bas de l'écran
        balls = [ball for ball in balls if ball["y"] - ball["radius"] <= SCREEN_HEIGHT]
        if not balls:
            print("Game Over!")
            running = False

        # Dessiner la raquette
        pygame.draw.rect(screen, BLUE, paddle_rect)

        # Dessiner les briques
        for row in bricks:
            for brick in row:
                if brick:
                    pygame.draw.rect(screen, RED, brick)

        # Dessiner les balles
        for ball in balls:
            pygame.draw.circle(
                screen, WHITE, (int(ball["x"]), int(ball["y"])), ball["radius"]
            )

        pygame.display.flip()

    pygame.quit()
    sys.exit()


# Programme principal
if __name__ == "__main__":
    show_menu()  # Afficher le menu de démarrage
    game_loop()  # Lancer le jeu
