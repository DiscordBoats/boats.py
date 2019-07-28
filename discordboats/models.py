class Bot:
    """Response object for the get_bot endpoint"""

    def __init__(self, data: dict):
        self.data = data

    def __getattribute__(self, item):
        if item == "data":
            return object.__getattribute__(self, item)
        try:
            return self.data[item]
        except KeyError as e:
            raise e

    def __getitem__(self, item):
        try:
            return self.data[item]
        except KeyError as e:
            raise e


class User:
    """Response object for the get_user endpoint"""

    def __init__(self, data: dict):
        self.data = data

    def __getattribute__(self, item):
        if item == "data":
            return object.__getattribute__(self, item)
        try:
            return self.data[item]
        except KeyError as e:
            raise e

    def __getitem__(self, item):
        try:
            return self.data[item]
        except KeyError as e:
            raise e