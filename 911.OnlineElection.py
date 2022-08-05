from typing import *

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        
        # person to vote count
        votes = {}

        # current maximun vote
        maxVote = 0

        winner = 0

        # winners by time
        self.winners = []

        for i in range(len(persons)):
            person = persons[i]
            time = times[i]
            prevCount = votes[person] if person in votes else 0
            newCount = prevCount + 1
            votes[person] = newCount
            
            if newCount >= maxVote:
                winner = person
                maxVote = newCount

            self.winners.append([time, winner])

    def q(self, t: int) -> int:
        
        if t >= self.winners[len(self.winners) - 1][0]:
            return self.winners[len(self.winners) - 1][1]

        i = self.search(0, len(self.winners) - 1, t)

        return self.winners[i][1]

    def search(self, i, j, time) -> int:

        if self.winners[j][0] <= time:
            return j

        pivotIndex = i + (j - i) // 2

        if self.winners[pivotIndex][0] == time or (self.winners[pivotIndex + 1][0] > time and self.winners[pivotIndex][0] < time):
            return pivotIndex

        if self.winners[pivotIndex][0] > time:
            return self.search(i, pivotIndex - 1, time)

        if self.winners[pivotIndex + 1][0] == time:
            return pivotIndex + 1

        return self.search(pivotIndex + 1, j, time)

#["TopVotedCandidate","q","q","q","q","q","q","q","q","q","q"]
# [[[0,0,0,0,1],[0,6,39,52,75]],[45],[49],[59],[68],[42],[37],[99],[26],[78],[43]]
# Your TopVotedCandidate object will be instantiated and called as such:
obj = TopVotedCandidate([0,0,0,0,1], [0,6,39,52,75])
print(obj.q(45))
print(obj.q(49))
print(obj.q(59))
print(obj.q(68))
print(obj.q(42))
print(obj.q(37))
print(obj.q(99))
print(obj.q(26))
print(obj.q(78))
print(obj.q(43))