"""
This file is a part of the 'Unnamed' source code.
The source code is distributed under the MIT license.
"""
from typing import Dict, Tuple

import pygame

import library.utils


class Button:
    """
    Clickable button
    """

    def __init__(
        self,
        pos: Tuple[int, int],
        size: Tuple[int, int],
        colors: Dict[str, Tuple[int, int, int]],
        font_name: str,
        text: str,
        corner_radius: int = None,
    ) -> None:
        """
        Parameters:
            pos: Position of the button
            size: Size of the button
            colors: Dict containing the colors of the button. It should have "static", "hover", "text" keys
            font_name: Font file name (without the .ttf)
            text: Text on the button
        """
        self.colors = colors

        self.rect = pygame.Rect(pos, size)

        self.text = text
        font = library.utils.font(size=size[1], name=font_name)
        self.text_surf = font.render(text, False, colors["text"])
        self.text_pos = self.text_surf.get_rect(center=self.rect.center).topleft

        self.corner_radius = corner_radius

        self.state = "static"
        self.clicked = False

    def update(
        self, mouse_pos: Tuple[int, int], mouse_buttons: Tuple[int, int, int]
    ) -> None:
        """
        Updates the button
        Parameters:
            mouse_pos: Position of the mouse
            mouse_keys: Keys of the mouse
        """
        self.clicked = False
        self.state = "static"

        if self.rect.collidepoint(mouse_pos):
            if mouse_buttons[0] and not self.clicked:
                self.clicked = True

            self.state = "hover"

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draws the button
        Parameters:
            screen: Display surface
        """
        if self.corner_radius is None:
            pygame.draw.rect(screen, self.colors[self.state], self.rect)
        else:
            pygame.draw.rect(
                screen,
                self.colors[self.state],
                self.rect,
                border_radius=self.corner_radius,
            )

        screen.blit(self.text_surf, self.text_pos)
