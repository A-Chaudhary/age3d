import open3d as o3d
import numpy as np
import heapq

# print(o3d.__version__)


def import_mesh(file_path: str):
    """
    Imports stl file as Mesh

    Args:
        file_path (str): file path of stl file

    Returns:

    """
    mesh = o3d.io.read_triangle_mesh(file_path)
    return mesh


def export_mesh(file_path: str, mesh):
    """
    Export a mesh to a given file path using the open3d library.

    Args:
        file_path (str): The file path where the mesh will be saved.
        mesh: The mesh to be exported.

    Returns:
        None
    """
    o3d.io.write_triangle_mesh(file_path, mesh)
    return


def clean_mesh(mesh):
    """
    Merge the close vertices of a mesh to remove noise.

    Args:
        mesh: The mesh to be cleaned.

    Returns:
        None
    """
    mesh.merge_close_vertices(0.01)
    return


def mesh_details(mesh) -> tuple:
    """
    Retrieve details of a mesh in the form of numpy arrays for vertices and triangles.

    Args:
        mesh: The mesh for which the details are to be extracted.

    Returns:
        tuple: A tuple of two numpy arrays. The first array contains the vertices of the mesh
               and the second array contains the triangles of the mesh.
    """
    return (np.asarray(mesh.vertices), np.asarray(mesh.triangles))


def visualize(entries, show_wireframe=False) -> None:
    """
    Visualize a single mesh or a list of meshes using the open3d library.

    Args:
        entries: The mesh/meshes to be visualized. It can be a single mesh or a list of meshes.
        show_wireframe (bool): A flag to show/hide the wireframe of the mesh/meshes.

    Returns:
        None
    """
    if type(entries) is not list:
        o3d.visualization.draw_geometries([entries], mesh_show_wireframe=show_wireframe)
    else:
        o3d.visualization.draw_geometries(entries, mesh_show_wireframe=show_wireframe)
        return


def get_mask(mesh, idx):
    """
    Create a mask array for a specific vertex of the mesh.

    Args:
        mesh: The mesh for which the mask is to be created.
        idx: The index of the vertex for which the mask is to be created.

    Returns:
        np.ndarray: A boolean mask array with True value for the given index and False for all
                    other vertices of the mesh.
    """
    mask = np.full(np.asarray(mesh.vertices).shape[0], False)
    mask[idx] = True
    return mask


def find_minimum(mesh, k: int = 1, idx_mask=[]):
    """
    Find the k number of vertices having minimum z-coordinate of a mesh.

    Args:
        mesh (open3d.geometry.TriangleMesh): The input mesh.
        k (int, optional):: The number of minimum vertices to be found.
        idx_mask (list, optional): A list of indices of vertices to be considered for finding minimum vertices.

    Returns:
        tuple: A tuple of two numpy arrays. The first array contains the indices of the minimum
               vertices and the second array contains the coordinates of the minimum vertices.
    """
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
    """
    Finds the maximum value(s) and corresponding index(s) in the z-coordinate of the mesh's vertices.

    Args:
        mesh (open3d.geometry.TriangleMesh): The input mesh.
        k (int, optional): The number of maximum values to return. Defaults to 1.
        idx_mask (list, optional): List of vertex indices to consider for the maximum search. Defaults to empty list.

    Returns:
        tuple: Two numpy arrays, one containing the index(s) of the maximum value(s) and the other containing
        the maximum value(s) in the z-coordinate of the mesh's vertices.
    """
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
    """
    Finds all the vertices below the given value in the z-coordinate.

    Args:
        mesh (open3d.geometry.TriangleMesh): The input mesh.
        value (float): The value below which to find vertices.
        inclusive (bool, optional): Whether to include vertices with value equal to the given value. Defaults to False.

    Returns:
        tuple: Two numpy arrays, one containing the indices and the other containing the vertices that are below the
        given value in the z-coordinate.
    """
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
    """
    Finds all the vertices above the given value in the z-coordinate.

    Args:
        mesh (open3d.geometry.TriangleMesh): The input mesh.
        value (float): The value above which to find vertices.
        inclusive (bool, optional): Whether to include vertices with value equal to the given value. Defaults to False.

    Returns:
        tuple: Two numpy arrays, one containing the indices and the other containing the vertices that are above the
        given value in the z-coordinate.
    """
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
    """
    Returns a NumPy array of vertices whose z-coordinate is between the given lower and higher values.

    Args:
        mesh (open3d.geometry.TriangleMesh): A triangle mesh object.
        lower_value (float): The lower bound of the z-coordinate.
        higher_value (float): The higher bound of the z-coordinate.

    Returns:
        np.ndarray: A NumPy array of vertices whose z-coordinate is between the given lower and higher values.
    """
    mesh_vertices_np = np.asarray(mesh.vertices)
    # print(mesh_vertices_np, type(mesh.vertices))

    res = []
    for vertex in mesh_vertices_np:
        if lower_value < vertex[2] < higher_value:
            res.append(vertex)
    return np.array(res).reshape((-1, 3))


