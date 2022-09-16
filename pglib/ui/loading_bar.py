import pygame
from library.common import ColorValue


class LoadingBar:
    """A simple loading bar."""

    def __init__(
        self, back_color: ColorValue, fore_color: ColorValue, rect: pygame.Rect
    ) -> None:
        self.back_color = back_color
        self.fore_color = fore_color
        self.back_rect = rect
        self.rect = self.back_rect.copy()
        self.rect.width = 0

    def update(self, ratio: float) -> None:
        """Updates the loading bar.

        Args:
            ratio (float): The ratio of

        Returns:
            None
        """

        self.rect.width = self.back_rect.width * ratio

    def draw(self, screen: pygame.Surface) -> None:
        """Draws the loading bar onto given surface.

        Args:
            screen (pygame.Surface): Surface to draw on.

        Returns:
            None
        """
        pygame.draw.rect(screen, self.back_color, self.back_rect)
        pygame.draw.rect(screen, self.fore_color, self.rect)
