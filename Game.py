import pygame, sys, math
from PlaySound_Button import playSound_Button
from pygame.locals import *


class Game:
    def __init__(self, screen, width, height, clock):

        pygame.mixer.init()
        pygame.mixer.set_num_channels(12)

        self.screen = screen
        self.width = width
        self.height = height
        self.clock = clock

        # Create a playSound button:
        self.play_sound_button = playSound_Button()

        # colors
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.grey = (50.2, 50.2, 50.2)

        self.running = True

    def run(self):

        # main loop
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

            left, middle, right = pygame.mouse.get_pressed()
            mouseX, mouseY = pygame.mouse.get_pos()


            self.screen.fill(self.white)

            piano = pygame.image.load('Resources/Piano_Keyboard.png')
            piano.convert()
            pianoRect = piano.get_rect()
            pianoRect.center = self.width//2, self.height//2

            self.screen.blit(piano, pianoRect)



            replay = pygame.image.load('Resources/replay_button.png')
            replaySize = pygame.transform.scale(replay, (75,75))
            replaySizeRect = replaySize.get_rect()
            replaySizeRect.move_ip(30, 30)
            self.screen.blit(replaySize, replaySizeRect)

            # Draw the playSound button
            self.play_sound_button.draw(self.screen)

            pygame.draw.line(self.screen, self.black, (0,0), (pygame.mouse.get_pos()))

            #accuracy meter
            meter = pygame.image.load("Resources/scale.png")
            meter = pygame.transform.scale(meter, (150, 150))
            self.screen.blit(meter, (self.width//2 - 75, self.height//4.5))

            needle = pygame.image.load("Resources/needle.png")
            needle = pygame.transform.scale(needle, (150, 150))
            self.screen.blit(needle, (self.width//2 - 75, self.height//4.5))
            

            print("Running Game")
            pygame.display.update()
            self.clock.tick(60)