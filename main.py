import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

figure = pyplot.figure()
axes = mplot3d.Axes3D(figure)

your_mesh = mesh.Mesh.from_file('Juso-3Ddata.stl')
axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

scale = your_mesh.points.flatten()
axes.auto_scale_xyz(scale, scale, scale)

pyplot.show()