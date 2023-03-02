import age3d

if __name__ == "__main__":
    print('ran main')
    # file_path = 'models/Mount_Fuji.stl'

    # mesh = import_mesh(file_path)
    # mesh.compute_vertex_normals()

    # print(mesh)
    # clean_mesh(mesh)
    # print(mesh)

    # mesh.compute_vertex_normals()
    # export_mesh('age3d/models/monkey_cleaned.stl', mesh)

    # file_path = 'age3d/models/monkey_cleaned.stl'
    # mesh = import_mesh(file_path)
    # print(mesh)

    # vertices = find_minimum(mesh, 10)
    # vertices = find_minimum(mesh, 1000)
    # min_point_cloud = make_point_cloud(vertices, [255,0,0])

    # threshold = 80000

    # vertices = find_all_below(mesh, threshold)
    # below_minimum_cloud = make_point_cloud(vertices, [0,0,255])

    # vertices = find_all_above(mesh, threshold)
    # above_minimum_cloud = make_point_cloud(vertices, [0,255,0])

    # visualize([mesh, min_point_cloud, below_minimum_cloud, above_minimum_cloud])

    # lower_threshold = 80000
    # higher_threshold = 80000 * 2

    # vertices = find_all_between(mesh, lower_threshold, higher_threshold)
    # between_minimum_cloud = make_point_cloud(vertices, [0,0,255])

    # visualize([mesh, min_point_cloud, between_minimum_cloud])

    # vertices = find_neighbors(mesh, 0)
