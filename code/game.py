#!/usr/bin/python
# -*- coding: utf-8 -*-
import Menu
import pygame
class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(800, 600))

    def run(self, ):
        while True:
            menu = Menu(self.window)
            pygame.display.update()
            menu.run()
            pass


            # Check for all events
            # for event in pygame.event.get():
            # if event.type == pygame.QUIT:
            #     event.quit()  # close window
            #    quit()  # end pygame





