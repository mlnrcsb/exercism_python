# Globals for the directions
# Change the values as you see fit
EAST = lambda x, y: (x+1, y)
NORTH = lambda x, y: (x, y+1)
WEST = lambda x, y: (x-1, y)
SOUTH = lambda x, y: (x, y-1)
DIRECTIONS = [NORTH, EAST, SOUTH, WEST] #Clockwise

class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)

    def move(self, instructions: str):
        for char in instructions:
            direction = DIRECTIONS.index(self.direction)
            if char == 'L':
                self.direction = DIRECTIONS[(direction - 1) % len(DIRECTIONS)]
            elif char == 'R':
                self.direction = DIRECTIONS[(direction + 1) % len(DIRECTIONS)]
            else:
                self.coordinates = self.direction(*self.coordinates)