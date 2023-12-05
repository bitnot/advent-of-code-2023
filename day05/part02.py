import sys

if __name__ == "__main__":
    lines = sys.stdin.readlines()
    
    seed_line = [int(x) for x in lines[0].split(':')[1].strip().split(' ')]
    seed_ranges = sorted(list(zip(seed_line[::2], seed_line[1::2])))

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
    
    location_found = False
    location = -1
    while not location_found and location < 9_999_999_999:
        location += 1
        if location % (1_000_000) == 0:
            print(f"checking location {location}")
        value = location
        for step in reversed(steps):
            for r in ranges[step]:
                source, destination, length = r
                if destination <= value < destination + length:
                    value = source + (value - destination)
                    break
        for seed_range in seed_ranges:
            seed_start, seed_length = seed_range
            if seed_start <= value < seed_start + seed_length:
                location_found = True
                break

    print(f"min location={location}") 