from interfaces.profession import Profession
from interfaces.actions import IBuildable


class Engineer(Profession, IBuildable):
    def perform_action(self) -> None:
        self.build()

    def build(self) -> None:
        print("Building a bridge.")
