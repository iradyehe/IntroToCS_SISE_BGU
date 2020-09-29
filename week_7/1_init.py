import copy


class Vector:
    """
    A class used to represent a vector.
    :attribute values: a list of numbers that describe the vector.
    """

    def __init__(self, lst):
        """
        Constructor for vector class.
        :param lst: a list of numbers
        """

        if not isinstance(lst, list):
            raise ValueError("Wrong parameter type")
        # self.values = copy.copy(lst)
        self.values = lst