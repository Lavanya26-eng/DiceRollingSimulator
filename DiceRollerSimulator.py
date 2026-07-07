import random

dice_faces = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"
    ),
    2: (
        "┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘"
    ),
    3: (
        "┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"
    ),
    4: (
        "┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"
    ),
    5: (
        "┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"
    ),
    6: (
        "┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘"
    )
}

print("=" * 40)
print("      🎲 Dice Rolling Simulator 🎲")
print("=" * 40)

while True:
    input("\nPress Enter to roll the dice...")

    number = random.randint(1, 6)

    print(f"\nYou rolled: {number}\n")

    for line in dice_faces[number]:
        print(line)

    again = input("\nRoll again? (y/n): ").lower()

    if again != 'y':
        print("\n🎉 Thanks for playing!")
        break