INPUT_FILE = "input_2.txt"

SYMBOL_TO_SHAPE = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}

WIN_STATES = [("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")]


def decide_outcome(player: str, opponent: str) -> str:
    if player == opponent:
        return "draw"
    elif (player, opponent) in WIN_STATES:
        return "win"
    else:
        return "loss"


def solve():
    total_score = 0
    with open(INPUT_FILE, "r") as input_file:
        for row in input_file:
            round_score = 0
            row = row.strip("\n")
            symbols = row.split(" ")
            player_shape = SYMBOL_TO_SHAPE[symbols[1]]
            opponent_shape = SYMBOL_TO_SHAPE[symbols[0]]
            match player_shape:
                case "rock":
                    round_score += 1
                case "paper":
                    round_score += 2
                case "scissors":
                    round_score += 3

            outcome = decide_outcome(player_shape, opponent_shape)
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
