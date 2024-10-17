# central_brain.py

import sqlite3

DB_FILE = 'central_brain.db'

def setup_database():
    """Create tables for robots and worlds."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    # Drop tables if they exist
    cursor.execute('''DROP TABLE IF EXISTS robots''')
    cursor.execute('''DROP TABLE IF EXISTS worlds''')

    conn.commit()
    
    # Table for robots: id, x, y, current_world, destination_x, destination_y
    cursor.execute('''CREATE TABLE IF NOT EXISTS robots (
                      id INTEGER PRIMARY KEY, 
                      x REAL, 
                      y REAL, 
                      current_world INTEGER,
                      destination_x REAL, 
                      destination_y REAL)''')

    # Table for worlds: id, x_min, x_max, y_min, y_max
    cursor.execute('''CREATE TABLE IF NOT EXISTS worlds (
                      id INTEGER PRIMARY KEY, 
                      x_min REAL, 
                      x_max REAL, 
                      y_min REAL, 
                      y_max REAL)''')

    conn.commit()
    conn.close()

def add_world(world_id, x_min, x_max, y_min, y_max):
    """Add a world to the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO worlds (id, x_min, x_max, y_min, y_max) 
                      VALUES (?, ?, ?, ?, ?)''', (world_id, x_min, x_max, y_min, y_max))
    conn.commit()
    conn.close()

def add_robot(robot_id, x, y, world_id, destination_x=None, destination_y=None):
    """Add a robot to the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO robots (id, x, y, current_world, destination_x, destination_y) 
                      VALUES (?, ?, ?, ?, ?, ?)''', (robot_id, x, y, world_id, destination_x, destination_y))
    conn.commit()
    conn.close()

def update_robot_position(robot_id, x, y, world_id, destination_x=None, destination_y=None):
    """Update a robot's position, current world, and destination."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''UPDATE robots 
                      SET x = ?, y = ?, current_world = ?, destination_x = ?, destination_y = ? 
                      WHERE id = ?''', (x, y, world_id, destination_x, destination_y, robot_id))
    conn.commit()
    conn.close()

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

def is_position_within_world(x, y, world_id):
    """Check if a position is within the boundaries of a world."""
    x_min, x_max, y_min, y_max = get_world_boundaries(world_id)
    return x_min <= x <= x_max and y_min <= y <= y_max
