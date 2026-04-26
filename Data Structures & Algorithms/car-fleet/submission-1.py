class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        blocking_time = 0
        carfleet = 0
        for i in range(len(position)):
            cars.append([position[i], speed[i]])
        
        cars.sort(key=lambda x: x[0])
        
        for i in reversed(cars):
            time_taken = (target - i[0])/i[1]
            if time_taken > blocking_time:
                carfleet += 1
                blocking_time = time_taken

        return carfleet            