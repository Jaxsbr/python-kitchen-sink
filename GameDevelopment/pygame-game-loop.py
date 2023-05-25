import pygame


def update_game_state():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


def update(xpos, ypos, step_x, step_y, screen_width, screen_height, ball_size):
    if xpos > screen_width - ball_size or xpos < 0:
        step_x = -step_x
    if ypos > screen_height - ball_size or ypos < 0:
        step_y = -step_y

    xpos += step_x
    ypos += step_y

    return xpos, ypos, step_x, step_y


def draw(screen, logo, xpos, ypos):
    screen.fill((200, 100, 100))
    screen.blit(logo, (xpos, ypos))
    pygame.display.flip()


def main():
    pygame.init()
    logo = pygame.image.load("GameDevelopment/ball64.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Game")

    ball_size = 64
    screen_width = 800
    screen_height = 480
    screen = pygame.display.set_mode((screen_width, screen_height))

    xpos = 50
    ypos = 50
    step_x = 0.1
    step_y = 0.1

    while True:
        running = update_game_state()
        if not running:
            break

        xpos, ypos, step_x, step_y = update(
            xpos, ypos, step_x, step_y, screen_width, screen_height, ball_size
        )
        draw(screen, logo, xpos, ypos)


if __name__ == "__main__":
    main()
