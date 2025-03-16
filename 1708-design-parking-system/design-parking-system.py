class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.spaces = [big, medium, small]       

    def addCar(self, carType: int) -> bool:
        # converting to 0-index 
        carType -= 1
        if self.spaces[carType] > 0:
            self.spaces[carType] -= 1
            return True
        else:
            return False 



# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)