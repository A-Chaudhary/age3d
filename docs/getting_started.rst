Getting Started
===============

Installation
------------

The recommended way to install age3d is through pip.
::
 
    pip install age3d


Usage
-----

Import the library:
::


    import age3d


Import a `.stl` model where `file_path` points to the location:
::

    mesh = age3d.import_mesh(file_path)



Erosion
-------

If the `mesh` is low-poly, run with `number_of_subdivisions > 0`:
::

    mesh = age3d.mesh_subdivision(mesh, iterations = number_of_subdivisions)



Erode the `mesh`:
::

    eroded_mesh = age3d.erode(mesh)



If Erosion with customized Passes and Max Particle Lifetime:
::

    updated_vertices, eroded_mesh = age3d.erode(mesh, iterations = 2, erosion_lifetime = 10)



Point Cloud Creation
--------------------

Make a `PointCloud` with Red Color Points:
::

    point_cloud = age3d.make_point_cloud(mesh, color = [255, 0, 0])



Visualization
-------------

Visualize Eroded Mesh:
::

    eroded_mesh.compute_vertex_normals()
    age3d.visualize(mesh)


or

::

    eroded_mesh.compute_vertex_normals()
    age3d.visualize([mesh])



Visualize Mesh & Point Cloud:
::

    eroded_mesh.compute_vertex_normals()
    age3d.visualize([mesh, point_cloud])



Visualize Mesh & Point Cloud with Wireframe:

::

    eroded_mesh.compute_vertex_normals()
    age3d.visualize([mesh, point_cloud], show_wireframe = True)

