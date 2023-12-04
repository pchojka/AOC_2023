import re
import operator


references = {
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9'
}

def script():
    with open('input.txt', 'r') as readfile:
        count = 0
        line_nb = 0
        lines = readfile.readlines()
        for line in lines:
            result = process_line(line)
            count += int(result)
            line_nb+=1
        print(count)
        print(f"LINES PROCESSED : {line_nb}")

def process_line(line: str):
    digits = get_digit_array(line)
    str_result = ''
    match len(digits):
        case 1:
            str_result += digits[0]['digit'] + digits[0]['digit']
        case 2:
            str_result += digits[0]['digit'] + digits[1]['digit']
        case _:
            str_result += digits[0]['digit'] + digits[len(digits) -1]['digit']
    print(f"{line[:-1]} : {digits} : {str_result}")
    return str_result


def get_digit_array(line: str):
    res = []

    for digit in references.keys():
        nb_occ =  line.count(digit)
        match nb_occ:
            case 0:
                continue
            case 1:
                occ = line.find(digit)
                res.append({
                    'digit': references[digit],
                    'index': occ
                     })
            case _:
                inserted_elements = 0
                scrapped = 0
                line_cpy = line
                while inserted_elements != nb_occ:
                    next_occ = line_cpy.find(digit) #6
                    res.append({
                        'digit': references[digit],
                        'index': next_occ + scrapped
                    })
                    inserted_elements+=1
                    line_cpy = line_cpy[next_occ + len(digit):]
                    scrapped += next_occ + len(digit) # , 

        
    for m in re.finditer(r"[0-9]", line):
        res.append({
            'digit':(m.group(0)),
            'index': m.start()
        })
    res.sort(key=operator.itemgetter('index'))
    return res


script()