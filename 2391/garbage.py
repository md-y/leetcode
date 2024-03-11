class Solution:
    def garbageCollection(self, garbage: list[str], travel: list[int]) -> int:
        travel_time = 0
        m, p, g = False, False, False
        for i in range(len(garbage) - 1, -1, -1):
            if not m and "M" in garbage[i]:
                m = True
                travel_time += sum(travel[:i])
            if not p and "P" in garbage[i]:
                p = True
                travel_time += sum(travel[:i])
            if not g and "G" in garbage[i]:
                g = True
                travel_time += sum(travel[:i])
            if m and p and g:
                break

        return travel_time + sum(len(i) for i in garbage)
