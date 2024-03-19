class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        task_counts = [0] * 26
        largest = 0
        num_largest = 0
        for char in tasks:
            i = ord(char) - ord('A') 
            count = task_counts[i] + 1
            task_counts[i] = count
            if count > largest:
                largest = count
                num_largest = 1
            elif count == largest:
                num_largest += 1

        return max(len(tasks), (n + 1) * (largest - 1) + num_largest)

sol = Solution()
res = sol.leastInterval(["A", "B", "C", "D", "E"], 1)
print(res)
