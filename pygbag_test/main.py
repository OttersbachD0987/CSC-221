from __future__ import annotations

import pygame
from pygame import Surface
from dataclasses import dataclass
from abc import ABC

@dataclass
class TextureStuff:
    texture: Surface
    size: tuple[int, int]
    
    @classmethod
    def Load(cls, a_path: str) -> TextureStuff:
        cls((tex := pygame.image.load(a_path)), tex.size)

@dataclass
class Component(ABC):
    componentID: str

class StatComponent(Component):
    ...

@dataclass
class Entity:
    size: tuple[int, int]

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 120, 200))
    screen.fill((100, 100, 0), (200, 200, 150, 150))
    pygame.display.flip()
    clock.tick(60)