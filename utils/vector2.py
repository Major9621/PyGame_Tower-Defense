import math

def magnitude(position):
    
    return math.sqrt(position[0]**2 + position[1]**2)

def distance(pos1, pos2):
    
    newVector = (pos2[0] - pos1[0], pos2[1] - pos1[1])
    
    return magnitude(newVector)

def normalized(pos):
    x, y = pos
    length = math.sqrt(x**2 + y**2)
    if length == 0:
        return (0, 0) 
    return (x / length, y / length)

def add(pos1, pos2):
    return (pos1[0] + pos2[0], pos1[1] + pos2[1])

def subtract(pos1, pos2):
    return (pos1[0] - pos2[0], pos1[1] - pos2[1])