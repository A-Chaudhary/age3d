import age3d

if __name__ == "__main__":
    print('ran main')
    file_path = 'models/monkey.stl'

    mesh = age3d.import_mesh(file_path)
    mesh.compute_vertex_normals()

    # # np.save('tests/monkey_vertices', np.asarray(mesh.vertices))
    # # np.save('tests/monkey_triangles', np.asarray(mesh.triangles))

    # print(mesh)
    # age3d.clean_mesh(mesh)
    # print(mesh)
    # mesh = age3d.mesh_subdivision(mesh, 3)
    # print(mesh)
    # print('-----------------')

    # vertices_idx, vertices = age3d.find_all_above(mesh, age3d.calculate_bounds_height(mesh), True)
    # above_point_cloud = age3d.make_point_cloud(vertices, [0, 255, 0])

    # # vertices_idx, mesh = age3d.erode(mesh, 200, 10)
    # vertices_idx, new_mesh = age3d.erode(mesh, 10, 10)
    # mesh.compute_vertex_normals()
    # point_cloud = age3d.make_point_cloud(np.asarray(new_mesh.vertices)[vertices_idx], [255, 0, 0])
    # # age3d.visualize([mesh, above_point_cloud, point_cloud], True)
    # # age3d.visualize([mesh, above_point_cloud, point_cloud], False)
    # age3d.visualize([mesh, point_cloud], True)
    # # age3d.visualize([mesh, point_cloud], False)
    # age3d.visualize([mesh], True)
    # age3d.visualize([mesh], False)
