import sys


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    
    seeds = [int(x) for x in lines[0].split(':')[1].strip().split(' ')]
    
    ranges = {}
    i = 2
    while i < len(lines):
        name = lines[i].split(' ')[0]
        current_ranges = []
        i += 1
        while i < len(lines) and lines[i].strip():
            destination, source, length = [int (x) for x in lines[i].strip().split(' ')]
            current_ranges.append([source, destination, length])
            i += 1
        ranges[name] = sorted(current_ranges)
        i += 1
    
    steps = [
        "seed-to-soil",
        "soil-to-fertilizer",
        "fertilizer-to-water",
        "water-to-light",
        "light-to-temperature",
        "temperature-to-humidity",
        "humidity-to-location"
    ]
    locations = []
    for seed in seeds:
        value = seed
        for step in steps:
            for r in ranges[step]:
                source, destination, length = r
                if source <= value <= source + length:
                    value = destination + (value - source)
                    break
                if source > value:
                    break
        locations.append(value) 
    
    print(min(locations)) 
