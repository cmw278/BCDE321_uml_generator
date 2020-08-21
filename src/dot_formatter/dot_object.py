from abc import ABC, abstractmethod


class DotObject(ABC):

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def __str__(self) -> str:
        pass

    def __eq__(self, other: object) -> bool:
        # https://stackoverflow.com/a/25176504
        return ((self.__dict__ == other.__dict__)
                if isinstance(other, self.__class__) else NotImplemented)

    def __hash__(self):
        # https://stackoverflow.com/a/25176504
        # Some limitations exist, see thread for details.
        return hash(tuple(sorted(self.__dict__.items())))
