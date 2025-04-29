from standardDeck import *
from analytics import *
from poker import *

myDeck = generate_deck()
testHand = draw_N(myDeck, 5)
print(testHand)
print("Pair:", has_pair(testHand))
print("Threekind:", has_threekind(testHand))
print("Fourkind:", is_fourkind(testHand))
print("Flush:", has_flush(testHand))
print("Straight:", has_straight(testHand))
print("Full:", is_full(testHand))
print("Straight Flush:", has_straightflush(testHand))
print("Royal Flush:", is_royalflush([10.25, 11.25, 12.25, 13.25, 14.5]))

