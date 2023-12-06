import sys, math

if __name__ == "__main__":
    lines = sys.stdin.readlines()
    times =     [int(t) for t in lines[0].split(":")[1].strip().split()]
    distances = [int(d) for d in lines[1].split(":")[1].strip().split()]
    races = zip(times, distances)
    # todo consider pre-computing/memoizing for max(time)
    ways = []
    for time, record_distance in races:
        w = 0
        for charge_time in range(1, time):
            time_left = time - charge_time
            initial_speed = charge_time
            distance = initial_speed * time_left
            if distance > record_distance:
                w +=1
        ways.append(w)
    print(math.prod(ways))