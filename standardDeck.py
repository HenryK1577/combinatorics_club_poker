import math

def generate_deck():
    deck = [x/100 for x in range(200, 1476, 25)]
    return deck

def parse_card(card):
    match(math.floor(card)):
        case 2:
            print("Two of ", end='')
        case 3:
            print("Three of ", end='')
        case 4:
            print("Four of ", end='')
        case 5:
            print("Five of ", end='')
        case 6:
            print("Six of ", end='')
        case 7:
            print("Seven of ", end='')
        case 8:
            print("Eight of ", end='')
        case 9:
            print("Nine of ", end='')
        case 10:
            print("Ten of ", end='')
        case 11:
            print("Jack of ", end='')
        case 12:
            print("Queen of ", end='')
        case 13:
            print("King of ", end='')
        case 14:
            print("Ace of ", end='')

    match(round(math.modf(card)[0], 2)):
        case 0:
            print("Hearts")
        case .25:
            print("Diamonds")
        case .50:
            print("Clubs")
        case .75:
            print("Spades")




    