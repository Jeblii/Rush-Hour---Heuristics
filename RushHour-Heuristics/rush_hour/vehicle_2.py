class Vehicle_2(object):
    """A configuration of a single vehicle
        This class is specifically designed to work with the 9x9 and 12X12 boards
    ."""

    def __init__(self, id, x, y, orientation):
        """Create a new vehicle.

        Arguments:
            id: a valid car or truck id character
            x: the x coordinate of the top left corner of the vehicle (0-5)
            y: the y coordinate of the top left corner of the vehicle (0-5)
            orientation: either the vehicle is vertical (V) or horizontal (H)
        Exceptions:
            ValueError: on invalid id, x, y, or orientation
        """
        self.id = id
        if self.id == 0:
            self.length = 2
        elif id > 29:
            self.length = 3
        elif id < 30:
            self.length = 2

        self.x = x
        self.y = y

        if orientation == 0:
            self.orientation = orientation
            x_end = self.x + (self.length - 1)
            y_end = self.y
        elif orientation == 1:
            self.orientation = orientation
            x_end = self.x
            y_end = self.y + (self.length - 1)
