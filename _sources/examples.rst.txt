Examples
========

.. container:: cell markdown

   .. rubric:: Import Library
      :name: import-library

.. container:: cell code

   .. code:: python

      import age3d as a3d

   .. container:: output stream stdout

      ::

         Jupyter environment detected. Enabling Open3D WebVisualizer.
         [Open3D INFO] WebRTC GUI backend enabled.
         [Open3D INFO] WebRTCWindowSystem: HTTP handshake server disabled.

.. container:: cell markdown

   .. rubric:: Import Mesh
      :name: import-mesh

.. container:: cell code

   .. code:: python

      file_path = 'models/monkey.stl'
      mesh = a3d.import_mesh(file_path)
      mesh.compute_vertex_normals()
      print(mesh)

   .. container:: output stream stdout

      ::

         TriangleMesh with 2866 points and 968 triangles.

.. container:: cell markdown

   .. rubric:: Export Mesh
      :name: export-mesh

.. container:: cell code

   .. code:: python

      export_file_path = 'models/export.stl'
      a3d.export_mesh(export_file_path ,mesh)

.. container:: cell markdown

   .. rubric:: Clean Mesh
      :name: clean-mesh

.. container:: cell code

   .. code:: python

      print('Original:', mesh)
      a3d.clean_mesh(mesh)
      print('Cleaned:', mesh)

   .. container:: output stream stdout

      ::

         Original: TriangleMesh with 2866 points and 968 triangles.
         Cleaned: TriangleMesh with 505 points and 968 triangles.

.. container:: cell code

   .. code:: python

      vertices, triangles =  a3d.mesh_details(mesh)
      print(vertices, triangles)

   .. container:: output stream stdout

      ::

         [[ 0.46875   -0.7578125  0.2421875]
          [ 0.4375    -0.765625   0.1640625]
          [ 0.5       -0.6875     0.09375  ]
          ...
          [-1.0234375  0.484375   0.4375   ]
          [ 0.859375   0.3828125  0.3828125]
          [-0.859375   0.3828125  0.3828125]] [[  0   1   2]
          [  0   2   3]
          [  4   5   6]
          ...
          [379 491 410]
          [493 384 380]
          [493 380 412]]

.. container:: cell markdown

   .. rubric:: Point Cloud Creation
      :name: point-cloud-creation

.. container:: cell code

   .. code:: python

      pc = a3d.make_point_cloud(vertices, (255, 0, 0))

.. container:: cell markdown

   .. rubric:: Visualization
      :name: visualization

.. container:: cell code

   .. code:: python

      a3d.visualize(mesh)

.. image:: img/monkey.png
  :alt: Monkey

.. container:: cell code

   .. code:: python

      a3d.visualize(mesh, show_wireframe=True)

.. image:: img/monkey_wireframe.png
  :alt: Monkey Wireframe

.. container:: cell code

   .. code:: python

      a3d.visualize([mesh, pc])

.. image:: img/monkey_pc.png
  :alt: Monkey

.. container:: cell markdown

   .. rubric:: Get Vertex Mask
      :name: get-vertex-mask

.. container:: cell code

   .. code:: python

      a3d.get_mask(mesh, [0, 1, -1])

   .. container:: output execute_result

      ::

         array([ True,  True, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                ...
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                 True])

.. container:: cell markdown

   .. rubric:: Find Minimum(s) & Maximum(s)
      :name: find-minimums--maximums

.. container:: cell code

   .. code:: python

      min_idxs, min_vertices = a3d.find_minimum(mesh,k = 1)
      min_pc = a3d.make_point_cloud(min_vertices, (255, 0, 00))

      max_idxs, max_vertices = a3d.find_maximum(mesh, k = 10)
      max_pc = a3d.make_point_cloud(max_vertices, (0, 0, 255))

      a3d.visualize([mesh, min_pc, max_pc])

.. image:: img/monkey_min_max.png
  :alt: Monkey Min Max

.. container:: cell markdown

   .. rubric:: Find All Below, Above, & Between
      :name: find-all-below-above--between

.. container:: cell code

   .. code:: python

      below_idxs, below_vertices = a3d.find_all_below(mesh, 0.25, inclusive=True)
      below_pc = a3d.make_point_cloud(below_vertices, (255, 0, 0))

      above_idxs, above_vertices = a3d.find_all_above(mesh, 0.75, inclusive=True)
      above_pc = a3d.make_point_cloud(above_vertices, (0, 255, 0))

      between_vertices = a3d.find_all_between(mesh, 0.25, 0.75)
      between_pc = a3d.make_point_cloud(between_vertices, (0, 0, 255))

      a3d.visualize([mesh, below_pc, above_pc, between_pc])

.. image:: img/monkey_below_above_between.png
  :alt: Monkey Below Above Between

.. container:: cell markdown

   .. rubric:: Find Neighbors
      :name: find-neighbors

