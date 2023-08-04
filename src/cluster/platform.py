from absl import flags
from pygame import Rect
from pygame.sprite import Sprite
from pygame.surface import Surface

from src.util.image import get_surface

FLAGS = flags.FLAGS


class Platform(Sprite):
    """
    Subjected to change, needs to adapt the Bound class, and also needs
    to have an image generated from chunks
    """

    def __init__(self, rel_x: float, rel_y: float, rel_width: float, rel_height: float):
        super().__init__()

        self.attributes = set()

        x = int(rel_x * FLAGS.game.window.width)
        y = int(rel_y * FLAGS.game.window.height)
        width = int(rel_width * FLAGS.game.window.width)
        height = int(rel_height * FLAGS.game.window.height)

        self.rect = Rect(x, y, width, height)
        self.image = get_surface(rect=self.rect, color=(0, 255, 255, 64))

    def show_bounds(self, surface: Surface):
        surface.blit(self.image, self.rect.topleft)