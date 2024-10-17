# setup.py
import sys
import os
from Simulator import simulator_process

DB_FILE = 'central_brain.db'

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python simulator.py <world_id>")
        sys.exit(1)
    world_id = int(sys.argv[1])
    simulator_process(world_id)
