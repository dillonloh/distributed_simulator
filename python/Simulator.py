import time

import sqlite3

from Robot import Robot
from central_brain import get_robot_position

def simulator_process(world_id):
    """Simulator process for a specific world."""
    print(f"[DEBUG] Starting simulator for World {world_id}")
    while True:
        conn = sqlite3.connect('central_brain.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT id, x, y, destination_x, destination_y FROM robots WHERE current_world = ?''', (world_id,))
        robots = cursor.fetchall()
        conn.close()

        for robot_id, x, y, destination_x, destination_y in robots:
            robot = Robot(robot_id, x, y, world_id, destination_x, destination_y)
            if destination_x is None or destination_y is None:
                continue

            if robot.has_reached_destination():
                print(f"[DEBUG] Robot {robot_id} has reached its final destination at ({destination_x}, {destination_y})")
                continue

            # Calculate direction to move towards destination
            direction_x = destination_x - robot.x
            direction_y = destination_y - robot.y
            magnitude = (direction_x ** 2 + direction_y ** 2) ** 0.5
            if magnitude == 0:
                continue  # Already at destination
            direction = [direction_x / magnitude, direction_y / magnitude]

            robot.move(direction, 1, 1)  # Move at speed 1 for simplicity
            robot.check_and_transfer()

        time.sleep(1)  # Simulate robot movement every second

