from enum import Enum

class Sensor(Enum):
    CAMERA = 1
    RADAR = 2
    LiDAR = 3

class Capability(Enum):
    LANE_CHANGING = 1
    OVERTAKING = 2
    INTERSECTION_NAVIGATION = 3

class Vehicle:
    def __init__(self, name):
        self.name = name
        self.capabilities = []

    def add_capability(self, capability):
        self.capabilities.append(capability)

    def has_capability(self, capability):
        return capability in self.capabilities

class Elite(Vehicle):
    def __init__(self, sensors):
        super().__init__("Elite")
        if Sensor.CAMERA in sensors:
            self.add_capability(Capability.LANE_CHANGING)
        if Sensor.RADAR in sensors:
            self.add_capability(Capability.OVERTAKING)
        if Sensor.LiDAR in sensors:
            self.add_capability(Capability.INTERSECTION_NAVIGATION)

class Classic(Vehicle):
    def __init__(self, sensors):
        super().__init__("Classic")
        if Sensor.RADAR in sensors:
            self.add_capability(Capability.OVERTAKING)

class Paragon(Vehicle):
    def __init__(self, sensors):
        super().__init__("Paragon")
        if Sensor.CAMERA in sensors:
            self.add_capability(Capability.LANE_CHANGING)

class Gentry(Vehicle):
    def __init__(self, sensors):
        super().__init__("Gentry")
        if Sensor.CAMERA in sensors:
            self.add_capability(Capability.LANE_CHANGING)
        if Sensor.RADAR in sensors:
            self.add_capability(Capability.OVERTAKING)

class Configuration:
    def __init__(self, model, sensors):
        self.model = model
        self.sensors = sensors

def create_vehicle(config):
    if config.model == "Elite":
        return Elite(config.sensors)
    elif config.model == "Classic":
        return Classic(config.sensors)
    elif config.model == "Paragon":
        return Paragon(config.sensors)
    elif config.model == "Gentry":
        return Gentry(config.sensors)
    
 def compare_vehicles(vehicle1, vehicle2):
    if len(vehicle1.capabilities) > len(vehicle2.capabilities):
        return vehicle1
    elif len(vehicle1.capabilities) < len(vehicle2.capabilities):
        return vehicle2
    else:
        return None

config1 = Configuration("Elite", [Sensor.CAMERA, Sensor.RADAR])
config2 = Configuration("Paragon", [Sensor.CAMERA])
vehicle1 = create_vehicle(config1)
vehicle2 = create_vehicle(config2)
print(vehicle1.name)
print(vehicle1.capabilities)
best_vehicle = compare_vehicles(vehicle1, vehicle2)
print(best_vehicle.name)

