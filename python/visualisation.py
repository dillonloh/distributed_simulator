import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.animation import FuncAnimation
import sqlite3
import time
import numpy as np

# Connect to the central_brain database
DB_FILE = 'central_brain.db'

def get_robot_position(robot_id):
    """Get the position, world, and destination of a robot."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''SELECT x, y, current_world, destination_x, destination_y 
                      FROM robots WHERE id = ?''', (robot_id,))
    result = cursor.fetchone()
    conn.close()
    return result

def get_world_boundaries(world_id):
    """Get the boundaries of a world from the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''SELECT x_min, x_max, y_min, y_max FROM worlds WHERE id = ?''', (world_id,))
    result = cursor.fetchone()
    conn.close()
    return result

# Define world boundaries for two worlds
worlds = {
    1: get_world_boundaries(1),  # (x_min, x_max, y_min, y_max)
    2: get_world_boundaries(2)
}

# Create a figure and axis for the plot
fig, ax = plt.subplots()
ax.set_aspect('equal')

# Plot the worlds as rectangles
world_rectangles = []
for world_id, boundaries in worlds.items():
    x_min, x_max, y_min, y_max = boundaries
    rect = Rectangle((x_min, y_min), x_max - x_min, y_max - y_min, 
                     edgecolor='blue', facecolor='none', linewidth=2)
    world_rectangles.append(rect)
    ax.add_patch(rect)
    ax.text((x_min + x_max) / 2, (y_min + y_max) / 2, f'World {world_id}', 
            fontsize=12, ha='center', va='center')

# Adjust the axis limits to include both worlds
ax.set_xlim(min(worlds[1][0], worlds[2][0]) - 10, max(worlds[1][1], worlds[2][1]) + 10)
ax.set_ylim(min(worlds[1][2], worlds[2][2]) - 10, max(worlds[1][3], worlds[2][3]) + 10)

# Create a marker for the robot
robot_marker, = ax.plot([], [], 'ro', markersize=10)

def update_robot_position(robot_id):
    """Fetch the robot's position from the database and update the plot."""
    x, y, current_world, destination_x, destination_y = get_robot_position(robot_id)
    return x, y

def init():
    """Initialize the animation."""
    robot_marker.set_data([], [])
    return robot_marker,

def update(frame):
    """Update the robot's position on each frame."""
    robot_x, robot_y = update_robot_position(1)
    robot_marker.set_data([robot_x], [robot_y])
    return robot_marker,


# Create the animation using FuncAnimation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), init_func=init, blit=True, interval=200)

plt.show()
