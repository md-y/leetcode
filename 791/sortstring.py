from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counts = Counter(s)
        output = []
        for c in order:
            if c in counts:
                output.append(c * counts[c])
                del counts[c]
        for c in counts:
            output.append(c * counts[c])
        return ''.join(output)

sol = Solution()
res = sol.customSortString('hucw', 'utzoampdgkalexslxoqfkdjoczajxtuhqyxvlfatmptqdsochtdzgypsfkgqwbgqbcamdqnqztaqhqanirikahtmalzqjjxtqfnh')
print(res)
