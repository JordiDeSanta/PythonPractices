import math

class point:

    # Initialize x,y variables
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    # Construct cartesian point format (X,Y)
    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    # Finds the quadrant of the point
    def quadrant(self):
        if self.x > 0 and self.y > 0:
            print("{} is in the first quadrant".format(self))
        elif self.x < 0 and self.y > 0:
            print("{} is in the second quadrant".format(self))
        elif self.x < 0 and self.y < 0:
            print("{} is in the third quadrant".format(self))
        elif self.x > 0 and self.y < 0:
            print("{} is in the fourth quadrant".format(self))
        elif self.x == 0 and self.y != 0:
            print("{} is in the y axis").format(self)
        elif self.x != 0 and self.y == 0:
            print("{} is in the x axis").format(self)
        else:
            print("{} is in the origin").format(self)
                  
pass

# Start
print("Give me a point in a graphic: ")

# Input and str to int transformation
print("Write the X location: "); xp = int(input())
print("Write the X location: "); yp = int(input())

# Create the point
point = point(xp, yp)
point.quadrant()



