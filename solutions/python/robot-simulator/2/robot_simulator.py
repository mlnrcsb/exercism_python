# Globals for the directions
# Change the values as you see fit
EAST = (1, 0)
NORTH = (0, 1)
WEST = (-1, 0)
SOUTH = (0, -1)
DIRECTIONS = [NORTH, EAST, SOUTH, WEST] #Clockwise

class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)

    @staticmethod
    def advance(coordinate, direction):
        x_position, y_position = coordinate
        x_movement, y_movement = direction
        return (x_position + x_movement, y_position + y_movement)
        

    def move(self, instructions: str):
        for char in instructions:
            direction = DIRECTIONS.index(self.direction)
            if char == 'L':
                self.direction = DIRECTIONS[(direction - 1) % len(DIRECTIONS)]
            elif char == 'R':
                self.direction = DIRECTIONS[(direction + 1) % len(DIRECTIONS)]
            else:
                self.coordinates = self.advance(self.coordinates, self.direction)