#! /usr/bin/python3

# Pier1 imports
import matplotlib.pyplot as plt
import numpy as np

# description of surface
surfState = "adjusted_range_polished"

# File to Data arrays. 3 is 
file = "test4_Height.csv"
dataPath = "/home/trey/Desktop/school/thesisStuff/Surface Problems/TjipSurfaceScans/TjipScansRawData/"
labelsFromHeader = np.loadtxt(dataPath + file, delimiter=',', quotechar='"', skiprows=12, max_rows=4, dtype=str)
data = np.loadtxt(dataPath + file, delimiter=',', quotechar='"', skiprows=20)

# Sanity print
#print(labelsFromHeader)

# Create the axis ranges and meshgrid for the image
xMax = int(labelsFromHeader[0, 1])
yMax = int(labelsFromHeader[1, 1])
xAxPts = np.arange(0, xMax)
yAxPts = np.arange(0, yMax)

#Color map for the z-axis
zMin = float(labelsFromHeader[2, 1]) # was -6.462, now at the min of all of the scans (num 5)
zMax = float(labelsFromHeader[3, 1]) # was  2.374, now at the max of all of the scans (num 5)
# nZpts = int((zMax - zMin)*1000) #it reports in μm, but measures down to nm
# zColorPts = np.linspace(zMin, zMax, nZpts)

#plotting, saving, showing
plt.close("all") # Close all previous plots
fig,ax = plt.subplots()
img = plt.imshow(data, cmap='inferno', vmin=zMin, vmax=zMax, extent=(0, xMax, 0, yMax), origin='lower')
plt.colorbar(label="Depth (μm)")
#plt.title(f"Laser profile {file}")
#plt.title(f"Laser profile of {surfState} surface")
plt.xlabel(f"{labelsFromHeader[0,0]}\n(μm)")
plt.ylabel(f"{labelsFromHeader[1,0]}\n(μm)")
plt.savefig(f"/home/trey/Desktop/school/thesisStuff/Surface Problems/TjipSurfaceScans/profileImages/{surfState}.png")

plt.show()