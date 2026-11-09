# Python OOP - Turn-Based Battle Simulation

A command-line interface (CLI) turn-based battle simulation developed in Python to demonstrate core Object-Oriented Programming (OOP) principles through a clean, modular architecture.

## Implemented OOP Concepts
* **Modular Architecture:** Classes and game execution logic are separated into distinct modules (`character.py`, `heroes.py`, `main.py`).
* **Encapsulation:** Character health points (`__hp`) are kept private to prevent unauthorized external modification. State changes are strictly managed via class methods (`take_damage()`, `is_alive()`).
* **Inheritance:** Specialized hero classes (`Warrior` and `Mage`) inherit core attributes and behaviors from the base `Character` class.
* **Polymorphism & Method Overriding:** Methods such as `attack()`, `take_damage()`, and `show_stats()` are overridden and customized according to each character class's unique mechanics (armor damage mitigation for Warriors, mana consumption and spell boosting for Mages).

## How to Run
1. Clone the repository:

    git clone https://github.com/kerembass/Python-oop-RPG-GamePrototype.git

2. Navigate to the project directory and run `main.py`:

    python main.py

