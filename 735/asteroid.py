class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = asteroids[:1]
        for a in asteroids[1:]:
            while stack and stack[-1] > 0 and a < 0:
                if stack[-1] + a == 0:
                    stack.pop()
                    break
                elif stack[-1] < -a:
                    stack.pop()
                    continue
                break
            else:
                stack.append(a)

        return stack
