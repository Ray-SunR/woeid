class WoeidError(Exception):
    """Base class for woeid errors
    """
    @property
    def message(self):
        """Returns the first argument used to construct this error.
        """
        return self.args[0]