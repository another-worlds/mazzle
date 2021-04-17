
# Main classes
class Game:...;
class Map:...;
class Entity:...;
class Entity:...;

class Game:
    def __init__(self, game_id1):
        self.game_id = game_id1

    @property
    def game_id(self):
        "I am the 'game_id' property."
        print('lmao')
        return self._game_id
    
    @game_id.setter
    def game_id(self, value):
        self._game_id = value
        print('alice rocks')


# Entity types
class StaticEntity(Entity):...;
class MovableEntity(Entity):...;


# Movable entities
class Player(MovableEntity):...;
class Bullet(MovableEntity):...;
class Bomb(MovableEntity):...;

#static entities
class Chest(StaticEntity):
    def __init__(self, is_true):
        self.is_true = is_true

class Hostpital(StaticEntity):...;
class Armory(StaticEntity):...;

class River(StaticEntity):
    def __init__(self, river_type):
        self.river_type = river_type

class Hole(StaticEntity):
    def __init__(self, is_exit):
        self.is_exit = is_exit