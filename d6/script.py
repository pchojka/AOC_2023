


def get_win_value(race):
    win_values = []
    race_time = int(race.split(',')[0])
    race_dist = int(race.split(',')[1])

    for i in range (1, race_time):
        distanceTraveled = i * (race_time-i)
        if distanceTraveled > race_dist:
            win_values.append(i)
    return len(win_values)


def script():
    result = 0
    with open('input.txt','r') as readfile:
        line = readfile.readline()
        races = [d for d in line.split(';')]
        for race in races:
            nb_win = get_win_value(race)
            print(nb_win)
            if result == 0:
                result = nb_win
            else:
                result *= nb_win
            print(result)

script()