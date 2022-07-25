from typing import List
import copy

class PrinsonCellSolution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:

        def next(cells: List[int]) -> List[int]:
            newCells = [0] * len(cells)
            for i, val in enumerate(cells):
                if i - 1 < 0 or i + 1 >= len(cells):
                    newCells[i] = 0 
                elif cells[i - 1] == cells[i + 1]:
                    newCells[i] = 1
                else:
                    newCells[i] = 0
            return newCells

        # patter string - (seq, pattern array)
        patterns = {}
        seq = 0
        while seq < n and ','.join(map(str, cells)) not in patterns:
            patterns[','.join(map(str, cells))] = (seq, copy.copy(cells))
            cells = next(cells)
            seq += 1

        if seq == n:
            return cells
        
        prevSeq = patterns[','.join(map(str, cells))][0]
        distance = seq - prevSeq
        n = (n - prevSeq) % distance

        for i in range(n):
            cells = next(cells)
        
        return cells

s = PrinsonCellSolution()
cells = s.prisonAfterNDays([1,0,0,1,0,0,1,0], 1000000000)
print(','.join(map(str, cells)))