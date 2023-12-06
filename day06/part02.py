import sys, math

if __name__ == "__main__":
    lines = sys.stdin.readlines()
    time =     int(lines[0].split(":")[1].strip().replace(" ", ""))
    record_distance = int(lines[1].split(":")[1].strip().replace(" ", ""))

    """
    distance = charge_time * (time - charge_time)
    distance > record_distance
    charge_time * (time - charge_time) - record_distance > 0
    -charge_time**2 + time*charge_time - record_distance > 0
    Ax**2           + Bx               + c
    """
    a = -1
    b = time
    c = -record_distance
    D = b**2 - 4*a*c

    x1 = math.ceil( (-b + math.sqrt(D))/-2)
    x2 = math.floor((-b - math.sqrt(D))/-2)
    print(x2-x1+1)