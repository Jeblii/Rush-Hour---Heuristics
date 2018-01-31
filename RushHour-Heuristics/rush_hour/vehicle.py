class vehicle(object):
    """A configuration of a single vehicle.
        This class is designed to work with the 6x6 boards
    """

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
        if self.id < 12:
            self.length = 2
        elif id > 11:
            self.length = 3
        elif id == 0:
            self.length = 2

        self.x = x
        self.y = y
        self.orientation = orientation