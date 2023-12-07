from maps import RangeMap
import sys


def script():
    seeds = []
    maps : [RangeMap] = []
    current_map: RangeMap = None
    locations : [int] = []
    with open('input.txt', 'r') as readfile:
        lines = readfile.readlines()
        count = 1
        for line in lines:
            try:
                if line.count('seeds') != 0:
                    seeds = [d for d in str(line.replace('\n', '').split(': ')[1]).split(' ')]
                elif line == '\n':
                    if current_map != None:
                        maps.append(current_map)
                        current_map = None
                    else:
                        continue
                elif line.count('map') != 0:
                    src = line.split('-to-')[0]
                    dst = line.split('-to-')[1].split(' ')[0]
                    current_map = RangeMap(src, dst)
                else:
                    range = line.split(' ')
                    current_map.add_sub_range(range)
            except TypeError as err:
                print(f"ERROR on line {count} : {err}")
        for seed in seeds:
            payload = {
                'type': 'seed',
                'value': int(seed)
            }
            print(payload)
            for map in maps:
                payload = map.process_input(payload['type'], payload['value'])
                print(payload)
                if payload['type'] == 'location':
                    locations.append(payload['value'])

    print(min(locations))


script()