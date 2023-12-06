import sys

if __name__ == "__main__":
    lines = sys.stdin.readlines()
    time =     int(lines[0].split(":")[1].strip().replace(" ", ""))
    record_distance = int(lines[1].split(":")[1].strip().replace(" ", ""))


    ways = 0
    for charge_time in range(1, time):
        time_left = time - charge_time
        initial_speed = charge_time
        distance = initial_speed * time_left
        if distance > record_distance:
            ways +=1
    
    print(ways)