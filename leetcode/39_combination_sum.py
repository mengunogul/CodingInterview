from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res: set[tuple[int]] = set()

        def backtrack(it, comb):
            if sum(comb) == target:
                self.res.add(tuple(sorted(comb)))
                return
            if sum(comb) > target:
                return
            if it >= len(candidates):
                return

            comb.append(candidates[it])
            backtrack(it, comb[:])
            comb.pop()
            backtrack(it + 1, comb[:])

        backtrack(0, [])
        return [list(res) for res in self.res]
