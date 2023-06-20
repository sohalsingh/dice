import random

def roll_dice():
    """Simulates rolling a six-sided dice."""
    return random.randint(1, 6)

# Example usage
result = roll_dice()
print(f"The dice rolled: {result}")
