import sys
import pygame
import os
import time

# Force static position of screen
os.environ['SDL_VIDEO_CENTERED'] = '1'

win_w, win_h = 920, 570
white = (255, 255, 255)
black = (0, 0, 0)
green = (232, 247, 209)
fps = 60

# to get rid of sound lag
pygame.mixer.pre_init(44100, -16, 2, 2048)


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((win_w, win_h), pygame.SRCALPHA)
        self.left_up = self.left_down = self.right_up = self.right_down = False
        self.clock = pygame.time.Clock()
        self.play = self.intro = True

        self.left_score = Text(90, "0", win_w / 4, win_h / 10, green)
        self.right_score = Text(90, "0", win_w - (win_w / 4), win_h / 10, green)
        self.title = Text(150, "Pong", win_w / 2, win_h / 2, green)
        self.subtitle = Text(90, "-- Click Here --", win_w / 2, win_h / 1, green)

        self.intro_back = pygame.image.load("images/introBackground.jpg").convert()
        self.intro_back = pygame.transform.scale(self.intro_back, (win_w, win_h))
        self.intro_rect = self.intro_back.get_rect()
        self.game_back = pygame.image.load("images/background.jpg").convert()
        self.game_back = pygame.transform.scale(self.game_back, (win_w, win_h))
        self.game_rect = self.game_back.get_rect()

    def blink(self, subtitle, subtitle_rect):
        if pygame.time.get_ticks() % 1000 < 500:
            self.screen.blit(subtitle, subtitle_rect)

    def update(self, ball, lp, rp):
        # Increments score
        if ball.rect.left > win_w:
            lp.score += 1
            self.left_score.image = self.left_score.font.render(str(lp.score), 1, green)
            ball.rect.centerx = win_w / 2
            ball.rect.centery = win_h / 2
            time.sleep(1.5)
        elif ball.rect.right < 0:
            rp.score += 1
            self.right_score.image = self.right_score.font.render(str(rp.score), 1, green)
            ball.rect.centerx = win_w / 2
            ball.rect.centery = win_h / 2
            time.sleep(1.5)

        if lp.score == 3 or rp.score == 3:
            self.play = False


class Text:
    def __init__(self, size, text, xpos, ypos, color):
        self.font = pygame.font.SysFont("Britannic Bold", size)
        self.image = self.font.render(text, 1, color)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(xpos - self.rect.width/2, ypos - self.rect.width/2)


class Paddle:
    def __init__(self, width, height, speed, xpos):
        self.width = width
        self.height = height
        self.speed = speed
        self.image = pygame.Surface((self.width, self.height))
        self.image = pygame.image.load("images/paddle.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = pygame.Rect(xpos, (win_h/2)-(self.height/2), self.width, self.height)
        self.score = 0

    def update(self, up, down):
        # Adjust speed
        if up:
            self.rect.y -= self.speed
        if down:
            self.rect.y += self.speed

        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.bottom > win_h:
            self.rect.bottom = win_h


class Ball:
    def __init__(self, dim, speed):
        self.dim = 40
        self.speed = speed
        self.image = pygame.image.load("images/ball.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.dim, self.dim))
        self.rect = pygame.Rect(win_w / 2, win_h / 2 - (self.dim / 2), self.dim, self.dim)

    def update(self, lp, rp, left_score):
        # If ball hits the top or bottom
        if self.rect.top < 0 or self.rect.top > win_h - self.rect.height:
            self.speed[1] = -self.speed[1]

        # If ball hits the paddle
        if self.rect.left > lp.rect.right - 5 and self.rect.left < lp.rect.right + 5 and self.rect.bottom > lp.rect.top and self.rect.top < lp.rect.bottom:
            self.speed[0] = -self.speed[0]
        if self.rect.right < rp.rect.left + 5 and self.rect.right > rp.rect.left - 5 and self.rect.bottom > rp.rect.top and self.rect.top < rp.rect.bottom:
            self.speed[0] = -self.speed[0]

        self.rect = self.rect.move(self.speed)


def main():
    global win_h, win_w, white, black, fps, intro

    # Runs imported module
    pygame.init()
    pygame.display.set_caption('Pong')

    run = Game()
    left_paddle = Paddle(40, 160, 8, 40 * 2)
    right_paddle = Paddle(40, 160, 8, win_w - (40 * 3))
    ball = Ball(40, [5, 5])

    music_intro = pygame.mixer.Sound("sound/intro.ogg")
    music_game = pygame.mixer.Sound("sound/intro.ogg")
    music_intro.play(-1)

    while True:

        while run.intro:

            # Checks if window exit button pressed
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN or pygame.key.get_pressed()[pygame.K_RETURN] != 0:
                    run.intro = False
                    music_intro.stop()

            # Blitting
            run.screen.blit(run.intro_back, run.intro_rect)
            run.screen.blit(run.title.image, run.title.rect)
            run.blink(run.subtitle.image, run.subtitle.rect)

            # Limits frames per iteration of while loop
            run.clock.tick(fps)
            # Writes to main surface
            pygame.display.flip()

        # Gameplay
        while run.play:
            # Checks if window exit button pressed
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

                # Keypresses
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_UP:
                        run.right_up = True
                        run.right_down = False

                    elif event.key == pygame.K_DOWN:
                        run.right_up = False
                        run.right_down = True
                    if event.key == pygame.K_w:
                        run.left_up = True
                        run.left_down = False

                    elif event.key == pygame.K_s:
                        run.left_up = False
                        run.left_down = True

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        run.right_up = False
                    elif event.key == pygame.K_DOWN:
                        run.right_down = False
                    if event.key == pygame.K_w:
                        run.left_up = False
                    elif event.key == pygame.K_s:
                        run.left_down = False

            left_paddle.update(run.left_up, run.left_down)
            right_paddle.update(run.right_up, run.right_down)
            ball.update(left_paddle, right_paddle, run.left_score)
            run.update(ball, left_paddle, right_paddle)

            # Blitting
            run.screen.blit(run.game_back, run.game_rect)
            run.screen.blit(left_paddle.image, left_paddle.rect)
            run.screen.blit(right_paddle.image, right_paddle.rect)
            run.screen.blit(ball.image, ball.rect)
            run.screen.blit(run.left_score.image, run.left_score.rect)
            run.screen.blit(run.right_score.image, run.right_score.rect)

            # Limits frames per iteration of while loop
            run.clock.tick(fps)
            # Writes to main surface
            pygame.display.flip()

        while run.outro:


if __name__ == "__main__":
    main()