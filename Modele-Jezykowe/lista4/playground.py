# text = """When we think of tasty food, one thing is clear. Savory dishes are a universal joy. Crispy fries with a creamy dip, tangy sauces that bring out the zest, and spicy notes that dance on your tongue. Let’s not forget desserts that melt in your mouth with every bite, from rich chocolate brownies to silky cheesecakes. When you bite into these treats, it’s as if time stops for a second. The flavors come alive, making each moment an unforgettable experience.

# The best part about food is its diversity, bringing together a world of flavors in every dish. Sushi rolls, wrapped with a hint of sea salt, pasta simmered in fresh tomatoes and basil, or perfectly seasoned meats grilled to perfection—each meal carries its unique charm.

# Whether it’s breakfast, lunch, or dinner, every meal has its magic. Freshly baked bread with a dab of butter, the crunch of a garden salad, or the simple joy of a cup of coffee with a hint of cinnamon. Food is a celebration for the senses, and every bite is a new story just waiting to be told."""

# code = ""

# for c in text:
#     if c == ".":
#         code += "."
#     elif c == ",":
#         code += "-"
#     elif c == "\n":
#         code += "/"


t = """
A combustion engine converts fuel into mechanical energy through a series of controlled explosions. The process begins with the intake stroke, where air and fuel mix inside the cylinder. The piston moves down, creating a vacuum that draws in this mixture. After the intake, the piston moves back up to compress the air-fuel mixture, increasing its temperature and pressure. Combustion occurs when the spark plug ignites the compressed mixture, causing an explosion. Kinetic energy from this explosion forces the piston down, turning the crankshaft and ultimately powering the vehicle. As the piston reaches the bottom of its stroke, the exhaust valve opens. This allows the spent gases from combustion to escape the cylinder. During the next cycle, the process repeats, with the engine continually drawing in fuel and air, igniting it, and expelling exhaust. Although different engine designs exist, the basic principles of operation remain consistent. With each cycle, the engine converts chemical energy in the fuel into mechanical energy, driving the vehicle forward. Numerous components, including the fuel system and ignition system, work together to ensure efficient operation."""
cleaned_string = ''.join(t.split())
snts = cleaned_string.split(".")
for s in snts:
    if s:
        print(s[0], end="")