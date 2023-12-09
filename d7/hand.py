ORDER = ['J','2','3','4','5','6','7','8','9','T','Q','K','A']

class Hand:
    def __init__(self, hand, bid) -> None:
        self.wildcards = 0
        self.order = hand
        self.hand= self.process(hand)
        self.bid = bid
        self.type = self.identify()
        self.rank = None
        

    def process(self, hand):
        res = {}
        for card in hand:
            if card in res.keys():
                res[card]+=1
            else:
                res[card]=1
        return res
    
    def set_rank(self, rank):
        self.rank = rank
    
    def get_bid(self):
        return self.bid
    
    def get_rank(self):
        return self.rank
    
    def get_better_hand(self):
        vals = list(self.hand.values())
        if self.wildcards == 5 or self.wildcards == 4:
            return {
                'name' : '5Kind',
                'value': 6
            }
        elif self.wildcards == 3:
            if 2 in vals:
                return {
                'name' : '5Kind',
                'value': 6
            }
            else:
                return {
                'name' : '4Kind',
                'value': 5
            }
        elif self.wildcards == 2 :
            if 3 in vals:
                return {
                'name' : '5Kind',
                'value': 6
            }
            elif 2 in vals:
                return {
                'name' : '4Kind',
                'value': 5
            }
            else:
                return {
                'name' : '3Kind',
                'value': 3
            }
        else:
            if 2 in vals:
                if vals.count(2) == 2:
                    return {
                        'name' : 'FHouse',
                        'value': 4
                    }
                else:
                    return {
                        'name' : '3Kind',
                        'value': 3
                    }
            elif 3 in vals:
                return {
                    'name' : '4Kind',
                    'value': 5
                }
            elif 4 in vals:
                return {
                    'name' : '5Kind',
                    'value': 6
                }
            else:
                return {
                    'name' : '1Pair',
                    'value': 1
                }










    def identify_basic(self):
        vals = list(self.hand.values())
        if 5 in vals:
            return {
                'name' : '5Kind',
                'value': 6
            }
        if 4 in vals:
            return {
                'name' : '4Kind',
                'value': 5
            }
        if 3 in vals:
            if 2 in vals:
                return {
                'name' : 'FHouse',
                'value': 4
            }
            return {
                'name' : '3Kind',
                'value': 3
            }
        if 2 in vals:
            if vals.count(2) ==2:
                return {
                'name' : '2Pair',
                'value': 2
            }
            return {
                'name' : '1Pair',
                'value': 1
            }
        return {
                'name' : 'High',
                'value': 0
            }

        
    def identify(self):
        updated_hand = self.hand
        vals = list(self.hand.keys())
        if 'J' in vals:
            self.wildcards+=self.hand['J']
            del self.hand['J']
        if self.wildcards == 0:
            return self.identify_basic()
        else:
            return self.get_better_hand()



    def __gt__ (self, other):
        if self.type['value'] == other.type['value']:
            for i in range(0, 5):
                if ORDER.index(self.order[i]) == ORDER.index(other.order[i]):
                    continue
                else:
                    return ORDER.index(self.order[i]) > ORDER.index(other.order[i])
        else:
            return self.type['value'] > other.type['value']
    
    def __lt__(self, other):
        if self.type['value'] == other.type['value']:
            for i in range(0, 5):
                if ORDER.index(self.order[i]) == ORDER.index(other.order[i]):
                    continue
                else:
                    return ORDER.index(self.order[i]) < ORDER.index(other.order[i])
        else:
            return self.type['value'] < other.type['value']
        
    def __repr__(self):
        dis = ''
        dis+= f' =>{self.order} : {self.type["name"]}<='
        return dis