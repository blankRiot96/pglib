from typing import Optional

import pygame
from library.utils.classes import Time

from pglib.sprite.load import load_images
from pglib.ui.loading_bar import LoadingBar


class LoadingScreen:
    """A loading screen."""

    FONT = pygame.font.SysFont("comicsansms", 40)

    def __init__(
        self,
        state: str,
        assets: dict,
        loading_bar: LoadingBar,
        debug_timer: Optional[float] = None,
    ) -> None:
        """Constructor of the LoadingScreen.

        Args:
            state (str): Current game state.
            assets (dict): Dictionary containing all assets.
            loading_bar (LoadingBar): LoadingBar to display.
            debug_timer (float): Optional amount of time to delay between each time
            a metafile is loaded.

        Returns:
            None
        """
        self.state = state
        self.loading = True
        self.loading_text = "Loading"
        self.loading_t = Time(0.7)
        self.assets = assets
        self.loading_screen_bg = assets["loading_screen"]
        self.asset_gen = load_images(state)
        self.total_metafiles = next(self.asset_gen)
        self.loading_bar = loading_bar
        if debug_timer is not None:
            self.t = Time(debug_timer)
        else:
            self.t = None
        self.n_metafiles_loaded = 0

    def loading_text_mod(self):
        if self.loading_t.update():
            self.loading_text += "."
            if self.loading_text == "Loading....":
                self.loading_text = "Loading"

    def handle_quit(self) -> None:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                raise SystemExit

    def update(self) -> None:
        self.handle_quit()
        self.loading_text_mod()

        if (self.t is not None) and (not self.t.update()):
            return

        try:
            asset = next(self.asset_gen)
            self.n_metafiles_loaded += 1
            self.loading_bar.update(self.n_metafiles_loaded / self.total_metafiles)
        except StopIteration:
            self.loading = False
            return

        self.assets |= asset

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.loading_screen_bg, (0, 0))
        loading_text_surf = self.FONT.render(self.loading_text, True, "black")
        screen.blit(loading_text_surf, (120, 540))

        self.loading_bar.draw(screen)
        pygame.display.flip()
