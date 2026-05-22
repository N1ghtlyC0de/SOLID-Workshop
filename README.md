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

- Un cambio en cómo actúa un Doctor no obliga a modificar `Human`.
- `Human` tiene una sola razón para cambiar: datos o reglas de la persona, no de las profesiones.
- Facilita pruebas unitarias: se puede probar `Doctor.heal()` sin instanciar un humano completo.
- Evita una clase “Dios” con métodos `heal()`, `build()`, `paint()` mezclados.

---

## b) Open/Closed Principle (OCP)

**Implementación:** Para agregar `Musician` solo se creó `professions/musician.py` e `IMusical` en `actions.py`. No se modificó `Human`, `Doctor`, `Engineer` ni el flujo principal de `main.py` más allá de registrar el nuevo tipo en la lista de demostración.

**Discusión — ¿Cómo permite tu diseño una extensión fácil?**

- Nuevas profesiones implementan `Profession` y las interfaces de acción que necesiten.
- El simulador trabaja con `Profession`, no con tipos concretos.
- Se cumple “abierto a extensión, cerrado a modificación”: extender sin tocar clases estables.

---

## c) Liskov Substitution Principle (LSP)

**Implementación:** `assign_profession()` acepta cualquier subtipo de `Profession`. Un `Doctor` puede sustituirse por un `Musician` en el mismo `Human` y `perform_action()` sigue funcionando.

**Discusión — ¿Qué violaría LSP en este diseño?**

- Una subclase que lance excepción en `perform_action()` cuando se espera comportamiento normal.
- `Doctor` que no pueda “actuar” como `Profession` (por ejemplo, `perform_action()` que no hace nada o rompe invariantes).
- Forzar en la jerarquía métodos que las subclases no pueden cumplir (p. ej. un `Intern` que “cura” pero está prohibido por reglas de negocio y lanza error).
- Cambiar contratos de la clase base (precondiciones más fuertes o postcondiciones más débiles en hijos).

---

## d) Interface Segregation Principle (ISP)

**Implementación:** Interfaces pequeñas: `IHealable`, `IBuildable`, `IPaintable`, `ITeachable`, `IMusical`. `Doctor` solo implementa `IHealable`; no está obligado a implementar `paint()` ni `play_music()`.

**Discusión — ¿Cómo mejora ISP la flexibilidad del código?**

- Las clases no cargan métodos que no usan (“interfaces gordas”).
- Se puede componer comportamiento: una profesión futura podría implementar varias interfaces si lo necesita.
- El código cliente (`run_specialized_action`) consulta capacidades con `isinstance`, no asume que todas las profesiones hacen lo mismo.

---

## e) Dependency Inversion Principle (DIP)

**Implementación:** `Human` depende de `Profession` (abstracción), no de `Doctor` o `Engineer`. Las profesiones concretas dependen de las interfaces en `interfaces/`.

**Discusión — ¿Cómo ayuda DIP con pruebas y extensión?**

- En pruebas se puede inyectar un `Profession` falso (mock) sin tocar `Human`.
- El módulo de alto nivel (`Human`) no se acopla a detalles de bajo nivel (clases concretas).
- Nuevas profesiones se conectan por contrato, no por modificar dependencias internas de `Human`.

---

## Reto de extensión — Musician

**Acción:** `play_music()` → salida: `Playing music.`

**Reflexión — ¿Qué principios SOLID facilitaron la extensión?**

| Principio | Rol en la extensión |
|-----------|---------------------|
| **OCP** | Se agregó `Musician` sin editar profesiones existentes |
| **DIP** | `Human` ya dependía de `Profession`; solo se pasó `Musician()` |
| **ISP** | Solo se añadió `IMusical`, no una interfaz monolítica |
| **LSP** | `Musician` se usa igual que `Doctor` en la simulación |
| **SRP** | La lógica musical quedó aislada en su propia clase |

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
