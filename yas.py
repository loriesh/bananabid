import random 

def bananabid (my_player_number, my_bananas, monkey_position, opponent_bananas, past_bid_list, turn_number):
    positions = [-3, -2, -1, 0, 1, 2, 3]
    opp_bids = []
    my_bids = [] 
    diffpos = 0
    if my_player_number == 1:
        diffpos = positions.index(monkey_position) - positions.index(-3)
    elif my_player_number == 2:
        diffpos = positions.index(3) - positions.index(monkey_position) 
    avgBananastoWin = my_bananas // abs(diffpos) if diffpos != 0 else my_bananas
    if my_player_number == 1:
        for b in past_bid_list:
            opp_bids.append(b[1])
        for b in past_bid_list:
            my_bids.append(b[0]) 
    else:
        for b in past_bid_list:
            opp_bids.append(b[0])
        for b in past_bid_list:
            my_bids.append(b[1])
    if len(past_bid_list) > 0:
        opp_avg = int(sum(opp_bids) // len(past_bid_list))
        my_avg = int(sum(my_bids) // len(past_bid_list)) # find the avg bid of opponent and self
    if opponent_bananas == 0 and my_bananas > 0:
        return 1
    if opponent_bananas < 50 and my_bananas > 30:
        return random.randint(20,30)
    if turn_number == 1:
        return random.randint(0, 4)
    if turn_number <= 3 and turn_number > 1:
        if opp_bids[-1] > my_bids[-1]:
            return random.randint(opp_bids[-1], opp_bids[-1] + 4)
        else:
            return random.randint(5, 20)
    if monkey_position == 2 and my_player_number == 1:
        return random.randint(opp_bids[-1], opp_bids[-1] + 20)
    if monkey_position == -2 and my_player_number == 2:
        return random.randint(opp_bids[-1], opp_bids[-1] + 20)
    elif turn_number >= 4:
        if monkey_position > 0 and my_bananas // 8 > opp_avg * 2 and (my_player_number == 2) and my_bananas > 150:
            return random.randint(opp_avg * 2 , my_bananas // 8) # greater than 0 and player 2 means ur winning
        elif monkey_position > 0 and my_bananas // 4 > opp_avg * 2 and (my_player_number == 1) and my_bananas > 150:
            return random.randint(opp_avg *2 ,  my_bananas // 4) # greater than 0 and player 1 means ur losing
        elif monkey_position < 0 and my_bananas // 8 > opp_avg * 2 and (my_player_number == 1) and my_bananas > 150:
            return random.randint(opp_avg * 2 , my_bananas // 8) # less than 0 and player 1 means ur winning
        elif monkey_position < 0 and my_bananas // 4 > opp_avg * 2 and (my_player_number == 2) and my_bananas > 150:
            return random.randint(opp_avg *2 ,  my_bananas // 4) # less than 0 and player 2 means ur losing
        else:
            return avgBananastoWin
           # return random.randint(my_bananas // 4, my_bananas)
    