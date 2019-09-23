import pygame
from pygame.locals import *
import sys

class Game():
    def step(self):
        if self.seen < 5:
            self.opening()
        elif self.seen < 10:
            self.quiz()
        else:
            self.ending()

    def opening(self):
        n = 0
        if self.seen % 2 == 0:
            for i in range(48):
                n += i
                self.clock.tick(30)
                self.anime += 1
                if self.anime == 10: self.anime = 0
                self.screen.blit(self.backGroundImg, (0, 0), (0, 0, 600, 480))
                self.screen.blit(self.animeImg, (0, 0), (50 * (self.anime % 5), 50 * (self.anime // 5), 50, 50))
                self.screen.blit(self.backGroundImg1, (-n // 2, 0), (0, 0, 600, 480))
                self.screen.blit(self.animeImg, (-n // 2, 0), (50 * (self.anime % 5), 50 * (self.anime // 5), 50, 50))
                pygame.display.update()
        else:
            for i in range(48):
                n += i
                self.clock.tick(30)
                self.anime += 1
                if self.anime == 10: self.anime = 0
                self.screen.blit(self.backGroundImg1, (0, 0), (0, 0, 600, 480))
                self.screen.blit(self.animeImg, (0, 0), (50 * (self.anime % 5), 50 * (self.anime // 5), 50, 50))
                self.screen.blit(self.backGroundImg, (-n // 2, 0), (0, 0, 600, 480))
                self.screen.blit(self.animeImg, (-n // 2, 0), (50 * (self.anime % 5), 50 * (self.anime // 5), 50, 50))
                pygame.display.update()
        self.seen += 1

    def quiz(self):
        self.seen += 1

    def ending(self):
        self.seen += 1

    def drawScreen(self):
        if self.seen % 2 == 0:
            self.screen.blit(self.backGroundImg1, (0, 0), (0, 0, 600, 480))
            self.screen.blit(self.animeImg, (0, 0), (50 * (self.anime % 5), 50 * (self.anime // 5), 50, 50))
        else:
            self.screen.blit(self.backGroundImg, (0, 0), (0, 0, 600, 480))
            self.screen.blit(self.animeImg, (0, 0), (50 * (self.anime % 5), 50 * (self.anime // 5), 50, 50))

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("足あとさがし")
        self.backGroundImg = pygame.image.load("img/backGround.png")
        self.backGroundImg1 = pygame.image.load("img/backGround1.png")
        self.animeImg = pygame.image.load("img/animation.png")
        self.screen = pygame.display.set_mode((600, 480))
##        self.font = pygame.font.Font(None, 55)
        self.clock = pygame.time.Clock()
        self.seen = 0
        self.cnt = 0
        self.anime = 0

    def main(self):
        while True:
            self.clock.tick(600)
            self.cnt += 1
            if self.cnt % 100 == 0:
                if self.anime == 9: self.anime -= 10
                self.anime += 1
                self.cnt = 0
            self.drawScreen()
##            self.text = self.font.render(str(self.seen), True, (0, 0, 0))
##            self.screen.blit(self.text, (20, 100))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                    self.x, self.y = event.pos
                    self.step()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()

game = Game()
game.main()
