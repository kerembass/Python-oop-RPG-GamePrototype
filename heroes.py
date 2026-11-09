from character import Character

# Inheritance: Warrior inherits attributes and methods from Character
class Warrior(Character):
    def __init__(self,name,hp,attack_power,armor):
        Character.__init__(self,name,hp,attack_power)
        self.armor = armor

    # Method Overriding: Custom damage calculation factoring in Warrior's armor
    def take_damage(self,damage):
        true_damage = damage - self.armor
        if true_damage < 0:
            true_damage = 0

        # Calling the parent class method to update the private __hp attribute
        Character.take_damage(self,true_damage)

    # Polymorphism: Warrior-specific attack implementation
    def attack(self,target):
        target.take_damage(self.attack_power)
        print(f"Warrior {self.name} dealt {self.attack_power} damage to target {target.name} with their sword! ")

    # Method Overriding: Extending show_stats to include armor
    def show_stats(self):
        Character.show_stats(self)
        print(f"Armor: {self.armor}")


# Inheritance: Mage inherits attributes and methods from Character
class Mage(Character):
    def __init__(self, name,hp,attack_power,magic):
        Character.__init__(self, name, hp, attack_power)
        self.magic = magic

    # Polymorphism: Mage-specific attack implementation using magic points
    def attack(self,target):
        if self.magic >= 20:
            self.magic -= 20
            target.take_damage(self.attack_power + 50)
            print(f"Mage {self.name} dealt {self.attack_power + 50} damage to target {target.name} with their spell!")
        else:
            # Fallback to basic attack if magic is insufficient
            target.take_damage(self.attack_power)
            print(f"Mage {self.name} dealt {self.attack_power} damage to target {target.name} with their spell!")

    # Method Overriding: Extending show_stats to include magic
    def show_stats(self):
        Character.show_stats(self)
        print(f"Magic: {self.magic}")