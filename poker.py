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
            return True
    return False

#Returns True if a hand contains three of a kind. Works for numeric hands.
def has_threekind(hand, only = False): ##TODO: only = True
    if(len(hand) < 3):
        return False
    for i in range(len(hand) - 2):
        if(math.floor(hand[i]) == math.floor(hand[i+1])):
            if(math.floor(hand[i+1]) == math.floor(hand[i+2])):
                return True
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
def has_flush(hand, only = False): ##TODO: only = True
    suits = [0] * len(hand)
    for i in range(len(hand)):
        suits[i] = round(math.modf(hand[i])[0], 2)

    if all(element == suits[0] for element in suits):
        return True
    else:
        return False
    
#Returns True if a hand contains a straight. Works for numeric hands.
def has_straight(hand, only = False): #TODO: only = True, aces low straight
    diffs = [0] * (len(hand)-1)
    for i in range(len(hand)-1):
        diffs[i] = math.floor(hand[i + 1]) - math.floor(hand[i])
    if all(element == 1 for element in diffs):
        return True
    else:
        return False
    
#Returns True if a hand contains a straight flush. Works for numeric hands.
def has_straightflush(hand, only = False): #TODO only = True
    if has_flush(hand) and has_straight(hand):
        if only:
            if is_royalflush(hand):
                return False
            else:
                return True
        return True
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

#Randomly draws hands of size N from deck until conditional_func returns true
def seek_handtype(deck, conditional_func, N = 5):
    hand = draw_N(deck, N)
    while not conditional_func(hand):
          hand = draw_N(deck, N)
    return hand