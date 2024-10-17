from central_brain import add_world

class World:
    def __init__(self, world_id, x_min, x_max, y_min, y_max):
        self.world_id = world_id
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        add_world(world_id, x_min, x_max, y_min, y_max)
