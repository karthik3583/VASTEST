# VASTEST

Min2 is a car manufacturing company which produces four different lines of luxurious vehicles. The Elite,
Classic, Paragon and Gentry lines are based on the Ant vehicle design. Ant vehicles are level 3
autonomous vehicles with the ability to brake, auto pilot, avoid obstacles.
Each car model has optional sensors that can be added to it:
• Elite: CAMERA, RADAR, and LiDAR.
• Classic: RADAR.
• Paragon: CAMERA.
• Gentry: CAMERA and RADAR.
The capability of the vehicle is dependent on the type of sensing hardware installed. For example, a
vehicle with only a camera sensor can perform lane changing. See the table for details about sensor and
vehicle functionality.
Min2 allows buyers to configure the type of vehicle when making a purchase. During configuration,
buyers select vehicle model and the type of sensor(s) hardware. Note you cannot install sensors on a
vehicle which is not configured for the sensor functionality.
Oscar is a test engineer whose job is to test the behavior of a vehicle. He wants a system that will allow
him to automate his test cases. He wants to provide the configuration he receives from a buyer to the
system and get in return a Vehicle object with the specified capabilities based on the supplied
configuration.


Sensor type Allowable vehicle functionality
LiDAR (Light Detection and Ranging) Intersections navigation
RADAR Overtaking
CAMERA Lane changing
