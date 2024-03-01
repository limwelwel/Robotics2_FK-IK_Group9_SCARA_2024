import numpy as np
import math

#link lengths in mm

a1 = float(input("a1 = "))
a2 = float(input("a2 = "))
a3 = float(input("a3 = "))
a4 = float(input("a4 = "))
a5 = float(input("a5 = "))

#joint variables: is mm if f, is degrees if theta
T1 = float(input("T1 = ")) #20 mm
T2 = float(input("T2 = ")) #30 deg
D3 = float(input("D3 = ")) #-90 deg

#degree to radian
T1 = (T1/180.0)*np.pi
T2 = (T2/180.0)*np.pi
