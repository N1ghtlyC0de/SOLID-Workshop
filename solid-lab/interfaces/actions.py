"""Interfaces pequeñas y específicas por capacidad (ISP)."""

from abc import ABC, abstractmethod


class IHealable(ABC):
    @abstractmethod
    def heal(self) -> None:
        pass


class IBuildable(ABC):
    @abstractmethod
    def build(self) -> None:
        pass


class IPaintable(ABC):
    @abstractmethod
    def paint(self) -> None:
        pass


class ITeachable(ABC):
    @abstractmethod
    def teach(self) -> None:
        pass


class IMusical(ABC):
    @abstractmethod
    def play_music(self) -> None:
        pass
