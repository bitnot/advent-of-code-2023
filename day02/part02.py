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

if __name__ == "__main__":
    lines = sys.stdin.readlines()
    games = [parse_game(line) for line in lines]
    powers = [game.rgb.red * game.rgb.green * game.rgb.blue
              for game in games]
    print(sum(powers))
