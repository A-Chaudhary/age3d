import open3d as o3d
import numpy as np
import heapq
# print(o3d.__version__)

def import_mesh(file_path):
    mesh = o3d.io.read_triangle_mesh(file_path)
    print(type(mesh))
    return mesh

def clean_mesh(mesh):
    mesh.merge_close_vertices(0.01)
    return

def mesh_details(mesh):
    print(np.asarray(mesh.vertices))
    print(np.asarray(mesh.triangles))

def visualize(entries):
    if type(entries) is not list:
        o3d.visualization.draw_geometries([entries])
    else:
        o3d.visualization.draw_geometries(entries)
        return

def find_minimum(mesh, k = 1):
    mesh_vertices_np = np.asarray(mesh.vertices)
    # print(mesh_vertices_np, type(mesh.vertices))
    
    heap = []
    i = 0
    for vertex in mesh_vertices_np:
        heapq.heappush(heap, (vertex[2] ,i, vertex))
        i+= 1
    return np.array([vertex for (_, _, vertex) in heapq.nsmallest(k, heap)]).reshape((-1, 3))

def find_all_below(mesh, value):
    mesh_vertices_np = np.asarray(mesh.vertices)
    # print(mesh_vertices_np, type(mesh.vertices))
    
    res = []
    for vertex in mesh_vertices_np:
        if vertex[2] < value:
            res.append(vertex)
    return np.array(res).reshape((-1, 3))

def find_all_above(mesh, value):
    mesh_vertices_np = np.asarray(mesh.vertices)
    # print(mesh_vertices_np, type(mesh.vertices))
    
    res = []
    for vertex in mesh_vertices_np:
        if vertex[2] > value:
            res.append(vertex)
    return np.array(res).reshape((-1, 3))

def find_all_between(mesh, lower_value, higher_value):
    mesh_vertices_np = np.asarray(mesh.vertices)
    # print(mesh_vertices_np, type(mesh.vertices))
    
    res = []
    for vertex in mesh_vertices_np:
        if  lower_value < vertex[2] < higher_value:
            res.append(vertex)
    return np.array(res).reshape((-1, 3))

def make_point_cloud(vertices, color):
    pc = o3d.geometry.PointCloud()
    pc.points = o3d.utility.Vector3dVector(vertices)
    pc.paint_uniform_color(np.array(color) / 255 )
    return pc

def find_neighbors(mesh, index:int):
    mesh_triangles_np = np.asarray(mesh.triangles)
    # print('Printing Tris')
    neighbors = []
    for tri in mesh_triangles_np:
        if index in tri:
            neighbors.append(tri)
    return np.array(neighbors).reshape(-1, 3)


def main():
    # file_path = 'models/monkey.stl'
    file_path = 'models/Mount_Fuji.stl'

    mesh = import_mesh(file_path)
    mesh.compute_vertex_normals()
    
    print(mesh)
    clean_mesh(mesh)
    print(mesh)

    mesh_details(mesh)


    # vertices = find_minimum(mesh, 10)
    vertices = find_minimum(mesh, 1000)
    min_point_cloud = make_point_cloud(vertices, [255,0,0])

    # threshold = 80000

    # vertices = find_all_below(mesh, threshold)
    # below_minimum_cloud = make_point_cloud(vertices, [0,0,255])

    # vertices = find_all_above(mesh, threshold)
    # above_minimum_cloud = make_point_cloud(vertices, [0,255,0])

    # visualize([mesh, min_point_cloud, below_minimum_cloud, above_minimum_cloud])

    lower_threshold = 80000
    higher_threshold = 80000 * 2

    vertices = find_all_between(mesh, lower_threshold, higher_threshold)
    between_minimum_cloud = make_point_cloud(vertices, [0,0,255])

    visualize([mesh, min_point_cloud, between_minimum_cloud])


    vertices = get_neighbors(mesh, 0)



if __name__ == "__main__":
    main()