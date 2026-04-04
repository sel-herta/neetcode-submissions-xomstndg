class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        h_car = {} # pos : speed
        for i in range(len(position)): # o(n)
            h_car[position[i]] = speed[i]
        h_car = dict(sorted(h_car.items())) # o(nlogn)
        
        # time = (goal - pos) / speed
        # goal = 20
        # pos = [1, 4]
        # speed = [10, 1]
        # times = [5, 1, 3, 5]
        times = []
        for pos, speed in h_car.items():
            time = (target - pos) / speed
            times.append(time)
        stack = []
        for time in times:
            while stack and stack[-1] <= time:
                stack.pop()
            stack.append(time)
        return len(stack)

        
