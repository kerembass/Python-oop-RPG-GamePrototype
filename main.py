from heroes import Warrior, Mage

# Instantiate character objects
garen = Warrior("garen",200,40,50)
ryze = Mage("ryze",100,80,40)

# Main CLI battle loop: continues as long as both characters are alive
while garen.is_alive() and ryze.is_alive():
    choice = input("\n Choose your move (1: Attack 2:view statistics 3:EXIT)")

    if choice == "1":
        garen.attack(ryze)
        # Check if the target survived before allowing a counter-attack
        if ryze.is_alive():
            ryze.attack(garen)

    elif choice == "2":
        garen.show_stats()
        ryze.show_stats()
    elif choice == "3":
        print("\n The game is over")
        break
    else:
        print("\n Choose your move")

# Determine and announce the winner after the loop ends
if not garen.is_alive():
    print("\n ryze won the battle!")
elif not ryze.is_alive():
    print("\n garen won the battle!")
else:
    print("\nLeft the arena without a winner")

