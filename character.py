class Character:
    """Base class representing a generic game character."""

    def __init__(self, name,hp,attack_power):
        self.name = name
        # Encapsulation: __hp is private to prevent direct external modification
        self.__hp = hp
        self.attack_power = attack_power

    def show_stats(self):
        """Displays the basic statistics of the character."""
        print(f"Name: {self.name} | HP: {self.__hp} | Attack: {self.attack_power}")

    def take_damage(self,damage):
        """Reduces character's HP by the damage amount, ensuring HP doesn't drop below 0."""
        self.__hp -= damage
        if self.__hp <= 0:
            self.__hp = 0

    def is_alive(self):
        """Returns True if the character's HP is greater than 0, False otherwise."""
        return self.__hp > 0