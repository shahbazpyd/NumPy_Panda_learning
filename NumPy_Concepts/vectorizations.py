import numpy as np

scores = np.array([50, 60, 70, 80])
bonus_points = 5

# Vectorized Addition: 
# The operator '+' is applied to every element in 'scores'
new_scores = scores + bonus_points 

print(f"Original Scores: {scores}")
print(f"Scores with Bonus: {new_scores}")
# Output: [55 65 75 85]

# Vectorized Multiplication: Doubling the scores
doubled_scores = scores * 2
print(f"Doubled Scores: {doubled_scores}")
# Output: [100 120 140 160]