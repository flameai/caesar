from caesar.types import TimeLasted


class UserDoesnotExist(Exception):
    pass


class GroupDoesntExist(Exception):
    pass


class NotEnoughTimeLasted(Exception):
    def __init__(self, seconds: TimeLasted) -> None:
        self.second = seconds
