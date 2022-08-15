ROCK = "r"
PAPER = "p"
SCISSORS = "s"

gambits = [ROCK, PAPER, SCISSORS]

score = 0

DRAW = 0
WIN = 1
LOSE = -1

def find_status(user_gambit, cpu_gambit):
    status = -5
    if user_gambit == ROCK:
        if cpu_gambit == ROCK:
            status = DRAW
        elif cpu_gambit == PAPER:
            status = LOSE
        else:
            status = WIN
    elif user_gambit == PAPER:
        if cpu_gambit == ROCK:
            status = WIN
        elif cpu_gambit == PAPER:
            status = DRAW
        else:
            status = LOSE
    elif user_gambit == SCISSORS:
        if cpu_gambit == ROCK:
            status = LOSE
        elif cpu_gambit == PAPER:
            status = WIN
        else:
            status = DRAW
    return status


def get_score(status):
    global score
    if status == DRAW:
        score += 0
    elif status == LOSE:
        score -= 1
    else:
        score += 1

