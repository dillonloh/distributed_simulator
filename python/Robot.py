from central_brain import update_robot_position, is_position_within_world

class Robot:
    def __init__(self, robot_id, x, y, current_world, destination_x=None, destination_y=None):
        self.robot_id = robot_id
        self.x = x
        self.y = y
        self.current_world = current_world
        self.destination_x = destination_x
        self.destination_y = destination_y
        update_robot_position(robot_id, x, y, current_world, destination_x, destination_y)
        print(f"[DEBUG] Robot {robot_id} initialized at ({x}, {y}) in World {current_world} with destination ({destination_x}, {destination_y})")
    
    def move(self, direction, speed, duration):
        """Move the robot and update the position."""
        new_x = self.x + direction[0] * speed * duration
        new_y = self.y + direction[1] * speed * duration
        self.x = new_x
        self.y = new_y
        update_robot_position(self.robot_id, new_x, new_y, self.current_world, self.destination_x, self.destination_y)
        print(f"[DEBUG] Robot {self.robot_id} moved to ({new_x:.2f}, {new_y:.2f}) in World {self.current_world}")

    def check_and_transfer(self):
        """Check if robot has crossed the world boundary and transfer to new world if necessary."""
        if not is_position_within_world(self.x, self.y, self.current_world):
            print(f"[DEBUG] Robot {self.robot_id} at ({self.x}, {self.y}) is crossing the boundary of World {self.current_world}")
            # Find the next world and transfer
            for world_id in range(1, 3):  # Assuming 2 worlds for simplicity
                if world_id != self.current_world and is_position_within_world(self.x, self.y, world_id):
                    print(f"[DEBUG] Robot {self.robot_id} crossing to World {world_id}")
                    self.current_world = world_id
                    update_robot_position(self.robot_id, self.x, self.y, self.current_world, self.destination_x, self.destination_y)
                    break

    def has_reached_destination(self):
        """Check if the robot has reached its destination."""
        return self.x == self.destination_x and self.y == self.destination_y
