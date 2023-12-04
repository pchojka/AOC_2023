
def script():
    data = []
    with open('input.txt', 'r') as readfile:
        lines = readfile.readlines()
        for line in lines:
            data.append(parse_line(line))
        print(data)
        process_matrix(data)
    return


def process_matrix(data):
    line_count = 0
    el_count = 0
    numbers = 0
    for line in data:
        for el in line:
            if el['type'] == 'operator':
                print(f'Operator detected [{line_count}, {el["index"]}], parsing adjacent lines')
                adj = get_adjacent_numbers(line_count, el['index'], data)
                for result in adj:
                    numbers+=int(result)
            el_count+=1
            
        line_count+=1
    print(numbers)

def get_adjacent_numbers(x, y, data):
    numbers = []
    res= []
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
             results = is_a_number(i,j, data)
             numbers.extend(results)

    for sublist in numbers:
        if sublist not in res:
            res.append(sublist)
    return res



def is_a_number(x, y, data: list):
    numbers = []
    print(f"CALLING WITH X= {x}, Y={y}")
    previous_line = [d['value'] for d in data[x] if d['type'] == 'number' and (y >= d['index_beg'] and y <= d['index_end'])]
    for sublist in previous_line:
        if sublist not in numbers:
            numbers.append(sublist)
    print(numbers)
    return numbers

def parse_line(line):
    line_data= []
    str_num = ''
    index = 0
    index_beg = 0
    char: str
    for char in line:
        if char.isdigit():
            if str_num == '':
                index_beg = index
            str_num+=char
        else:
            if str_num != '':
                line_data.append({
                    'type': 'number',
                    'value': str_num,
                    'index_beg': index_beg,
                    'index_end': index-1,
                })
                str_num = ''
            if char != '.' and char != '\n':
                line_data.append({
                    'type': 'operator',
                    'index': index
                })
        index+=1
    return line_data
        

script()