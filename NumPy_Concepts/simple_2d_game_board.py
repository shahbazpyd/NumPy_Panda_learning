import numpy as np

# A standard Python list of lists representing a Tic-Tac-Toe board
python_board = [[0, 1, 0],
                [1, 0, 1],
                [0, 1, 0]]

# Convert the Python list to a 2d NumPy array (matrix)
game_board = np.array(python_board)

print("Game Board Matrix:")
print(game_board)
print(f"Shap: {game_board.shape}")

