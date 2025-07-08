from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack: List[int] = []

        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                collide = stack.pop()
                if collide > abs(asteroid):
                    stack.append(collide)
                    break
                elif collide == abs(asteroid):
                    break
                else:
                    continue
            else:
                stack.append(asteroid)

        return stack
