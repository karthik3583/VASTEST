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

config = Configuration("Elite", [Sensor.CAMERA, Sensor.RADAR])
vehicle = create_vehicle(config)
print(vehicle.name)
print(vehicle.capabilities)

