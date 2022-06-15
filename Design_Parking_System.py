class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.big = big
        self.medium = medium
        self.small = small
        

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        no_of_big_car, no_of_medium_car, no_of_small_car = 0,0,0
        
        if carType == 1: #for big cars
            no_of_big_car+=1
            if no_of_big_car <= self.big:
                self.big -=1
                return True
        elif carType == 2: #for medium cars
            no_of_medium_car+=1
            if no_of_medium_car <= self.medium:
                self.medium -=1
                return True
        elif carType == 3: #for small cars
            no_of_small_car+=1
            if no_of_small_car <= self.small:
                self.small -=1
                return True
            
        return False
            
        
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
