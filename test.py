import unittest
from main import *

class TestCreateVehicle(unittest.TestCase):

    def test_create_elite_with_camera_and_radar(self):
        config = Configuration("Elite", [Sensor.CAMERA, Sensor.RADAR])
        vehicle = create_vehicle(config)
        self.assertEqual(vehicle.name, "Elite")
        self.assertTrue(vehicle.has_capability(Capability.LANE_CHANGING))
        self.assertTrue(vehicle.has_capability(Capability.OVERTAKING))
        self.assertFalse(vehicle.has_capability(Capability.INTERSECTION_NAVIGATION))

    

if __name__ == "__main__":
    unittest.main()