# PROJECT: Make a Car Class with all Methods associated with operating a car

# DECLARE Class Car with Private Attributes
class Car:
    def __init__(self, car_name, car_milage,):
        self.__carName = car_name
        self.__carMilage = car_milage
        self.__maxSpeed = 100
        self.__currentSpeed = 0
        self.__fuel = 0
        self.__capacity = 6
        self.__engineStatus = False

    # GET METHODS: car_milage, fuel, engine_status, current_speed
    def GetCarMilage(self):
        return self.__carMilage
    
    def GetFuelLevel(self):
        return self.__fuel

    def GetEngineStatus(self):
        return self.__engineStatus
    
    def GetCurrentSpeed(self):
        return self.__currentSpeed

    # SET METHODS: car_milage, current_speed, fuel
    def SetCarMilage(self, NewCarMilage):
        self.__carMilage = NewCarMilage
    
    def SetCurrentSpeed(self, NewCurrentSpeed):
        self.__currentSpeed = NewCurrentSpeed
    
    def SetFuelLevel(self, NewFuelLevel):
        self.__fuel = NewFuelLevel

    # OPERATIONAL METHODS: StartCar, StopCar, GoForward, PumpFuel
    def StartCar(self):
        if self.__engineStatus == False:
            self.__engineStatus = True
        else:
            print("Car already Started!")
    
    def StopCar(self):
        if self.__engineStatus == True:
            self.__engineStatus = False
        else:
            print("Car already Stopped!")
    
    def GoForward(self):
        if self.__fuel > 0.5:
            self.__carMilage += 1
            self.__fuel -= 0.5
        else:
            print("Not Enough Fuel, can't go forward!")
    
    def PumpFuel(self ,NewFuelLevel):
        if self.__fuel <= 0.5:
            NewFuelLevel(NewFuelLevel)
        else:
            print("Have Enough Fuel to travel")