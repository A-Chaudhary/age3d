import open3d as o3d
import numpy as np
import heapq
# print(o3d.__version__)

def import_mesh(file_path:str):
    mesh = o3d.io.read_triangle_mesh(file_path)
    return mesh

def export_mesh(file_path:str, mesh):
    o3d.io.write_triangle_mesh(file_path, mesh)
    return

def clean_mesh(mesh):
    mesh.merge_close_vertices(0.01)
    return

def mesh_details(mesh)->tuple[np.ndarray, np.ndarray]:
    return (np.asarray(mesh.vertices), np.asarray(mesh.triangles))

def visualize(entries)->None:
    if type(entries) is not list:
        o3d.visualization.draw_geometries([entries])
    else:
        o3d.visualization.draw_geometries(entries)
        return

def find_minimum(mesh, k:int = 1)->np.ndarray:
    mesh_vertices_np = np.asarray(mesh.vertices)
    # print(mesh_vertices_np, type(mesh.vertices))
    
    heap = []
    i = 0
    for vertex in mesh_vertices_np:
        heapq.heappush(heap, (vertex[2] ,i, vertex))
        i+= 1
    return np.array([vertex for (_, _, vertex) in heapq.nsmallest(k, heap)]).reshape((-1, 3))

def find_all_below(mesh, value, inclusive = False)->np.ndarray:
    mesh_vertices_np = np.asarray(mesh.vertices)
    # print(mesh_vertices_np, type(mesh.vertices))
    
    res = []
    if inclusive:
        for vertex in mesh_vertices_np:
            if vertex[2] <= value:
                res.append(vertex)
    else:
        for vertex in mesh_vertices_np:
            if vertex[2] < value:
                res.append(vertex)
    return np.array(res).reshape((-1, 3))

def find_all_above(mesh, value:float, inclusive = False)->np.ndarray:
    mesh_vertices_np = np.asarray(mesh.vertices)
    # print(mesh_vertices_np, type(mesh.vertices))
    
    res = []
    if inclusive:
        for vertex in mesh_vertices_np:
            if vertex[2] >= value:
                res.append(vertex)
    else:
        for vertex in mesh_vertices_np:
            if vertex[2] > value:
                res.append(vertex)
    return np.array(res).reshape((-1, 3))

def find_all_between(mesh, lower_value:float, higher_value:float)->np.ndarray:
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

def find_neighbors(mesh, index:int)->np.ndarray:
    mesh_triangles_np = np.asarray(mesh.triangles)
    # print('Printing Tris')
    neighbors = []
    for tri in mesh_triangles_np:
        if index in tri:
            neighbors.append(tri)
    return np.array(neighbors).reshape(-1, 3)
