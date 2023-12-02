import sys
from collections import namedtuple

RGB = namedtuple('RGB', ['red', 'green', 'blue'])
Game = namedtuple('Game', ['id', 'rgb'])

def parse_game(line) -> Game:
    game_line, draws_line = line.split(':')
    _, game_id = game_line.split(' ')
    draws = draws_line.split(';')
    rgbs = []
    for draw in draws:
        color_lines = draw.split(',')
        rgb = RGB(0,0,0)._asdict()
        for color_line in color_lines:
            number,color = color_line.strip().split(' ')
            rgb[color] = int(number)
        rgbs.append(RGB(**rgb))
    rgb_values = tuple(zip(*rgbs))
    rgb = RGB(max(rgb_values[0]), max(rgb_values[1]), max(rgb_values[2]))
    return Game(int(game_id), rgb)


def is_game_possible(game: Game, max_cubes: RGB) -> bool:
    return all( a <= b for (a,b) in zip(game.rgb, max_cubes))

if __name__ == "__main__":
    max_cubes = RGB(12,13,14)
    lines = sys.stdin.readlines()
    games = [parse_game(line) for line in lines]
    possible_games = [game for game in games
                           if is_game_possible(game, max_cubes)]
    print(sum(game.id for game in possible_games))
