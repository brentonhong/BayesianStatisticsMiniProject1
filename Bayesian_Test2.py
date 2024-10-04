import numpy as np
from scipy.stats import beta

# Historical data (wins and losses)
wins = 6 
losses = 8  

# Initialize prior based on historical win/loss data
# Beta distribution prior: Beta(wins + 1, losses + 1)
prior_alpha = wins + 1
prior_beta = losses + 1

# Function to calculate the posterior probability of winning
def calculate_win_probability(opponent_wins):
    # Update the Beta prior based on the opponent's performance
    # For simplicity, assume the likelihood of winning is inversely proportional to opponent wins
    # The more games the opponent has won, the less likely o'dowd will win.
    likelihood_factor = 1 / (opponent_wins + 1)  # Likelihood decreases with opponent wins
    updated_alpha = prior_alpha * likelihood_factor
    updated_beta = prior_beta * (1 - likelihood_factor)
    
    # Posterior Beta distribution
    posterior = beta(updated_alpha, updated_beta)
    
    # Calculate expected win probability from the posterior
    win_probability = posterior.mean()
    return win_probability

# Main program
def main():
    opponent_wins = int(input("Enter the number of games the opponent has won: "))
    
    # Calculate the win probability
    win_prob = calculate_win_probability(opponent_wins)
    
    print(f"The estimated probability of the school winning is: {win_prob:.2f}")

if __name__ == "__main__":
    main()
5