from caesar.types import TimeLasted


class UserDoesntExistError(Exception):
    pass


class GroupDoesntExistError(Exception):
    pass


class NotEnoughTimeLastedError(Exception):
    def __init__(self, seconds: TimeLasted) -> None:
        self.second = seconds
