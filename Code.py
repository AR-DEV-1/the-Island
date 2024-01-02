# A simple text-based survival game
# This is Bing

# Import the random module
import random

# Define some variables
inventory = [] # The player's inventory
resources = {"wood": 0, "stone": 0, "food": 0, "water": 0} # The available resources
items = {"axe": {"wood": 3, "stone": 2}, "knife": {"wood": 1, "stone": 1}, "fire": {"wood": 5}, "shelter": {"wood": 10, "stone": 5}, "fishing rod": {"wood": 2, "string": 1}} # The craftable items
health = 100 # The player's health
hunger = 0 # The player's hunger
thirst = 0 # The player's thirst
day = 1 # The current day
game_over = False # A flag to indicate if the game is over

# Define some functions
def print_status():
  # Print the current status of the player and the island
  global inventory
  global resources
  global health
  global hunger
  global thirst
  global day
  print("Day", day)
  print("Health:", health)
  print("Hunger:", hunger)
  print("Thirst:", thirst)
  print("Inventory:", inventory)
  print("Resources:", resources)

def get_input():
  # Get the user input and validate it
  global game_over
  command = input("What do you want to do? ").lower()
  valid_commands = ["explore", "collect", "craft", "eat", "drink", "rest", "quit"]
  if command == "":
    print("Please enter a command.")
    return None
  elif command == "quit":
    print("You quit the game.")
    game_over = True
    return None
  else:
    if command not in valid_commands:
      print("Please enter a valid command.")
      return None
    else:
      return command

def explore():
  # Explore the island and find random resources or events
  global resources
  global health
  global hunger
  global thirst
  global day
  print("You explore the island.")
  chance = random.randint(1,10)
