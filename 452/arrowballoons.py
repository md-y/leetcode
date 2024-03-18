from operator import itemgetter

class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=itemgetter(1))
        arrow_count = 1
        right_end = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] > right_end:
                arrow_count += 1
                right_end = points[i][1]
        return arrow_count

sol = Solution()
res = sol.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]])
print(res)
