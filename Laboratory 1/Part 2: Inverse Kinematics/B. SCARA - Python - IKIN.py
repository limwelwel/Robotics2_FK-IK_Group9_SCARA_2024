import numpy as np

#Inverse Kinematics of SCARA MANIPULATOR using Graphical Method

# link lengths in mm
a1 = float(input("a1 = "))
a2 = float(input("a2 = "))
a3 = float(input("a3 = "))
a4 = float(input("a4 = "))
a5 = float(input("a5 = "))

# Position Vector in mm
x0_3 = float(input("x0_3 = "))
y0_3 = float(input("y0_3 = "))
z0_3 = float(input("z0_3 = "))

# Inverse Kinematic Solutions using Graphical Method

# Solution 1
phi2 = np.arctan(y0_3/x0_3)
phi2 = phi2*180/np.pi

# Solution 2
r1 = np.sqrt((y0_3**2)+(x0_3**2))
# Solution 3
# Solution 4
# Solution 5
# Solution 6
# Solution 7
