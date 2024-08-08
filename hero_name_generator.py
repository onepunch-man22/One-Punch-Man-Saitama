import random

def generate_hero_name():
    # Lists of words to generate hero names
    adjectives = ["Mighty", "Invisible", "Thunder", "Cosmic", "Iron", "Shadow", "Blazing", "Atomic", "Lightning", "Giant"]
    nouns = ["Warrior", "Ninja", "Samurai", "Guardian", "Crusader", "Defender", "Champion", "Knight", "Master", "Titan"]
    
    # Get user input
    first_name = input("Enter your first name: ").capitalize()
    last_name = input("Enter your last name: ").capitalize()
    
    # Generate random hero name parts
    adj1 = random.choice(adjectives)
    adj2 = random.choice(adjectives)
    noun = random.choice(nouns)
    
    # Construct hero name
    hero_name = f"{adj1} {adj2} {noun}"
    
    # Output the hero name
    print(f"Hello {first_name} {last_name}, your One Punch Man universe hero name is: {hero_name}")

if __name__ == "__main__":
    generate_hero_name()
