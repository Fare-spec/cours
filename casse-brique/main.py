import pygame
import sys
import random

# Initialisation de Pygame
pygame.init()

# Définition des dimensions de la fenêtre
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Définition des couleurs (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)

# Création de la fenêtre de jeu
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Casse-Brique")

# Paramètres de la raquette
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 15
paddle_x = (SCREEN_WIDTH - PADDLE_WIDTH) / 2  # position horizontale centrée
paddle_y = SCREEN_HEIGHT - PADDLE_HEIGHT - 10   # position verticale (en bas)
paddle_speed = 7

# Paramètres de la balle
ball_radius = 10
ball_x = SCREEN_WIDTH / 2
ball_y = SCREEN_HEIGHT / 2
# La balle part dans une direction aléatoire horizontalement
ball_speed_x = 4 * random.choice([-1, 1])
ball_speed_y = -4

# Paramètres des briques
BRICK_ROWS = 5       # nombre de lignes de briques
BRICK_COLUMNS = 10   # nombre de colonnes de briques
BRICK_WIDTH = SCREEN_WIDTH // BRICK_COLUMNS
BRICK_HEIGHT = 20
brick_padding = 5

# Création de la grille de briques sous forme de liste de listes
bricks = []
for row in range(BRICK_ROWS):
    brick_row = []
    for col in range(BRICK_COLUMNS):
        # Calcul des coordonnées de la brique
        brick_x = col * BRICK_WIDTH + brick_padding
        brick_y = row * (BRICK_HEIGHT + brick_padding) + brick_padding
        # On soustrait un peu de largeur pour le padding entre les briques
        brick_rect = pygame.Rect(brick_x, brick_y, BRICK_WIDTH - brick_padding * 2, BRICK_HEIGHT)
        brick_row.append(brick_rect)
    bricks.append(brick_row)

# Horloge pour contrôler le taux de rafraîchissement (FPS)
clock = pygame.time.Clock()
FPS = 60

# Boucle principale du jeu
running = True
while running:
    clock.tick(FPS)
    
    # Gestion des événements (fermeture de la fenêtre, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Gestion du mouvement de la raquette avec les touches fléchées gauche et droite
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < SCREEN_WIDTH - PADDLE_WIDTH:
        paddle_x += paddle_speed

    # Mise à jour de la position de la balle
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Gestion des collisions avec les murs latéraux
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= SCREEN_WIDTH:
        ball_speed_x *= -1

    # Collision avec le haut de la fenêtre
    if ball_y - ball_radius <= 0:
        ball_speed_y *= -1

    # Création des rectangles pour la raquette et la balle (pour la détection des collisions)
    paddle_rect = pygame.Rect(paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball_rect = pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)

    # Collision entre la balle et la raquette
    if ball_rect.colliderect(paddle_rect) and ball_speed_y > 0:
        ball_speed_y *= -1
        # Ajustement de la direction de la balle en fonction de l'endroit où elle touche la raquette
        offset = (ball_x - (paddle_x + PADDLE_WIDTH / 2)) / (PADDLE_WIDTH / 2)
        ball_speed_x = 4 * offset

    # Gestion des collisions avec les briques
    hit_brick = None
    for row in bricks:
        for brick in row:
            if brick and ball_rect.colliderect(brick):
                hit_brick = brick
                # Inverser la direction verticale de la balle lors d'une collision avec une brique
                ball_speed_y *= -1
                break
        if hit_brick:
            # Supprimer la brique touchée en la remplaçant par None
            row[row.index(hit_brick)] = None
            break

    # Vérification si la balle sort de l'écran (cas de défaite)
    if ball_y - ball_radius > SCREEN_HEIGHT:
        print("Game Over!")
        running = False

    # Dessin de la scène
    screen.fill(BLACK)

    # Dessiner la balle
    pygame.draw.circle(screen, WHITE, (int(ball_x), int(ball_y)), ball_radius)
    
    # Dessiner la raquette
    pygame.draw.rect(screen, BLUE, paddle_rect)
    
    # Dessiner les briques restantes
    for row in bricks:
        for brick in row:
            if brick:
                pygame.draw.rect(screen, RED, brick)
    
    # Actualiser l'affichage
    pygame.display.flip()

# Fermeture de Pygame et du programme
pygame.quit()
sys.exit()

