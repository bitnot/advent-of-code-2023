import sys


def get_scores(lines) -> [int]:
    scores = []
    for line in lines:
        prefix, rest = line.split(':')
        winning_line, drawn_line = rest.split('|')
        winning_numbers = set(int(x) for x in winning_line.strip().split(' ')   if x)
        drawn_numbers   = set(int(x) for x in drawn_line.strip().split(' ')     if x)
        number_drawn_wins = len(winning_numbers & drawn_numbers)
        score = 2 ** (number_drawn_wins - 1) if number_drawn_wins else 0
        scores.append(score)
    return scores

if __name__ == "__main__":
    lines = sys.stdin.readlines()
    scores = get_scores(lines)
    print(sum(scores))
