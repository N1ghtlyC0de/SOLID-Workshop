"""Abstracción base para profesiones (DIP)."""

from abc import ABC, abstractmethod


class Profession(ABC):
    """Contrato común: cualquier profesión puede ejecutar una acción principal."""

    @abstractmethod
    def perform_action(self) -> None:
        pass

    @property
    def name(self) -> str:
        return self.__class__.__name__
