#!/usr/bin/env python3
"""Simulación de humanos con profesiones — Taller SOLID."""

from models.human import Human
from professions import Doctor, Engineer, Artist, Teacher, Musician
from interfaces.actions import IHealable, IPaintable, IMusical


def run_specialized_action(human: Human) -> None:
    """Usa solo la interfaz que la profesión implementa (ISP)."""
    profession = human.profession

    if isinstance(profession, IHealable):
        profession.heal()
    elif isinstance(profession, IPaintable):
        profession.paint()
    elif isinstance(profession, IMusical):
        profession.play_music()
    else:
        human.perform_action()


def simulate(humans: list[Human]) -> None:
    print("=== Simulación de humanos ===\n")
    for human in humans:
        print(f"{human.name} ({human.age} años) — {human.profession.name}")
        human.perform_action()
    print()


def demonstrate_lsp(human: Human) -> None:
    """Cambio de profesión en tiempo de ejecución sin romper la simulación."""
    print("=== Demostración LSP: cambio de profesión ===\n")
    print(f"Antes: {human.profession.name}")
    human.perform_action()

    human.assign_profession(Musician())
    print(f"Después: {human.profession.name}")
    human.perform_action()
    print()


def main() -> None:
    humans = [
        Human("Alice", 30, Doctor()),
        Human("Bob", 25, Engineer()),
        Human("Carla", 28, Artist()),
        Human("Diego", 40, Teacher()),
        Human("Elena", 22, Musician()),  # extensión OCP
    ]

    simulate(humans)

    print("=== Acciones especializadas vía ISP ===\n")
    run_specialized_action(humans[0])
    run_specialized_action(humans[2])
    run_specialized_action(humans[4])
    print()

    demonstrate_lsp(Human("Frank", 35, Doctor()))


if __name__ == "__main__":
    main()
