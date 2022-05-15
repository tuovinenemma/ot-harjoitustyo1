import pygame
import os
dirname = os.path.dirname(__file__)

class Maze:
    def __init__(self, screen):
        """lays the foundation for the maze

        Args:
            screen 
        """
        self._screen = screen
        self._all_units = pygame.sprite.Group()
        self._walls = pygame.sprite.Group()
        self._paths = pygame.sprite.Group()
        self._pellet = pygame.sprite.Group()
        self._cherry = pygame.sprite.Group()
        self._largepellet = pygame.sprite.Group()
        self._strawberry = pygame.sprite.Group()
        

    def _create_maze(self):
        """creates the maze
        """
        unit_size = 25
        maze = MAZE_ONE
        width, height = len(maze[0]), len(maze)
        for x in range(width):
            for y in range(height):
                unit = maze[y][x]
                x_axis = x * unit_size
                y_axis = y * unit_size
                self._add_units(unit, x_axis, y_axis)
                
        self._group_units()

    def _group_units(self):
        """groups the units
        """
        self._all_units.add(self._paths, self._walls, self._pellet, self._cherry, self._largepellet, self._strawberry)

    def _add_units(self, unit, x, y):
        """adds units to the maze

        Args:
            unit 
            x 
            y 
        """
        if unit == 1:
            self._walls.add(Wall(x, y))
        else:
            if unit == 0:
                self._paths.add(Path(x, y))
                self._pellet.add(Pellet(x, y))
            if unit == 2:
                self._paths.add(Path(x, y))
            if unit == 3:
                self._paths.add(Path(x, y))
            if unit == 4:
                self._paths.add(Path(x, y))
                self._cherry.add(Cherry(x, y))
            if unit == 5:
                self._paths.add(Path(x, y))
                self._largepellet.add(LargePellet(x, y))
            if unit == 6:
                self._paths.add(Path(x, y))
                self._strawberry.add(Strawberry(x, y))

    def _make_maze(self):
        """draws the maze
        """
        self._all_units.draw(self._screen)
                
class Pellet(pygame.sprite.Sprite):
    """draws pellets

    Args:
        pygame
    """
    def __init__(self, x, y):
        super().__init__()
        image = pygame.image.load(os.path.join(dirname, "assets", "pellet.png"))
        self.image = pygame.transform.smoothscale(image, (10, 10))
        self.rect = self.image.get_rect()
        self.rect.x = x+8
        self.rect.y = y+8
        
class LargePellet(pygame.sprite.Sprite):
    """draws large pellets

    Args:
        pygame
    """
    def __init__(self, x, y):
        super().__init__()
        image = pygame.image.load(os.path.join(dirname, "assets", "largepellet.png"))
        self.image = pygame.transform.smoothscale(image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.x = x+2
        self.rect.y = y+2
        
class Cherry(pygame.sprite.Sprite):
    """draws cherries

    Args:
        pygame
    """
    def __init__(self, x, y):
        super().__init__()
        image = pygame.image.load(os.path.join(dirname, "assets", "cherry.png"))
        self.image = pygame.transform.smoothscale(image, (25, 25))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y+1
class Strawberry(pygame.sprite.Sprite):
    """draws strawberries

    Args:
        pygame
    """
    def __init__(self, x, y):
        super().__init__()
        image = pygame.image.load(os.path.join(dirname, "assets", "strawberry.png"))
        self.image = pygame.transform.smoothscale(image, (25, 25))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y+1
        
class Path(pygame.sprite.Sprite):
    """draws paths

    Args:
        pygame
    """
    def __init__(self, x, y):
        super().__init__()
        image = pygame.Surface((25, 25))
        self.image = image
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
class Wall(pygame.sprite.Sprite):
    """draws walls

    Args:
        pygame
    """
    def __init__(self, x, y):
        super().__init__()
        image = pygame.Surface((25, 25))
        self.image = image
        self.image.fill((0, 0, 100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
MAZE_ONE = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],

        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 4, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 2, 1, 0, 1, 2, 2, 2, 2, 1, 0, 1, 0, 1, 2, 2, 2, 2, 2, 1, 0, 1, 2, 1, 0, 1],
        [1, 0, 1, 2, 1, 0, 1, 2, 2, 2, 2, 1, 0, 1, 0, 1, 2, 2, 2, 2, 2, 1, 0, 1, 2, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 5, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 2, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 6, 1, 2, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 1, 2, 2, 1, 1, 1, 0, 1, 0, 1, 1, 1, 2, 2, 2, 1, 0, 1, 1, 1, 1, 1],
        [2, 2, 2, 2, 1, 0, 1, 2, 2, 1, 0, 0, 0, 0, 0, 0, 5, 1, 2, 2, 2, 1, 0, 1, 2, 2, 2, 2],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 2, 2, 2, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [2, 2, 2, 2, 1, 0, 1, 2, 2, 1, 0, 1, 1, 1, 1, 1, 0, 1, 2, 2, 2, 1, 0, 1, 2, 2, 2, 2],
        [1, 1, 1, 1, 1, 0, 1, 2, 2, 1, 5, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 1, 0, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 2, 2, 1, 0, 0, 0, 1, 0, 0, 0, 1, 2, 2, 2, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 2, 2, 1, 1, 1, 0, 1, 0, 1, 1, 1, 2, 2, 2, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 1, 2, 2, 2, 2, 1, 0, 1, 0, 1, 2, 2, 2, 2, 2, 1, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1, 6, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 4, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]