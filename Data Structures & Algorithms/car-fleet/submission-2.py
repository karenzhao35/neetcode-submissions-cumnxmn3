class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = list(zip(position, speed))
        cars.sort()

        result = 0
        prev_steps = -1
        while cars: 
            position, speed = cars.pop()
            steps = (target - position) / speed
            if steps > prev_steps: 
                prev_steps = steps
                result += 1

        return result