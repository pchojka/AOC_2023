from hand import Hand


def bubble_sort(hands):
    nb_hands = len(hands)

    for i in range(nb_hands):
        swap = False
        for j in range(0, nb_hands - i - 1):
            if hands[j] > hands[j+1]:
                hands[j], hands[j+1] = hands[j+1], hands[j]
                swap = True
        if not swap:
            break

def script():
    with open('input.txt', 'r') as readfile:
        sum_of = 0
        res = []
        lines = readfile.readlines()
        for line in lines:
            hand = line.split(' ')
            new_hand = Hand(hand[0], hand[1])
            res.append(new_hand)
        print(res)
        bubble_sort(res)
        print(res)
        for i in range(len(res)):
            res[i].set_rank(i+1)
            sum_of += int(res[i].get_bid())*res[i].get_rank()
        print(sum_of)


script()


    