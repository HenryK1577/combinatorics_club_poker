from analytics import *
import math
import copy

#Returns an array of N cards from a deck
def draw_N(deck, n = 5):
    return sorted(sample(deck, n, replace = False))

#Returns True if a hand contains a pair. Works for numeric hands.
def has_pair(hand, only = False): ##TODO: only = True
    for i in range(len(hand) - 1):
        if(math.floor(hand[i]) == math.floor(hand[i+1])):
            if not only:
                return True
            else:
                return not (has_threekind(hand) or has_twopair(hand)) #TODO: has_threekind() or has_twopair()
    return False

#Returns True if a hand contains two pair. Works for numeric hands.
def has_twopair(hand, only = False):
    arrCopy = [math.floor(x) for x in hand]
    counter = [0] * 14
    for i in range(1, 14):
        counter[i] = arrCopy.count(i)
    
    if counter.count(2) == 2:
        return True
    elif not only:
        return is_full(hand)
    else:
        return False

#Returns True if a hand contains three of a kind. Works for numeric hands.
def has_threekind(hand, only = False):
    if(len(hand) < 3):
        return False
    for i in range(len(hand) - 2):
        if(math.floor(hand[i]) == math.floor(hand[i+1])):
            if(math.floor(hand[i+1]) == math.floor(hand[i+2])):
                if not only:
                    return True
                else:
                    return not is_full(hand)
    return False

#Returns True if a hand contains four of a kind. Works for numeric hands.
def is_fourkind(hand):
    if(len(hand) < 4):
        return False
    
    for i in range(len(hand) - 3):
        if(math.floor(hand[i]) == math.floor(hand[i+1])):
            if(math.floor(hand[i+1]) == math.floor(hand[i+2])):
                if(math.floor(hand[i+2]) == math.floor(hand[i+3])):
                    return True
    return False

#Returns True if a hand contains a full house. Works for numeric hands.
def is_full(hand):
    if(len(hand) < 5):
        return False
    if not has_threekind(hand):
        return False

    arrCopy = [math.floor(x) for x in hand]
    counter = [0] * 14
    for i in range(14):
        counter[i] = arrCopy.count(i+1)

    if(counter.count(2) == 1 and counter.count(3) == 1):
        return True
    
    return False

#Returns True if a hand contains a flush. Works for numeric hands.
def has_flush(hand, only = False):
    suits = [0] * len(hand)
    for i in range(len(hand)):
        suits[i] = round(math.modf(hand[i])[0], 2)

    if all(element == suits[0] for element in suits):
        if not only:
            return True
        else:
            return not has_straight(hand)
    else:
        return False
    
#Returns True if a hand contains a straight. Works for numeric hands.
def has_straight(hand, only = False): #TODO: only = True, aces low straight
    diffs = [0] * (len(hand)-1)
    for i in range(len(hand)-1):
        diffs[i] = math.floor(hand[i + 1]) - math.floor(hand[i])

    if all(element == 1 for element in diffs) or has_straight_aceslow(hand):
        if not only:
            return True
        else:
            return not has_flush(hand)
    else:
        return False

#Returns True if a hand contains a straight, treating aces (14) as 1. Works for numeric hands.
def has_straight_aceslow(hand):
    diffs = [0] * (len(hand)-1)
    aces_low = hand.copy()
    aces_low[:] = [math.floor(x) for x in aces_low]
    aces_low[:] = [x if x != 14 else 1 for x in aces_low]
    
    for i in range(len(aces_low)-1):
        diffs[i] = math.floor(aces_low[i + 1]) - math.floor(aces_low[i])
    
    if all(element == 1 for element in diffs):
        return True
    else:
        return False





#Returns True if a hand contains a straight flush. Works for numeric hands.
def has_straightflush(hand, only = False): #TODO only = True
    if has_flush(hand) and has_straight(hand):
        if not only:
            return True
        else:
            return not is_royalflush(hand)
    else:
        return False
    
#Returns True if a hand contains a royal flush. Works for numeric hands.
def is_royalflush(hand):
    if not has_straightflush(hand):
        return False
    else:
        arrCopy = [math.floor(x) for x in hand]
        if (arrCopy == [10,11,12,13,14]):
            return True

#Returns True if the hand's best scoring is a high card. Works for numeric hands
def is_highcard(hand):
    return not(has_pair(hand) or has_straight(hand) or has_flush(hand))

#Randomly draws hands of size N from deck until conditional_func returns true
def seek_handtype(deck, conditional_func, N = 5):
    hand = draw_N(deck, N)
    while not conditional_func(hand):
          hand = draw_N(deck, N)
    return hand

#Returns the highest score a hand can make
#1 - High Card | 2 - Pair | 3 - Two Pair | 4 - Three Kind
#5 - Straight | 6 - Flush | 7 - Full House | 8 - Four kind
#9 - Straight Flush | 10 - Royal Flush
def get_highest_score(hand):
    if is_highcard(hand):
        return 1
    elif has_pair(hand, True):
        return 2
    elif has_twopair(hand, True):
        return 3
    elif has_threekind(hand, True):
        return 4
    elif has_straight(hand, True):
        return 5
    elif has_flush(hand, True):
        return 6
    elif is_full(hand):
        return 7
    elif is_fourkind(hand):
        return 8
    elif has_straightflush(hand, True):
        return 9
    elif is_royalflush(hand):
        return 10
    else:
        return -1

#Returns an array representing the occurences of hands in an array of hands
def analyze_hands(handarray):
    occurences = [0] * 10

    for hand in handarray:
        occurences[get_highest_score(hand) -1] += 1

    return occurences

