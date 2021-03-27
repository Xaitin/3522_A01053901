class InvalidDataError(Exception):
    """Invalid data error class"""
    def __init__(self, *args):
        """Initializer for data errors"""
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        """String output of our errors"""
        if self.message:
            return 'Could not process order, data was corrupted. InvalidDataError - {0}'.format(self.message)
        else:
            return 'InvalidDataError has been Raised'

