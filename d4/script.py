def script():
    data = []
    with open('input.txt', 'r') as readfile:
        lines = readfile.readlines()
        for line in lines:
            card_id = line.split(':')[0].split('Card ')[1]
            card_values = line.split(':')[1]
            win_no = card_values.split('|')[0]
            win_arr = win_no.split(' ')
            card_no = card_values.split('|')[1]
            card_arr = card_no.split(' ')

            data.append({
                'id': card_id,
                'winning_numbers': [d for d in win_arr if d != "" and d!= '\n'],
                'card_numbers': [d.replace('\n', '') for d in card_arr if d != ""],
                'editions': 1
            })
        readfile.close()
    #print(data)
    ###### P1
    # for card in data:
    #     score = process_card(card)
    #     total_score += score
    # print(total_score)

    results = process_data(data)
    print(results)


def process_card(card):
    matching_numbers = 0
    for num in card['card_numbers']:
        if num in card['winning_numbers']:
            if card_score == 0:
                card_score+=1
            else:
                card_score*=2
    print(f"CARD {card['id']} : {card_score} Pts")
    return card_score

def process_data(data):
    results = []
    sum = 0
    for card in data:
        matching_numbers = 0
        id = card['id']
        for num in card['card_numbers']:
            if num in card['winning_numbers']:
                matching_numbers+=1
        results.append({
            'id': int(card['id']),
            'winning_nos': matching_numbers,
            'editions': 1
        })
    for card in results:
        for j in range(0, card['editions']):
            if card['winning_nos'] != 0:
                for i in range(card['id']+1, card['id'] + card['winning_nos'] +1):
                    results[i-1]['editions']+=1
    for card in results:
        sum += card['editions']
    return sum



script()