.. container:: cell code

   .. code:: python

      center_idx = 100
      neighbors_idx, neighbors_vertices = a3d.find_neighbors(mesh, center_idx)
      neighbors_pc = a3d.make_point_cloud(neighbors_vertices, (255, 0, 0))

      center_vertex = vertices[a3d.get_mask(mesh, center_idx)]
      center_pc = a3d.make_point_cloud(center_vertex, (0, 0, 255))

      a3d.visualize([mesh,neighbors_pc, center_pc])

.. image:: img/monkey_neighbors.png
  :alt: Monkey Neighbors

.. container:: cell markdown

   .. rubric:: Mesh Subdivision
      :name: mesh-subdivision

.. container:: cell code

   .. code:: python

      print(mesh)
      mesh = a3d.mesh_subdivision(mesh, iterations=2)
      print(mesh)

      vertices, triangles =  a3d.mesh_details(mesh)
      print(vertices, triangles)

      a3d.visualize(mesh, show_wireframe=True)

.. image:: img/monkey_subdivision.png
  :alt: Monkey Subdivision

.. container:: output stream stdout

   ::

      TriangleMesh with 505 points and 968 triangles.
      TriangleMesh with 7828 points and 15488 triangles.
      [[ 0.46875    -0.7578125   0.2421875 ]
         [ 0.4375     -0.765625    0.1640625 ]
         [ 0.5        -0.6875      0.09375   ]
         ...
         [-0.73632812  0.23632812 -0.12890625]
         [-0.6875      0.1953125  -0.12890625]
         [-0.73242188  0.18554688 -0.1328125 ]] [[   0 1978 1980]
         [1978  505 1979]
         [1979  507 1980]
         ...
         [7826 1709 7827]
         [7827 1924 7825]
         [7826 7827 7825]]

.. container:: cell markdown

   .. rubric:: Bound Height
      :name: bound-height

.. container:: cell code

   .. code:: python

      bound_height = a3d.calculate_bounds_height(mesh)
      print(bound_height)

      below_idxs, below_vertices = a3d.find_all_below(mesh, bound_height)
      below_pc = a3d.make_point_cloud(below_vertices, (255, 0, 0))

      above_idxs, above_vertices = a3d.find_all_above(mesh, bound_height)
      above_pc = a3d.make_point_cloud(above_vertices, (0, 255, 0))

      a3d.visualize([mesh, below_pc, above_pc])

.. image:: img/monkey_bound_height.png
  :alt: Monkey Bound Height

.. container:: output stream stdout

   ::

      0.296875

.. container:: cell markdown

   .. rubric:: Find Accessible
      :name: find-accessible

.. container:: cell code

   .. code:: python

      direction = [0, 0, -1]
      accessible_idx, accessible_vertices = a3d.find_accessible(mesh, direction)
      accessible_pc = a3d.make_point_cloud(accessible_vertices, (255, 0, 0))
      a3d.visualize([mesh, accessible_pc], show_wireframe=True)

.. image:: img/monkey_accessible.png
  :alt: Monkey Erode Wirefram Direction 

.. container:: cell markdown

   .. rubric:: Erode
      :name: erode

.. container:: cell code

   .. code:: python

      updated_idxs, eroded_mesh = a3d.erode(mesh, iterations=100, erosion_lifetime=10)
      eroded_mesh.compute_vertex_normals()

      updated_pc = a3d.make_point_cloud(vertices[updated_idxs], (255, 0, 0))

      a3d.visualize([eroded_mesh, updated_pc], True)

.. image:: img/monkey_erode_wireframe.png
  :alt: Monkey Erode Wireframe

.. container:: output stream stdout

   ::

      Iter:  0 , V_idx:  7569
      Iter:  1 , V_idx:  1537
      Iter:  2 , V_idx:  6081
      ...
      Iter:  97 , V_idx:  4564
      Iter:  98 , V_idx:  113
      Iter:  99 , V_idx:  130

.. container:: cell code

   .. code:: python

      a3d.visualize([eroded_mesh, updated_pc])

.. image:: img/monkey_erode.png
  :alt: Monkey Erode

.. container:: cell code

   .. code:: python

      updated_idxs, eroded_mesh = a3d.erode(mesh, iterations=100, erosion_lifetime=10, direction=direction)
      eroded_mesh.compute_vertex_normals()

      updated_pc = a3d.make_point_cloud(vertices[updated_idxs], (255, 0, 0))

      a3d.visualize([eroded_mesh, updated_pc], True)

   .. container:: output stream stdout

      ::

         Iter:  0 , V_idx:  7693
         Iter:  1 , V_idx:  1537
         Iter:  2 , V_idx:  6131
         ...
         Iter:  97 , V_idx:  5687
         Iter:  98 , V_idx:  120
         Iter:  99 , V_idx:  192

.. image:: img/monkey_erode_wireframe_direction.png
  :alt: Monkey Erode Wirefram Direction 

.. container:: cell code

   .. code:: python

      a3d.visualize([eroded_mesh, updated_pc])

.. image:: img/monkey_erode_direction.png
  :alt: Monkey Erode Wirefram Direction 