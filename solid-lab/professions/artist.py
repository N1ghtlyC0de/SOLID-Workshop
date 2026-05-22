from interfaces.profession import Profession
from interfaces.actions import IPaintable


class Artist(Profession, IPaintable):
    def perform_action(self) -> None:
        self.paint()

    def paint(self) -> None:
        print("Painting a masterpiece.")
