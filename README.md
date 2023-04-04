# age3d
A Python Library to age 3d models by simulating the effects of weather 

[![Build Status](https://github.com/A-Chaudhary/age3d/workflows/Build%20Status/badge.svg?branch=main)](https://github.com/A-Chaudhary/age3d/actions?query=workflow%3A%22Build+Status%22)
[![codecov](https://codecov.io/gh/A-Chaudhary/age3d/branch/main/graph/badge.svg)](https://codecov.io/gh/A-Chaudhary/age3d)
[![GitHub](https://img.shields.io/github/license/A-Chaudhary/age3d)](https://github.com/A-Chaudhary/age3d/blob/main/LICENSE)
[![](https://img.shields.io/github/issues/A-Chaudhary/age3d)](https://github.com/A-Chaudhary/age3d/issues)
[![PyPI](https://img.shields.io/pypi/v/age3d)](https://pypi.org/project/age3d/)
[![Documentation Status](https://readthedocs.org/projects/age3d/badge/?version=latest)](https://age3d.readthedocs.io/en/latest/?badge=latest)

[![Documentation](https://img.shields.io/badge/GitHub%20Pages-222222?style=for-the-badge&logo=GitHub%20Pages&logoColor=white)](https://a-chaudhary.github.io/age3d/)

## Overview

Age3D is a Python Library that allows for eroding of 3d models. It uses the `.stl` file format and incorporates Open3D functionality, allowing users to simulate material removal.

Features:
- Simplified Workflow for `.stl` $\rightarrow$ `TriangleMesh` $\rightarrow$ `PointCloud` & `BitMask`
- Visualization of `TriangleMesh` & `PointCloud`
- Calculate Metric of `TriangleMesh`
- Erosion Method for Aging
  - Customizable Number of Passes of Simulated Erosion Particles
  - Customizable lifetime of Simulated Erosion Particles

## Dependencies

age3d requires the [open3d](http://www.open3d.org/) Python Library which is installed during libray installation.

## Installation

The recommended way to install age3d is through pip.
```
pip install age3d
```

## Usage

Import the library:
```
import age3d
```

Import a `.stl` model where `file_path` points to the location:
```
mesh = age3d.import_mesh(file_path)
```

### Erosion

If the `mesh` is low-poly, run with `number_of_subdivisions > 0`:
```
mesh = age3d.mesh_subdivision(mesh, iterations = number_of_subdivisions)
```


Erode the `mesh`:
```
eroded_mesh = age3d.erode(mesh)
```

If Erosion with customized Passes and Max Particle Lifetime:
```
updated_vertices, eroded_mesh = age3d.erode(mesh, iterations = 2, erosion_lifetime = 10)
```

### Point Cloud Creation

Make a `PointCloud` with Red Color Points:
```
point_cloud = age3d.make_point_cloud(mesh, color = [255, 0, 0])
```

### Visualization

Visualize Eroded Mesh:
```
eroded_mesh.compute_vertex_normals()
age3d.visualize(mesh)
```
or
```
eroded_mesh.compute_vertex_normals()
age3d.visualize([mesh])
```

Visualize Mesh & Point Cloud:
```
eroded_mesh.compute_vertex_normals()
age3d.visualize([mesh, point_cloud])
```

Visualize Mesh & Point Cloud with Wireframe:
```
eroded_mesh.compute_vertex_normals()
age3d.visualize([mesh, point_cloud], show_wireframe = True)
```

## Contributing
If you encounter an issue, please feel free to raise it by opening an issue. Likewise, if you have resolved an issue, you are welcome to open a pull request.

See more at [CONTRIBUTING.md](./CONTRIBUTING.md)
