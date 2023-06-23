from abc import ABC, abstractmethod


class BaseAnyElement(ABC):
    @abstractmethod
    def __init__(self, arg) -> None:
        ...

    @abstractmethod
    def __eq__(self, other) -> bool:
        ...


class BaseManyElement(ABC):
    @abstractmethod
    def __eq__(self, other) -> bool:
        ...


class BaseOrMather(ABC):
    @abstractmethod
    def __or__(self) -> bool:
        ...
