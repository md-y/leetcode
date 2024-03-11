class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a = (1, 1, 1, 1, 1)
        for _ in range(1, n):
            a = (
                a[1] + a[2] + a[4],
                a[0] + a[2],
                a[1] + a[3],
                a[2],
                a[2] + a[3],
            )
        return sum(a) % 1000000007
