from maps import RangeMap
import sys

def process_seeds(seeds):
    arr = []
    for i in range(0, len(seeds)-1, 2):
        arr.append({
            'type': 'seed',
            'min_value': int(seeds[i]),
            'max_value': int(seeds[i]) + int(seeds[i+1]) - 1
        })
    return arr

def process_pivot_value(seed_value, maps):
    payload = {
        'type': 'seed',
        'value': int(seed_value)
    }
    map: RangeMap
    for map in maps:
        payload = map.process_input(payload['type'], payload['value'])
        if payload['type'] == 'location':
            return payload['value']



def script():
    seeds = []
    maps : [RangeMap] = []
    current_map: RangeMap = None
    locations : [int] = []
    with open('test.txt', 'r') as readfile:
        lines = readfile.readlines()
        count = 1
        for line in lines:
            try:
                if line.count('seeds') != 0:
                    seeds = [d for d in str(line.replace('\n', '').split(': ')[1]).split(' ')]
                    seeds = process_seeds(seeds)
                    print(seeds)
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
            
            map: RangeMap
        for map in maps:
            map.process()
        print(maps)

        pivot = process_pivot_value(seeds[0]['min_value'], maps)
        print(f"PIVOT VALUE : {pivot}")

        for seed in seeds:
            for map in maps:
                payload = map.process_input_range(seed['type'], seed['min_value'], seed['max_value']) 
        # for seed in seeds:
        #     for map in maps:
                
        #         payload = map.process_input(payload['type'], payload['value'])
        #         print(payload)
        #         if payload['type'] == 'location':
        #             locations.append(payload['value'])

    #print(min(locations))


script()