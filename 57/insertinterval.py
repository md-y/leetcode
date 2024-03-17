class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        '''
        Merges in-place
        '''

        indexes = [-1, -1] # Indexes of intervals to merge
        i = 0

        # ti is the index we are testing against (either start or end of newInterval)
        for ti in range(2):
            # Skip intervals that don't overlap newInterval
            while i < len(intervals) and newInterval[ti] > intervals[i][1]:
                i += 1

            if i == len(intervals) or newInterval[ti] < intervals[i][0]:
                intervals.insert(i, [newInterval[ti], newInterval[ti]])
            indexes[ti] = i

        # Merge intervals
        intervals[indexes[1]] = [intervals[indexes[0]][0], intervals[indexes[1]][1]]
        del intervals[indexes[0]:indexes[1]]
        return intervals

sol = Solution()
res = sol.insert([[1,5]], [0,3])
print(res)
