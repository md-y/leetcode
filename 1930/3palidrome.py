class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        char_info: dict[str, list[int]] = {}

        for i in range(len(s)):
            char = s[i]
            if char in char_info:
                if char_info[char][0] + 1 != i:
                    char_info[char][1] = i
            else:
                char_info[char] = [i, -1]

        total = 0
        for key in char_info:
            info = char_info[key]
            if info[1] > 0:
                total += len(set(s[info[0] + 1 : info[1]]))

        return total
