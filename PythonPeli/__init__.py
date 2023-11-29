import pygame
import sys
import random


class RoboSeppo:
    def __init__(self):
        pygame.init()
        self.naytto = pygame.display.set_mode((1024, 768))
        self.robo = pygame.image.load("robo.png")
        self.kolikko = pygame.image.load("kolikko.png")
        self.x = 100
        self.y = 50
        self.nopeus = 0.1
        self.move_x = 0
        self.move_y = 0
        self.kolikko_x = random.randint(0, self.naytto.get_width() - self.kolikko.get_width())
        self.kolikko_y = random.randint(0, self.naytto.get_height() - self.kolikko.get_height())
        self.piste = 0
        self.fontti = pygame.font.SysFont("Arial", 24)
        self.hirvio = pygame.image.load("hirvio.png")
        self.hirvio_x = random.randint(0, self.naytto.get_width() - self.hirvio.get_width())
        self.hirvio_y = random.randint(0, self.naytto.get_height() - self.hirvio.get_height())

    def handle_events(self):
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_UP:
                    self.move_y = -self.nopeus
                elif tapahtuma.key == pygame.K_DOWN:
                    self.move_y = self.nopeus
                elif tapahtuma.key == pygame.K_LEFT:
                    self.move_x = -self.nopeus
                elif tapahtuma.key == pygame.K_RIGHT:
                    self.move_x = self.nopeus
            elif tapahtuma.type == pygame.KEYUP:
                if tapahtuma.key == pygame.K_UP or tapahtuma.key == pygame.K_DOWN:
                    self.move_y = 0
                elif tapahtuma.key == pygame.K_LEFT or tapahtuma.key == pygame.K_RIGHT:
                    self.move_x = 0

    def update(self):
        uusi_x = self.x + self.move_x
        uusi_y = self.y + self.move_y

        if 0 <= uusi_x <= self.naytto.get_width() - self.robo.get_width():
            self.x = uusi_x
        if 0 <= uusi_y <= self.naytto.get_height() - self.robo.get_height():
            self.y = uusi_y

    def tormays(self):
        robo_rect = pygame.Rect(self.x, self.y, self.robo.get_width(), self.robo.get_height())
        kolikko_rect = pygame.Rect(self.kolikko_x, self.kolikko_y, self.kolikko.get_width(), self.kolikko.get_height())
        hirvio_rect = pygame.Rect(self.hirvio_x, self.hirvio_y, self.hirvio.get_width(), self.hirvio.get_height())

        if hirvio_rect.colliderect(robo_rect):
            self.piste = max(0, self.piste - 1)
            self.hirvio_x = random.randint(0, self.naytto.get_width() - self.hirvio.get_width())
            self.hirvio_y = random.randint(0, self.naytto.get_height() - self.hirvio.get_height())

        if robo_rect.colliderect(kolikko_rect):
            self.kolikko_x = random.randint(0, self.naytto.get_width() - self.kolikko.get_width())
            self.kolikko_y = random.randint(0, self.naytto.get_height() - self.kolikko.get_height())
            self.naytto.blit(self.hirvio, (self.hirvio_x, self.hirvio_y))

            self.piste += 1

    def paa(self):
        voitto_fontti = pygame.font.Font(None, 48)
        voitto_text = voitto_fontti.render("Voitit pelin!", True, (255, 255, 255))
        voitto_text_rect = voitto_text.get_rect(center=(self.naytto.get_width() // 2, self.naytto.get_height() // 2))

        while True:
            self.handle_events()
            self.update()
            self.tormays()
            self.naytto.fill((0, 255, 0))
            self.naytto.blit(self.robo, (self.x, self.y))
            self.naytto.blit(self.kolikko, (self.kolikko_x, self.kolikko_y))
            pisteet = self.fontti.render(f"Pisteet: {self.piste}", True, (255, 255, 255))
            self.naytto.blit(pisteet, (10, 10))
            if self.piste >= 0:
                self.hirvio_nopeus = 0.05
                if self.x < self.hirvio_x:
                    self.hirvio_x -= self.hirvio_nopeus
                elif self.x > self.hirvio_x:
                    self.hirvio_x += self.hirvio_nopeus

                if self.y < self.hirvio_y:
                    self.hirvio_y -= self.hirvio_nopeus
                elif self.y > self.hirvio_y:
                    self.hirvio_y += self.hirvio_nopeus

                self.naytto.blit(self.hirvio, (self.hirvio_x, self.hirvio_y))

            if self.piste == 10:
                self.naytto.blit(voitto_text, voitto_text_rect)
            pygame.display.flip()


if __name__ == "__main__":
    robotti = RoboSeppo()
    robotti.paa()