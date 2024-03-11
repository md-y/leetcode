class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        brick_diffs = []
        i = 0
        while i < len(heights) - 1:
            diff = heights[i + 1] - heights[i]
            if diff <= 0:
                pass
            elif bricks >= diff:
                bricks -= diff
                heapq.heappush(brick_diffs, -diff)
            elif ladders > 0:
                ladders -= 1
                if len(brick_diffs) > 0:
                    possible_bricks = -brick_diffs[0]
                    if possible_bricks >= diff:
                        bricks += -heapq.heappop(brick_diffs)
                        continue
            else:
                return i
            i += 1
        return len(heights) - 1

