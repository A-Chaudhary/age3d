import open3d as o3d
import numpy as np
import heapq

# print(o3d.__version__)


def import_mesh(file_path: str):
    mesh = o3d.io.read_triangle_mesh(file_path)
    return mesh


def export_mesh(file_path: str, mesh):
    o3d.io.write_triangle_mesh(file_path, mesh)
    return


def clean_mesh(mesh):
    mesh.merge_close_vertices(0.01)
    return


def mesh_details(mesh) -> tuple:
    return (np.asarray(mesh.vertices), np.asarray(mesh.triangles))


def visualize(entries, show_wireframe=False) -> None:
    if type(entries) is not list:
        o3d.visualization.draw_geometries([entries], mesh_show_wireframe=show_wireframe)
    else:
        o3d.visualization.draw_geometries(entries, mesh_show_wireframe=show_wireframe)
        return


def get_mask(mesh, idx):
    mask = np.full(np.asarray(mesh.vertices).shape[0], False)
    mask[idx] = True
    return mask


def find_minimum(mesh, k: int = 1, idx_mask=[]):
    mesh_vertices_np = np.asarray(mesh.vertices)
    idx_mask = set(idx_mask)
    # print(mesh_vertices_np, type(mesh.vertices))

    heap: list = []
    for i, vertex in enumerate(mesh_vertices_np):
        if len(idx_mask) == 0:
            heapq.heappush(heap, (vertex[2], i, vertex))

        elif len(idx_mask) > 0 and i in idx_mask:
            heapq.heappush(heap, (vertex[2], i, vertex))

    return np.array([idx for (_, idx, _) in heapq.nsmallest(k, heap)]).reshape((-1, 1)), np.array(
        [vertex for (_, _, vertex) in heapq.nsmallest(k, heap)]
    ).reshape((-1, 3))


def find_maximum(mesh, k: int = 1, idx_mask=[]):
    mesh_vertices_np = np.asarray(mesh.vertices)
    idx_mask = set(idx_mask)
    # print(mesh_vertices_np, type(mesh.vertices))

    heap: list = []
    for i, vertex in enumerate(mesh_vertices_np):
        if len(idx_mask) == 0:
            heapq.heappush(heap, (vertex[2], i, vertex))

        elif len(idx_mask) > 0 and i in idx_mask:
            heapq.heappush(heap, (vertex[2], i, vertex))

    return np.array([idx for (_, idx, _) in heapq.nlargest(k, heap)]).reshape((-1, 1)), np.array(
        [vertex for (_, _, vertex) in heapq.nlargest(k, heap)]
    ).reshape((-1, 3))


def find_all_below(mesh, value: float, inclusive=False):
    mesh_vertices_np = np.asarray(mesh.vertices)
    # print(mesh_vertices_np, type(mesh.vertices))

    idx = []
    res = []
    if inclusive:
        for v, vertex in enumerate(mesh_vertices_np):
            if vertex[2] <= value:
                idx.append(v)
                res.append(vertex)
    else:
        for v, vertex in enumerate(mesh_vertices_np):
            if vertex[2] < value:
                idx.append(v)
                res.append(vertex)
    return np.array(idx), np.array(res).reshape((-1, 3))


def find_all_above(mesh, value: float, inclusive=False):
    mesh_vertices_np = np.asarray(mesh.vertices)
    # print(mesh_vertices_np, type(mesh.vertices))

    idx = []
    res = []
    if inclusive:
        for v, vertex in enumerate(mesh_vertices_np):
            if vertex[2] >= value:
                idx.append(v)
                res.append(vertex)
    else:
        for v, vertex in enumerate(mesh_vertices_np):
            if vertex[2] > value:
                idx.append(v)
                res.append(vertex)
    return np.array(idx), np.array(res).reshape((-1, 3))


def find_all_between(mesh, lower_value: float, higher_value: float) -> np.ndarray:
    mesh_vertices_np = np.asarray(mesh.vertices)
    # print(mesh_vertices_np, type(mesh.vertices))

    res = []
    for vertex in mesh_vertices_np:
        if lower_value < vertex[2] < higher_value:
            res.append(vertex)
    return np.array(res).reshape((-1, 3))


def make_point_cloud(vertices, color):
    pc = o3d.geometry.PointCloud()
    pc.points = o3d.utility.Vector3dVector(vertices)
    pc.paint_uniform_color(np.array(color) / 255)
    return pc


def find_neighbors(mesh, index: int):
    mesh_triangles_np = np.asarray(mesh.triangles)
    # print('Printing Tris')
    neighbors = set()
    for tri in mesh_triangles_np:
        if index in tri:
            for i in tri:
                neighbors.add(i)
    neighbors.remove(index)
    return np.array([*neighbors]), np.asarray(mesh.vertices)[np.array([*neighbors])]


def mesh_subdivision(mesh, iterations=1):
    return mesh.subdivide_midpoint(number_of_iterations=iterations)


def calculate_bounds_height(mesh):
    mesh_vertices_np = np.asarray(mesh.vertices)
    min_x_vertex = mesh_vertices_np[np.argmin(mesh_vertices_np[:, 0])]
    max_x_vertex = mesh_vertices_np[np.argmin(mesh_vertices_np[:, 0])]
    min_y_vertex = mesh_vertices_np[np.argmin(mesh_vertices_np[:, 1])]
    max_y_vertex = mesh_vertices_np[np.argmin(mesh_vertices_np[:, 1])]

    return min(min_x_vertex[2], max_x_vertex[2], min_y_vertex[2], max_y_vertex[2])


def erode(mesh, iterations=2, erosion_lifetime=10):
    # total_vertex_count = np.asarray(mesh.vertices).shape[0]

    vertices_idx, vertices = find_all_above(mesh, calculate_bounds_height(mesh), True)

    set_vertices_idx = set()
    for idx in vertices_idx:
        set_vertices_idx.add(idx)
    # print('set', set_vertices_idx)

    new_mesh = o3d.geometry.TriangleMesh()
    new_vertices = np.asarray(mesh.vertices)
    new_triangles = np.asarray(mesh.triangles)
    updated_vertices = []

    new_mesh.vertices = o3d.utility.Vector3dVector(new_vertices)
    new_mesh.triangles = o3d.utility.Vector3iVector(new_triangles)

    mesh_max_height = find_maximum(mesh)[1][0, 2]
    rng = np.random.default_rng(10)

    for iter_no in range(iterations):
        v_idx_curr = vertices_idx[int(rng.random() * vertices.shape[0])]
        print('Iter: ', iter_no, ', V_idx: ', v_idx_curr)

        lifetime = erosion_lifetime
        strength = 0.5
        while lifetime > 0:
            new_mesh.vertices = o3d.utility.Vector3dVector(new_vertices)
            neighbors_idx, _ = find_neighbors(new_mesh, v_idx_curr)
            v_idx_next = int(find_minimum(new_mesh, 1, neighbors_idx)[0])

            if v_idx_next not in vertices_idx:
                break

            # if #TODO Angle Calculations

            new_vertices[v_idx_curr, 2] -= (
                strength * abs(new_vertices[v_idx_next, 2] - new_vertices[v_idx_curr, 2]) / mesh_max_height
            )
            updated_vertices.append(v_idx_curr)

            lifetime -= 1
            strength *= 0.69
            v_idx_curr = v_idx_next

    new_mesh.vertices = o3d.utility.Vector3dVector(new_vertices)
    new_mesh.triangles = o3d.utility.Vector3iVector(new_triangles)
    return np.array(updated_vertices), new_mesh
