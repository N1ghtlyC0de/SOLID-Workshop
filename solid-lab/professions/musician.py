"""Reto de extensión (OCP): nueva profesión sin modificar código existente."""

from interfaces.profession import Profession
from interfaces.actions import IMusical


class Musician(Profession, IMusical):
    def perform_action(self) -> None:
        self.play_music()

    def play_music(self) -> None:
        print("Playing music.")
