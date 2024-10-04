import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
4
# Data: opponent wins and the school's game results (1 for win, 0 for loss)
opponent_wins = np.array([6, 12, 10, 8, 9, 11, 3, 7, 1, 5, 8, 6, 4])
game_results = np.array([1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0])  # 1 is win, 0 is loss

# Fit logistic regression model
log_reg = LogisticRegression()
log_reg.fit(opponent_wins.reshape(-1, 1), game_results)

# Function to predict the probability of winning based on opponent wins
def predict_win_probability(opponent_wins):
    win_prob = log_reg.predict_proba(np.array(opponent_wins).reshape(-1, 1))[:, 1]  # Probability of winning (class 1)
    return win_prob[0]

# Take user input for the number of games the opponent has won
opponent_win_input = int(input("Enter the number of games the opponent has won: "))

# Output the predicted probability of winning
win_probability = predict_win_probability(opponent_win_input)
print(f"The predicted probability of the school winning is: {win_probability * 100:.2f}%")

# Optional: Plot the probability curve for different opponent wins
x_values = np.arange(0, 15).reshape(-1, 1)  # Possible range of opponent wins
y_values = log_reg.predict_proba(x_values)[:, 1]

