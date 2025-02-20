import pickle

class Game:
    def __init__(self, level, score):
        self.level = level
        self.score = score

    def save_state(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @staticmethod
    def load_state(filename):
        with open(filename, "rb") as file:
            return pickle.load(file)

# Create a Game
game = Game(5, 1000)

# Save state
game.save_state("game_state.pkl")

# Load state
loaded_game = Game.load_state("game_state.pkl")
print("Loaded Game state:")
print(f"Level: {loaded_game.level}, Score: {loaded_game.score}")









# 9. Restoring Object State:
#    - Saved and restored the state of a Game object.
#    - Used Pickle for simplicity.

