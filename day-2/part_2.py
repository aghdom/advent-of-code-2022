INPUT_FILE = "input_2.txt"

SYMBOL_TO_SHAPE = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
}

SYMBOL_TO_OUTCOME = {"X": "loss", "Y": "draw", "Z": "win"}


# X: Y - If opponent has X, I need to pick Y to lose
LOSS_STATES = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

# X: Y - If opponent has X, I need to pick Y to win
WIN_STATES = {"rock": "paper", "paper": "scissors", "scissors": "rock"}


def decide_player_shape(opponent: str, outcome: str) -> str:
    match outcome:
        case "draw":
            return opponent
        case "win":
            return WIN_STATES[opponent]
        case "loss":
            return LOSS_STATES[opponent]


def solve():
    total_score = 0
    with open(INPUT_FILE, "r") as input_file:
        for row in input_file:
            round_score = 0
            row = row.strip("\n")
            symbols = row.split(" ")
            opponent_shape = SYMBOL_TO_SHAPE[symbols[0]]
            outcome = SYMBOL_TO_OUTCOME[symbols[1]]
            player_shape = decide_player_shape(opponent_shape, outcome)
            match player_shape:
                case "rock":
                    round_score += 1
                case "paper":
                    round_score += 2
                case "scissors":
                    round_score += 3
            match outcome:
                case "win":
                    round_score += 6
                case "draw":
                    round_score += 3
                case "loss":
                    pass
            print(f"{player_shape} {opponent_shape}: {outcome} - {round_score}")
            total_score += round_score
    print(total_score)


if __name__ == "__main__":
    solve()
