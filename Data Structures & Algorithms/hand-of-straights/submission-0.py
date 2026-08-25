class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        dict={}

        hand=sorted(hand)
        for i in range(0,len(hand)):
            if hand[i] in dict:
                dict[hand[i]]+=1
            else:
                dict[hand[i]]=1
        for card in hand:
            if dict[card]==0:
                continue
            for next_card in range(card,card+groupSize):
                if next_card not in dict or dict[next_card]==0:
                    return False
                dict[next_card]-=1
        return True

