from interfaces.profession import Profession
from interfaces.actions import IHealable


class Doctor(Profession, IHealable):
    def perform_action(self) -> None:
        self.heal()

    def heal(self) -> None:
        print("Healing a patient.")
