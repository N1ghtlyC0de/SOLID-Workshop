from interfaces.profession import Profession
from interfaces.actions import ITeachable


class Teacher(Profession, ITeachable):
    def perform_action(self) -> None:
        self.teach()

    def teach(self) -> None:
        print("Teaching a class.")
