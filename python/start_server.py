# setup.py

import os
import time
from central_brain import setup_database, add_robot, get_robot_position, update_robot_position
from World import World

DB_FILE = 'central_brain.db'

def get_user_input_for_destination():
    """Prompt the user for the robot's destination coordinates."""
    try:
        x = float(input("Enter the destination x-coordinate: "))
        y = float(input("Enter the destination y-coordinate: "))
        return x, y
    except ValueError:
        print("[ERROR] Invalid input, please enter numeric values for x and y.")
        return None, None

def print_current_status(robot_id):
    """Print the current status of the robot."""
    x, y, current_world, destination_x, destination_y = get_robot_position(robot_id)
    print(f"[STATUS] Robot {robot_id} is at ({x}, {y}) in World {current_world} with destination ({destination_x}, {destination_y})")

def handle_commands(robot_id):
    """Handle user commands to update the robot or show status."""
    while True:
        print("\nCommands:")
        print("1. Set new destination")
        print("2. Show current robot status")
        print("3. Exit setup")

        command = input("Enter your command: ")
        if command == '1':
            destination_x, destination_y = get_user_input_for_destination()
            if destination_x is not None and destination_y is not None:
                x, y, current_world = get_robot_position(robot_id)[:3]
                update_robot_position(robot_id, x, y, current_world, destination_x, destination_y)
                print(f"[DEBUG] Robot destination updated to ({destination_x}, {destination_y})")
        elif command == '2':
            print_current_status(robot_id)
        elif command == '3':
            print("[INFO] Exiting setup.")
            break
        else:
            print("[ERROR] Invalid command, please try again.")

def main():
    # Check if the database exists; if not, set it up.
    print("[INFO] Initializing new simulation setup.")
    setup_database()
    World(1, 0, 20, 0, 40)   # World 1 boundaries
    World(2, 20, 40, 0, 40)  # World 2 boundaries
    print("[DEBUG] Worlds 1 and 2 have been created.")

    # Add a robot starting in world 1
    add_robot(1, 5, 5, 1)
    print("[DEBUG] Robot initialized at (5, 5) in World 1")
    
    # Handle user commands for input
    handle_commands(1)

if __name__ == "__main__":
    main()
