import csv
import re
ref = {
    'max_green': 13,
    'max_red': 12,
    'max_blue': 14
}

def script():
    games = []
    count = 0
    with open('input.csv', 'r') as readfile:
        filereader = csv.reader(readfile, delimiter=';')
        for row in filereader:
            max_blue = max_red = max_green = 0
            elements = []
            for el in row:
                for m in re.finditer(r"[0-9]+ (blue|green|red)", el):
                    elements.append(m.group(0))

            el: str
            for el in elements:
                print(el)
                if el.find('blue') != -1:
                    if int(el.replace(' blue', '')) > max_blue:
                        max_blue = int(el.replace(' blue', ''))
                if el.find('green') != -1:
                    if int(el.replace(' green', '')) > max_green:
                        max_green = int(el.replace(' green', ''))
                if el.find('red') != -1:
                    if int(el.replace(' red', '')) > max_red:
                        max_red = int(el.replace(' red', ''))
            games.append({
                'id': int(row[0].split(':')[0].replace("Game ", "")),
                'max_red': max_red,
                'max_green': max_green,
                'max_blue': max_blue
            })
    for game in games:
        if game['max_red'] <= ref['max_red'] and game['max_blue'] <= ref['max_blue'] and game['max_green'] <= ref['max_green']:
            print(f"GAME {game['id']} : POSSIBLE")
            count+= int(game['id'])
        else:
            print(f"GAME {game['id']}: IMPOSSIBLE")
    
    print(count)

            
            


script()