import pandas as pd
from scipy.stats import beta

# Data for the games
data = {
    "Date": ["Aug 30", "Sep 06", "Sep 13", "Sep 20", "Sep 03, 2021", "Sep 10, 2021", "Sep 17, 2021", "Sep 24, 2021", "Sep 30, 2021", "Oct 08, 2021", "Oct 15, 2021", "Oct 22, 2021", "Oct 29, 2021", "Nov 05, 2021"],
    "Opponent": ["Tamalpais", "Monte Vista", "McClymonds", "Cardinal Newman", "San Ramon Valley", "El Cerrito", "St. Mary's", "Castlemont", "Liberty", "Hayward", "Moreau Catholic", "Piedmont", "James Logan", "San Leandro"],
    "Result": ["Win", "Win", "Loss", "Loss", "Loss", "Loss", "Loss", "Win", "Loss", "Win", "Win", "Win", "Loss", "Loss"],
    "Score": ["51 - 13", "24 - 20", "14 - 28", "0 - 56", "7 - 34", "14 - 27", "6 - 42", "41 - 12", "14 - 42", "46 - 6", "49 - 13", "31 - 8", "7 - 42", "10 - 33"],
    "Opponent Wins": [None, 6, 12, 10, 8, 9, 11, 3, 7, 1, 5, 8, 6, 4]
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Function to calculate O'dowd's chance of winning
def calculate_chance_of_winning(opponent_wins, prior_wins=1, prior_losses=1):
    # Filter games based on opponent wins
    relevant_games = df[df["Opponent Wins"] == opponent_wins]

    # Count wins and losses
    wins = (relevant_games["Result"] == "Win").sum()
    losses = (relevant_games["Result"] == "Loss").sum()

    # Apply the Beta distribution with prior wins/losses
    posterior_alpha = prior_wins + wins
    posterior_beta = prior_losses + losses

    # Posterior mean (expected probability of winning)
    chance_of_winning = beta.mean(posterior_alpha, posterior_beta)

    return chance_of_winning

# Sample calculation
opponent_wins_input = int(input("Enter the number of games the opponent has won: "))  # Example input from user
chance_of_winning = calculate_chance_of_winning(opponent_wins_input)

print(f"Chance of winning against an opponent with {opponent_wins_input} wins: {chance_of_winning:.2f}")
