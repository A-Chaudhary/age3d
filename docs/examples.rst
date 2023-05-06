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
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
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
      Iter:  3 , V_idx:  1202
      Iter:  4 , V_idx:  4516
      Iter:  5 , V_idx:  1168
      Iter:  6 , V_idx:  5715
      Iter:  7 , V_idx:  6116
      Iter:  8 , V_idx:  3095
      Iter:  9 , V_idx:  7572
      Iter:  10 , V_idx:  6073
      Iter:  11 , V_idx:  2458
      Iter:  12 , V_idx:  4677
      Iter:  13 , V_idx:  5880
      Iter:  14 , V_idx:  6078
      Iter:  15 , V_idx:  7146
      Iter:  16 , V_idx:  1191
      Iter:  17 , V_idx:  5861
      Iter:  18 , V_idx:  1177
      Iter:  19 , V_idx:  6651
      Iter:  20 , V_idx:  1634
      Iter:  21 , V_idx:  6353
      Iter:  22 , V_idx:  2341
      Iter:  23 , V_idx:  7677
      Iter:  24 , V_idx:  4529
      Iter:  25 , V_idx:  2410
      Iter:  26 , V_idx:  2280
      Iter:  27 , V_idx:  4923
      Iter:  28 , V_idx:  2447
      Iter:  29 , V_idx:  5688
      Iter:  30 , V_idx:  1257
      Iter:  31 , V_idx:  1946
      Iter:  32 , V_idx:  6396
      Iter:  33 , V_idx:  4909
      Iter:  34 , V_idx:  2217
      Iter:  35 , V_idx:  1203
      Iter:  36 , V_idx:  1170
      Iter:  37 , V_idx:  1944
      Iter:  38 , V_idx:  2986
      Iter:  39 , V_idx:  5034
      Iter:  40 , V_idx:  6105
      Iter:  41 , V_idx:  5938
      Iter:  42 , V_idx:  2461
      Iter:  43 , V_idx:  1200
      Iter:  44 , V_idx:  3175
      Iter:  45 , V_idx:  3126
      Iter:  46 , V_idx:  4673
      Iter:  47 , V_idx:  2961
      Iter:  48 , V_idx:  4995
      Iter:  49 , V_idx:  814
      Iter:  50 , V_idx:  1696
      Iter:  51 , V_idx:  5916
      Iter:  52 , V_idx:  7721
      Iter:  53 , V_idx:  6020
      Iter:  54 , V_idx:  6120
      Iter:  55 , V_idx:  5988
      Iter:  56 , V_idx:  3174
      Iter:  57 , V_idx:  5842
      Iter:  58 , V_idx:  4684
      Iter:  59 , V_idx:  3159
      Iter:  60 , V_idx:  2251
      Iter:  61 , V_idx:  6382
      Iter:  62 , V_idx:  572
      Iter:  63 , V_idx:  6042
      Iter:  64 , V_idx:  6426
      Iter:  65 , V_idx:  3089
      Iter:  66 , V_idx:  6094
      Iter:  67 , V_idx:  2465
      Iter:  68 , V_idx:  4534
      Iter:  69 , V_idx:  4609
      Iter:  70 , V_idx:  1499
      Iter:  71 , V_idx:  2445
      Iter:  72 , V_idx:  2267
      Iter:  73 , V_idx:  3176
      Iter:  74 , V_idx:  5678
      Iter:  75 , V_idx:  5701
      Iter:  76 , V_idx:  4544
      Iter:  77 , V_idx:  3194
      Iter:  78 , V_idx:  4506
      Iter:  79 , V_idx:  2423
      Iter:  80 , V_idx:  1448
      Iter:  81 , V_idx:  2323
      Iter:  82 , V_idx:  5032
      Iter:  83 , V_idx:  500
      Iter:  84 , V_idx:  4994
      Iter:  85 , V_idx:  2271
      Iter:  86 , V_idx:  1482
      Iter:  87 , V_idx:  4336
      Iter:  88 , V_idx:  2900
      Iter:  89 , V_idx:  767
      Iter:  90 , V_idx:  5767
      Iter:  91 , V_idx:  5978
      Iter:  92 , V_idx:  347
      Iter:  93 , V_idx:  4975
      Iter:  94 , V_idx:  1947
      Iter:  95 , V_idx:  3099
      Iter:  96 , V_idx:  5975
      Iter:  97 , V_idx:  4564
      Iter:  98 , V_idx:  113
      Iter:  99 , V_idx:  130

.. container:: cell code

   .. code:: python

      a3d.visualize([eroded_mesh, updated_pc])

.. image:: img/monkey_erode.png
  :alt: Monkey Erode

