import pickle

class GameV1:
    def __init__(self, level, score):
        self.level = level
        self.score = score

class GameV2:
    def __init__(self, level, score, player_name):
        self.level = level
        self.score = score
        self.player_name = player_name

    @staticmethod
    def from_v1(v1_game, player_name):
        return GameV2(v1_game.level, v1_game.score, player_name)

# Simulate an old version
game_v1 = GameV1(5, 1000)

# Save V1 game
with open("game_v1.pkl", "wb") as file:
    pickle.dump(game_v1, file)

# Load and upgrade to V2
with open("game_v1.pkl", "rb") as file:
    loaded_game_v1 = pickle.load(file)
    game_v2 = GameV2.from_v1(loaded_game_v1, "Alice")

print("Upgraded GameV2 object:")
print(f"Level: {game_v2.level}, Score: {game_v2.score}, Player: {game_v2.player_name}")





# 10. Versioning Serialized Objects:
#     - Handled version changes in a Game class.
#     - Added a version attribute and upgrade logic.

