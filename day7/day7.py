import os
dirname = os.path.dirname(__file__)
from collections import Counter

f = open(dirname + "/input.txt")
lines = f.readlines()
result = 0
counter = 1
def problem_1():

    hands = [1,1,1,1,1],[1,1,1,2], [1,2,2],[1,1,3],[2,3],[1,4],[5]
    card_mapping = {"A": 1, "K":2, "Q":3, "J":4, "T":5, "9":6, "8":7, "7":8, "6":9, "5":10, "4":11, "3":12, "2":13} 


    high_card = []
    one_pair = []
    two_pair = []
    three_of_a_kind = []
    full_house = []
    four_of_kind = []
    five_of_kind = []

    def sort_and_calculate_cards(input):
        global counter
        global result
        for i in range(len(input)):
            for j in range(0, len(input)-i-1):
                for k in range(5):
                    if card_mapping[input[j][0][0][k]] != card_mapping[input[j+1][0][0][k]]:
                        if card_mapping[input[j][0][0][k]] < card_mapping[input[j+1][0][0][k]]:
                            input[j], input[j + 1] = input[j + 1], input[j]
                        else:
                            break
                        break
        for i in range(len(input)):
            result += (counter * input[i][1])
            counter += 1    

    for i in lines:
        i = i.strip('\n')
        hand = i.split()[:1]
        bid = i.split()[1:]
        hand_values = {}
        hand_check = []
        for j in hand[0]:
            if j not in hand_values:
                hand_values[j] = 0
            hand_values[j] += 1
        for v in hand_values.values():
            hand_check.append(v)
        hand_check.sort()   

        if hand_check == hands[0]:
            high_card.append((hand, int(bid[0])))
        elif hand_check == hands[1]:
            one_pair.append((hand, int(bid[0])))
        elif hand_check == hands[2]:
            two_pair.append((hand, int(bid[0])))
        elif hand_check == hands[3]:
            three_of_a_kind.append((hand, int(bid[0])))
        elif hand_check == hands[4]:
            full_house.append((hand, int(bid[0])))
        elif hand_check == hands[5]:
            four_of_kind.append((hand, int(bid[0])))
        elif hand_check == hands[6]:
            five_of_kind.append((hand, int(bid[0])))    

    sort_and_calculate_cards(high_card)
    sort_and_calculate_cards(one_pair)
    sort_and_calculate_cards(two_pair)
    sort_and_calculate_cards(three_of_a_kind)
    sort_and_calculate_cards(full_house)
    sort_and_calculate_cards(four_of_kind)
    sort_and_calculate_cards(five_of_kind)
    print(result)


problem_1()
result = 0
counter = 1

def problem_2():

    hands = [1,1,1,1,1],[1,1,1,2], [1,2,2],[1,1,3],[2,3],[1,4],[5]
    card_mapping = {"A": 1, "K":2, "Q":3, "T":5, "9":6, "8":7, "7":8, "6":9, "5":10, "4":11, "3":12, "2":13, "J":14} 
    high_card = []
    one_pair = []
    two_pair = []
    three_of_a_kind = []
    full_house = []
    four_of_kind = []
    five_of_kind = []

    def sort_and_calculate_cards(input):
        global counter
        global result
        for i in range(len(input)):
            for j in range(0, len(input)-i-1):
                for k in range(5):
                    if card_mapping[input[j][0][0][k]] != card_mapping[input[j+1][0][0][k]]:
                        if card_mapping[input[j][0][0][k]] < card_mapping[input[j+1][0][0][k]]:
                            input[j], input[j + 1] = input[j + 1], input[j]
                        else:
                            break
                        break
        for i in range(len(input)):
            result += (counter * input[i][1])
            counter += 1    
    for i in lines:
        i = i.strip('\n')
        hand = i.split()[:1]
        bid = i.split()[1:]
        hand_values = {}
        hand_check = []
        j_values = False
        for j in hand[0]:
            if j not in hand_values:
                hand_values[j] = 0
            hand_values[j] += 1

        for k,v in hand_values.items():
            if k != "J":
                hand_check.append(v)
            else:
                j_values = v
        if j_values and j_values == 5:
            hand_check = [5]
        elif j_values:
            max_hand_check = max(hand_check)
            hand_check[hand_check.index(max_hand_check)] = max_hand_check + j_values

        hand_check.sort()   
        if hand_check == hands[0]:
            high_card.append((hand, int(bid[0])))
        elif hand_check == hands[1]:
            one_pair.append((hand, int(bid[0])))
        elif hand_check == hands[2]:
            two_pair.append((hand, int(bid[0])))
        elif hand_check == hands[3]:
            three_of_a_kind.append((hand, int(bid[0])))
        elif hand_check == hands[4]:
            full_house.append((hand, int(bid[0])))
        elif hand_check == hands[5]:
            four_of_kind.append((hand, int(bid[0])))
        elif hand_check == hands[6]:
            five_of_kind.append((hand, int(bid[0])))    
    sort_and_calculate_cards(high_card)
    sort_and_calculate_cards(one_pair)
    sort_and_calculate_cards(two_pair)
    sort_and_calculate_cards(three_of_a_kind)
    sort_and_calculate_cards(full_house)
    sort_and_calculate_cards(four_of_kind)
    sort_and_calculate_cards(five_of_kind)
    print(result)

problem_2()