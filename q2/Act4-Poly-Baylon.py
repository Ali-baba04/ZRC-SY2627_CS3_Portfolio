
class HealthPotion:
    def use(self):
        print("You regain 50 HP!")

class ManaPotion:
    def use(self):
        print("You restore 30 MP!")

class SpeedBoost:
    def use(self):
        print("Your speed increases for 10 seconds!")

def apply_item(item):
    item.use()

# Create one object of each class
health = HealthPotion()
mana = ManaPotion()
speed = SpeedBoost()

# Store the objects in a list
items = [health, mana, speed]

# Use a loop to apply each item
for item in items:
    apply_item(item)