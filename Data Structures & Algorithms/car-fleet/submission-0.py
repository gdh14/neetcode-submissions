""" 
Monotonic Stack application, a bit hard to come up with the algo, but the code is simple.

Intuition
- Cars that start closer to the target are processed first.
- For each car, we compute the time it will take to reach the target.
- If a car behind reaches the target no faster than the car in front, it will eventually catch up and join the same fleet.
- So we only keep the car’s time if it forms a new fleet; otherwise, it merges with the previous one.
- Using a stack helps us easily compare each car's time with the fleet ahead of it. the stack element is the time of each fleet's arrival, therefore the size of fleet is the answer


Example: 

target = 10

sorted
- position: [5, 3, 1]
- speed: [2, 6, 2]
- 
stack = []

"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # keep track of time of each fleet's arrival
        stack = []

        # sort each car (descending in position, first car is closet to target)
        cars = sorted(zip(position, speed), reverse=True)

        for p, s in cars:
            time_to_tgt = (target - p) / s
            
            # first car, no blocking
            if len(stack) == 0:
                stack.append(time_to_tgt)
                continue

            # current car is faster, then it will be merged to the car ahead into one fleet
            # only when slower, it will be push to stack to form a new fleet 
            # with a longer arrival time
            if time_to_tgt > stack[-1]:
                stack.append(time_to_tgt)
        
        return len(stack)








