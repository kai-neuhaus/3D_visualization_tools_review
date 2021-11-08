#https://newbedev.com/exporting-a-3d-numpy-to-a-vtk-file-for-viewing-in-paraview-mayavi
import numpy as np

from tvtk.api import tvtk, write_data

# data = np.random.random((10,10,10))
data = np.load(r'd124_ICM_0002_Mode3D.npy')

grid = tvtk.ImageData(spacing=(10, 5, -10), origin=(100, 350, 200), dimensions=data.shape)
grid.point_data.scalars = np.ravel(data, order='F')
grid.point_data.scalars.name = 'Test Data'

# Writes legacy ".vtk" format if filename ends with "vtk", otherwise
# this will write data using the newer xml-based format.
write_data(grid, r'd124_ICM_0002_Mode3D.vtk')