def make_point_cloud(vertices, color):
    """
    Creates a point cloud object with the given vertices and color.

    Args:
        vertices (np.ndarray): A NumPy array of vertices.
        color (tuple): A tuple of RGB values (0-255).

    Returns:
        open3d.geometry.PointCloud: A point cloud object.
    """
    pc = o3d.geometry.PointCloud()
    pc.points = o3d.utility.Vector3dVector(vertices)
    pc.paint_uniform_color(np.array(color) / 255)
    return pc


def find_neighbors(mesh, index: int):
    """
    Returns the indices and coordinates of the neighboring vertices of the given vertex index.

    Args:
        mesh (open3d.geometry.TriangleMesh): A triangle mesh object.
        index (int): The index of the vertex.

    Returns:
        Tuple[np.ndarray, np.ndarray]: A tuple of two NumPy arrays
        representing the neighboring vertex indices and coordinates.
    """
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
    """
    Returns a new triangle mesh object obtained by subdividing the given mesh.

    Args:
        mesh (open3d.geometry.TriangleMesh): A triangle mesh object.
        iterations (int): The number of times to subdivide the mesh.

    Returns:
        open3d.geometry.TriangleMesh: A new triangle mesh object obtained by subdividing the given mesh.
    """
    return mesh.subdivide_midpoint(number_of_iterations=iterations)


def calculate_bounds_height(mesh):
    """
    Returns the minimum z-coordinate of the vertices at the boundary of the given mesh.

    Args:
        mesh (open3d.geometry.TriangleMesh): A triangle mesh object.

    Returns:
        float: The minimum z-coordinate of the vertices at the boundary of the given mesh.
    """
    mesh_vertices_np = np.asarray(mesh.vertices)
    min_x_vertex = mesh_vertices_np[np.argmin(mesh_vertices_np[:, 0])]
    max_x_vertex = mesh_vertices_np[np.argmin(mesh_vertices_np[:, 0])]
    min_y_vertex = mesh_vertices_np[np.argmin(mesh_vertices_np[:, 1])]
    max_y_vertex = mesh_vertices_np[np.argmin(mesh_vertices_np[:, 1])]

    return min(min_x_vertex[2], max_x_vertex[2], min_y_vertex[2], max_y_vertex[2])


def erode(mesh, iterations=2, erosion_lifetime=10):
    """
    Erodes the mesh using the particle deposition and erosion method.

    Args:
        mesh (open3d.geometry.TriangleMesh): The mesh to be eroded.
        iterations (int, optional): The number of iterations for the erosion process. Defaults to 2.
        erosion_lifetime (int, optional): The maximum number of times a vertex can be eroded. Defaults to 10.

    Returns:
        Tuple[np.ndarray, open3d.geometry.TriangleMesh]: A tuple containing the updated vertex
        indices and the eroded mesh.
    """
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
