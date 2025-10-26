import pygame
import sys
import random
import math

pygame.init()

# Ukuran layar dan warna dasar
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)
BLUE = (100, 150, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Batu Gunting Kertas")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 40)

# State awal
game_state = "menu"

# Gambar karakter (pakai persegi dulu jika belum punya gambar)
player_img = pygame.image.load("assets/player.png")
computer_img = pygame.image.load("assets/computer.png")
player_img = pygame.transform.scale(player_img, (150, 150))
computer_img = pygame.transform.scale(computer_img, (150, 150))

batu_img = pygame.image.load("assets/batu.png")
gunting_img = pygame.image.load("assets/gunting.png")
kertas_img = pygame.image.load("assets/kertas.png")

# Sesuaikan ukuran biar seragam dan tidak terlalu besar
batu_img = pygame.transform.scale(batu_img, (100, 100))
gunting_img = pygame.transform.scale(gunting_img, (100, 100))
kertas_img = pygame.transform.scale(kertas_img, (100, 100))


# Pilihan dan hasil
choices = ["batu", "gunting", "kertas"]
player_choice = None
computer_choice = None
result_text = ""

# Tombol start (didefinisikan di awal agar bisa diakses di event loop)
start_button = pygame.Rect(WIDTH/2 - 70, 250, 140, 60)

# Fungsi menggambar teks
def draw_text(text, x, y, color=BLACK):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

# Fungsi reset permainan
def reset_game():
    global player_choice, computer_choice, result_text
    player_choice = None
    computer_choice = None
    result_text = ""

# Loop utama
running = True
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Menu start
        if game_state == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    game_state = "play"
                    reset_game()

        # Game utama
        elif game_state == "play":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    player_choice = "batu"
                elif event.key == pygame.K_2:
                    player_choice = "gunting"
                elif event.key == pygame.K_3:
                    player_choice = "kertas"

                # Jika pemain sudah memilih
                if player_choice:
                    computer_choice = random.choice(choices)
                    if player_choice == computer_choice:
                        result_text = "Seri!"
                    elif (player_choice == "batu" and computer_choice == "gunting") or \
                         (player_choice == "gunting" and computer_choice == "kertas") or \
                         (player_choice == "kertas" and computer_choice == "batu"):
                        result_text = "Kamu Menang!"
                    else:
                        result_text = "Kamu Kalah!"

            # Tombol kembali ke menu
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                game_state = "menu"

    # Tampilan menu
    if game_state == "menu":
        # Judul di tengah
        title = "Game Batu Gunting Kertas"
        title_surface = font.render(title, True, BLACK)
        title_rect = title_surface.get_rect(center=(WIDTH/2, HEIGHT/2 - 120))
        screen.blit(title_surface, title_rect)

        # Gambar batu, gunting, kertas ditampilkan di tengah layar
        total_width = 3 * 100 + 2 * 40  # lebar gambar + jarak antar gambar
        start_x = (WIDTH - total_width) // 2
        y_pos = HEIGHT / 2 - 40

        screen.blit(batu_img, (start_x, y_pos))
        screen.blit(gunting_img, (start_x + 140, y_pos))
        screen.blit(kertas_img, (start_x + 280, y_pos))

        # Tombol START di bawah gambar
        start_button = pygame.Rect(WIDTH/2 - 70, HEIGHT/2 + 100, 140, 60)
        pygame.draw.rect(screen, BLUE, start_button, border_radius=10)

        start_text = font.render("START", True, WHITE)
        start_rect = start_text.get_rect(center=start_button.center)
        screen.blit(start_text, start_rect)

        # Petunjuk di bawah tombol
        info_text = font.render("Klik tombol START untuk mulai", True, GRAY)
        info_rect = info_text.get_rect(center=(WIDTH/2, HEIGHT/2 + 180))
        screen.blit(info_text, info_rect)



    # Tampilan permainan
    elif game_state == "play":
        screen.blit(player_img, (180, 180))
        screen.blit(computer_img, (470, 180))
        draw_text("1: Batu   2: Gunting   3: Kertas", 200, 100)
        draw_text("ESC untuk kembali ke Menu", 230, 500, GRAY)

        if player_choice:
            draw_text(f"Kamu: {player_choice}", 180, 360)
            draw_text(f"Komputer: {computer_choice}", 470, 360)
            draw_text(result_text, 330, 420)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
