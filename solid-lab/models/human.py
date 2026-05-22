"""Entidad Human: solo datos genéricos de persona (SRP + DIP)."""

from interfaces.profession import Profession


class Human:
    def __init__(self, name: str, age: int, profession: Profession) -> None:
        self._name = name
        self._age = age
        self._profession = profession  # depende de abstracción, no de clases concretas

    @property
    def name(self) -> str:
        return self._name

    @property
    def age(self) -> int:
        return self._age

    @property
    def profession(self) -> Profession:
        return self._profession

    def assign_profession(self, profession: Profession) -> None:
        """Cualquier subtipo de Profession es válido (LSP)."""
        self._profession = profession

    def perform_action(self) -> None:
        self._profession.perform_action()
