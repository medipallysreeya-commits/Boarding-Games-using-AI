import random

# ------------------ PLAYER ------------------

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.score = 0
        self.keys = 0
        self.treasure_pieces = 0
        self.inventory = []

    def show_status(self):
        print("\n" + "=" * 40)
        print(f"Player: {self.name}")
        print(f"Health: {self.health}")
        print(f"Score: {self.score}")
        print(f"Keys: {self.keys}")
        print(f"Treasure Pieces: {self.treasure_pieces}/5")
        print(f"Inventory: {self.inventory}")
        print("=" * 40)

# ------------------ CHEST ------------------

class Chest:
    def __init__(self):
        self.type = random.choice([
            "gold",
            "trap",
            "key",
            "artifact",
            "treasure_piece"
        ])

    def open(self, player):

        if self.type == "gold":
            gold = random.randint(10, 50)
            player.score += gold
            print(f"\n💰 You found {gold} gold!")

        elif self.type == "trap":
            damage = random.randint(10, 30)
            player.health -= damage
            print(f"\n☠️ Trap activated! Lost {damage} health!")

        elif self.type == "key":
            player.keys += 1
            print("\n🔑 You found a key!")

        elif self.type == "artifact":
            artifact = random.choice([
                "Golden Skull",
                "Ancient Coin",
                "Crystal Orb",
                "Pirate Compass"
            ])
            player.inventory.append(artifact)
            player.score += 20
            print(f"\n✨ Artifact Found: {artifact}")

        elif self.type == "treasure_piece":
            player.treasure_pieces += 1
            player.score += 50
            print("\n🧩 Legendary Treasure Piece Found!")

# ------------------ LOCATION ------------------

class Location:
    def __init__(self, name):
        self.name = name
        self.chests = random.randint(1, 3)

    def explore(self, player):
        print(f"\n📍 Exploring {self.name}")

        for i in range(self.chests):
            print(f"\nChest {i+1} Found!")

            choice = input("Open chest? (y/n): ").lower()

            if choice == 'y':
                chest = Chest()
                chest.open(player)
            else:
                print("You skipped the chest.")

# ------------------ GAME ENGINE ------------------

class GameEngine:

    def __init__(self):
        self.locations = [
            "Pirate Cove",
            "Forgotten Temple",
            "Dark Forest",
            "Ancient Ruins",
            "Crystal Cave",
            "Lost Island",
            "Hidden Fortress",
            "Sunken Harbor"
        ]

    def start(self):

        print("\n🏴‍☠️ TREASURE OR TRAP 🏴‍☠️")

        name = input("Enter player name: ")

        player = Player(name)

        while True:

            if player.health <= 0:
                print("\n☠️ GAME OVER!")
                print("You died while searching for treasure.")
                break

            if player.treasure_pieces >= 5:
                print("\n🏆 CONGRATULATIONS!")
                print("You assembled the Legendary Treasure!")
                print(f"Final Score: {player.score}")
                break

            player.show_status()

            print("\nChoose a location:\n")

            for i, loc in enumerate(self.locations):
                print(f"{i+1}. {loc}")

            print("0. Quit")

            try:
                choice = int(input("\nEnter choice: "))

                if choice == 0:
                    print("\nThanks for playing!")
                    break

                if 1 <= choice <= len(self.locations):

                    selected = Location(
                        self.locations[choice - 1]
                    )

                    selected.explore(player)

                else:
                    print("Invalid choice!")

            except:
                print("Enter a valid number!")

# ------------------ MAIN ------------------

if __name__ == "__main__":
    game = GameEngine()
    game.start()