import sys
from collections import deque


def get_scores(lines) -> [int]:
    scores = []
    for line in lines:
        prefix, rest = line.split(':')
        winning_line, drawn_line = rest.split('|')
        winning_numbers = set(int(x) for x in winning_line.strip().split(' ')   if x)
        drawn_numbers   = set(int(x) for x in drawn_line.strip().split(' ')     if x)
        score = len(winning_numbers & drawn_numbers)
        scores.append(score)
    return scores


def count_cards(scores) -> int:
    num_cards = len(scores)
    copies = deque()
    for index, score in enumerate(scores):
        for i in range(score):
            copies.append(index+1+i)
    while copies:
        num_cards += 1
        index = copies.popleft()
        score = scores[index]
        for i in range(score):
            copies.append(index+1+i)
    return num_cards


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    scores = get_scores(lines)
    print(count_cards(scores))
