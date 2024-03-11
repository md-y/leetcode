import functools

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @functools.cache
        def parse(s: str, p: str):
            if len(p) > 1 and p[1] == '*':
                if len(s) > 0 and (p[0] == s[0] or p[0] == '.'):
                    return parse(s[1:], p) or parse(s, p[2:])
                else:
                    return parse(s, p[2:])

            if len(s) == 0:
                return len(p) == 0
            if len(p) == 0:
                return False

            if p[0] == s[0] or p[0] == '.':
                return parse(s[1:], p[1:])

            return False
        
        parts = p.split('*')
        for i in range(len(parts) - 1, 1, -1):
            if len(parts[i]) == 1 and parts[i - 1].endswith(parts[i]):
                parts.pop(i)
        p = '*'.join(parts)
        return parse(s, p)
