import sys
from collections import Counter
from enum import Enum, auto


class HandType(Enum):
    HighCard = auto()
    Pair = auto()
    TwoPair = auto()
    ThreeOfAKind = auto()
    FullHouse = auto()
    FourOfAKind = auto()
    FiveOfAKind = auto()

    def __lt__(self, other):
        # Custom comparison based on the order of enum members
        return self.value < other.value

    @classmethod
    def parse(cls, value):
        assert len(value) == 5, "Hand is expected to be 5 cards"

        chars = Counter(list(value))
        cardinality = len(chars)
        
        if cardinality == 5:
            return HandType.HighCard
        elif cardinality == 4:
            return HandType.Pair
        elif cardinality == 3:
            if max(chars.values()) == 3:
                return HandType.ThreeOfAKind
            else:
                return HandType.TwoPair
        elif cardinality == 2:
            if max(chars.values()) == 3:
                return HandType.FullHouse
            else:
                return HandType.FourOfAKind
        elif cardinality == 1:
            return HandType.FiveOfAKind
        else:
            raise ValueError(f"Unparseable hand type: {value}")
 

class Hand:
    _card_mapping = {
            "A":"m", "K":"l", "Q":"k", "J":"j", "T":"i", "9":"h", "8":"g", "7":"f", "6":"e", "5":"d", "4":"c", "3":"b", "2":"a",
        }

    def __init__(self, hand:str):
        self.raw_value = hand
        self.normalized_value = self._normalize(hand)
        self.hand_type = HandType.parse(hand)

    def __repr__(self):
        return f"Hand(raw_value={self.raw_value}, hand_type={self.hand_type})"

    def __eq__(self, other):
        return self.raw_value == other.raw_value

    def __lt__(self, other):
        return self.hand_type < other.hand_type or (
            self.hand_type == other.hand_type and self.normalized_value < other.normalized_value)

    def _normalize(self, hand):
        return "".join([
            Hand._card_mapping[x] for x in hand
        ])


class Bet:
    def __init__(self, hand:Hand, amount:int):
        self.hand = hand
        self.amount = amount

    def __repr__(self):
        return f"Bet(hand={self.hand}, amount={self.amount})"


def parse(lines):
    bets = []
    for line in lines:
        hand, amount = line.strip().split()
        bets.append(Bet(Hand(hand), int(amount)))
    return bets

if __name__ == "__main__":
    lines = sys.stdin.readlines()
    bets = parse(lines)

    print(sum((rank+1)*bet.amount for rank,bet in enumerate(sorted(bets, key=lambda x: x.hand))))