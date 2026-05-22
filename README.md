# Taller SOLID — Simulación de humanos en videojuego

Implementación del taller de principios SOLID (Ingeniería de Software II, Universidad Nacional de Colombia). Simulación de humanos con distintas profesiones y comportamientos extensibles.

**Integrantes:** Andrés Felipe Rosada · Pablo Esteban Olaya Arias

---

## Estructura del proyecto

```
solid-lab/
├── interfaces/
│   ├── profession.py    # Abstracción Profession (DIP)
│   └── actions.py       # IHealable, IBuildable, IPaintable, etc. (ISP)
├── models/
│   └── human.py         # Solo name y age (SRP)
├── professions/
│   ├── doctor.py
│   ├── engineer.py
│   ├── artist.py
│   ├── teacher.py
│   └── musician.py      # Reto de extensión (OCP)
├── main.py
└── README.md
```

---

## a) Single Responsibility Principle (SRP)

**Implementación:** La clase `Human` solo almacena y expone datos genéricos (`name`, `age`) y delega el comportamiento profesional a un objeto `Profession`. Cada profesión (`Doctor`, `Engineer`, etc.) vive en su propio archivo y encapsula su lógica.

**Discusión — ¿Por qué es mejor separar la lógica de profesión de la entidad humano?**

- Porque evita que la clase `Human` esté anidada a la lógica de las clases para las profesiones. Esto asegura el cumplimiento de la SRP, ya que limita a la clase de los humanos a manejar exclusivamente el nombre y edad de la persona, y dicha clase no se verá afectada en el caso que se quieran modificar los métodos pertenecientes a las profesiones. 
---

## b) Open/Closed Principle (OCP)

**Implementación:** Para agregar `Musician` solo se creó `professions/musician.py` e `IMusical` en `actions.py`. No se modificó `Human`, `Doctor`, `Engineer` ni el flujo principal de `main.py` más allá de registrar el nuevo tipo en la lista de demostración.

**Discusión — ¿Cómo permite tu diseño una extensión fácil?**

- Debido a que se cumple con el principio de “abierto a extensión, cerrado a modificación”, añadir nuevas profesiones no requiere de la modificación de las clases ya existentes. Esto es de gran ayuda, ya que garantiza que el sistema pueda crecer de manera ordenada al mantener la estabilidad del código ya existente, lo que reduce el riesgo de introducir errores si se llega a añadir nuevas funcionalidades (por ejemplo, la adición de la profesión `Musician`).

---

## c) Liskov Substitution Principle (LSP)

**Implementación:** `assign_profession()` acepta cualquier subtipo de `Profession`. Un `Doctor` puede sustituirse por un `Musician` en el mismo `Human` y `perform_action()` sigue funcionando.

**Discusión — ¿Qué violaría LSP en este diseño?**

- El LSP se vería comprometido si una subclase de `Profession` altera el comportamiento esperado por el sistema. Por ejemplo, al retornar tipos de datos inesperados, lanzar excepciones no controladas o imponer nuevas condiciones que el método `perform_action()` no anticipaba. 

---

## d) Interface Segregation Principle (ISP)

**Implementación:** Interfaces pequeñas: `IHealable`, `IBuildable`, `IPaintable`, `ITeachable`, `IMusical`. `Doctor` solo implementa `IHealable`; no está obligado a implementar `paint()` ni `play_music()`.

**Discusión — ¿Cómo mejora ISP la flexibilidad del código?**

- La flexibilidad del código se ve mejorada ya que la ISP implica que el sistema evita la carga de métodos innecesarios a clases que no las requieren. Esto da paso a que el sistema se comporte de manera modular, en el cual cada clase implementa únicamente las interfaces que necesita, y una nueva profesión puede combinar varias interfaces si lo requiere.

---

## e) Dependency Inversion Principle (DIP)

**Implementación:** `Human` depende de `Profession` (abstracción), no de `Doctor` o `Engineer`. Las profesiones concretas dependen de las interfaces en `interfaces/`.

**Discusión — ¿Cómo ayuda DIP con pruebas y extensión de tu simulación?**

- Ayuda al permitir que el código sea más flexible y desacoplado, lo que facilita cambiar implementaciones sin afectar otras partes de la base de código. Esto significa que se pueden inyectar implementaciones falsas (mocks) de la interfaz `Profession` sin necesidad de modificar la clase `Human`. 

---

## Reto de extensión — Musician

**Acción:** `play_music()` → salida: `Playing music.`

**Reflexión — ¿Qué principios SOLID facilitaron la extensión?**

| Principio | Rol en la extensión |
|-----------|---------------------|
| **SRP** | La lógica musical quedó aislada en su propia clase`Musician`. No se mezcló con `Human`. |
| **OCP** | Se agregó `Musician` sin editar ninguna de las profesiones existentes, ni alterar la clase `Human`. |
| **LSP** | `Musician` se usa exactamente igual que `Doctor` en la simulación. Puede pasarse al constructor de `Human` de forma transparente y el método `perform_action()` corre sin romper el programa. |
| **ISP** | Solo se añadió `IMusical` y `Playable`, la cual no es una interfaz monolítica. Evita que las demás profesiones tengan que arrastrar el método `playMusic()`. |
| **DIP** | `Human` ya dependía de la abstracción `Profession`; solo se le pasó la instancia `Musician()`. |

---

## Discusión grupal

**Desafíos comunes:**

- Diseño inicial con todo en una sola clase `Human`.
- Decidir entre herencia y composición para profesiones.
- Evitar interfaces demasiado grandes o demasiado fragmentadas.

**Cómo ayudaron los principios SOLID:**

- Código más legible, modular y preparado para nuevas profesiones (Chef, Pilot, etc.).
- Menor riesgo de regresiones al extender.

**Mejoras futuras:**

- Patrón Strategy o Factory para crear profesiones por nombre/config.
- Persistencia y eventos de juego desacoplados (otro SRP).
- Tests automatizados con mocks de `Profession`.

---

## Conclusiones

1. **SRP** mantiene cada clase enfocada en un solo concepto.
2. **OCP** permite crecer el sistema agregando clases, no editando las estables.
3. **LSP** garantiza que los subtipos sean intercambiables sin sorpresas.
4. **ISP** evita contratos innecesarios entre componentes.
5. **DIP** invierte dependencias hacia abstracciones, mejorando mantenimiento y pruebas.

Estos principios, aplicados juntos, producen un diseño extensible para simulaciones, APIs y cualquier dominio orientado a objetos.

---

## Ejecución

Requisito: Python 3.10+

```bash
python3 main.py
```

Salida esperada:

```
=== Simulación de humanos ===

Alice (30 años) — Doctor
Healing a patient.
Bob (25 años) — Engineer
Building a bridge.
...
```
