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
        mesh (open3d.geometry.TriangleMesh): Mesh to be processed.
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


def find_accessible(mesh, rain_direction):
    """
    Returns the indices and coordinates of the vertices accessible by a given angle of particles' direction.

    Args:
        mesh (open3d.geometry.TriangleMesh): The mesh to check.

        rain_direction (numpy.ndarray): The direction angle of the rain as a numpy array of shape (3,).
            If direction is [0,0,0], every vertex is chosen.

    Returns:
        Tuple[np.ndarray, np.ndarray]: A tuple of two NumPy arrays
        representing the neighboring vertex indices and coordinates.
    """
    rain_direction = np.asarray(rain_direction)
    # if rain_direction[2] == 0:
    #     return np.array([]), np.array([])
    raycast_angle = rain_direction * -1
    # print(raycast_angle, type(rain_direction))
    mesh_vertices_np = np.asarray(mesh.vertices)

    angle_np = np.full(mesh_vertices_np.shape, raycast_angle)
    ray_np = np.append(mesh_vertices_np, angle_np, axis=1)

    rays = o3d.core.Tensor(ray_np, dtype=o3d.core.Dtype.Float32)
    # print('ray', rays)
    rays[:, 0] += 1e-6 * np.sign(raycast_angle[0])
    rays[:, 1] += 1e-6 * np.sign(raycast_angle[1])
    rays[:, 2] += 1e-6 * np.sign(raycast_angle[2])

    # print('ray added', rays)
    raycasting_scene = o3d.t.geometry.RaycastingScene()
    mesh_legacy = o3d.t.geometry.TriangleMesh.from_legacy(mesh)
    _ = raycasting_scene.add_triangles(mesh_legacy)
    collision = raycasting_scene.cast_rays(rays)

    idx = []
    res = []
    collisions_hit = collision['t_hit'].numpy()
    # print('hit', collisions_hit)

    for v, vertex in enumerate(mesh_vertices_np):
        if collisions_hit[v] == np.inf:
            idx.append(v)
            res.append(vertex)
    return np.array(idx), np.array(res).reshape((-1, 3))


def erode(mesh: o3d.geometry.TriangleMesh, iterations: int = 2, erosion_lifetime: int = 10, direction=None, verbose=[]):
    """
    Erodes the mesh using the particle deposition and erosion method.

    Args:
        mesh (open3d.geometry.TriangleMesh): The mesh to be eroded.

        iterations (int, optional): The number of iterations for the erosion process. Defaults to 2.

        erosion_lifetime (int, optional): The maximum number of times a vertex can be eroded. Defaults to 10.

        direction (numpy.ndarray, optional): The direction of the rain as a numpy array of shape (3,).
            If not provided, the vertex mask is calculated from the mesh's bounding box. Defaults to None.

        verbose (list[str], optional): A list of strings containing information to be printed.
            Possible strings include 'all', 'vertex_progression', 'vector_direction',
            'vector_angle', 'ray', 'ray_scene', 'mesh', and 'collision'.
            Defaults to an empty list.

    Returns:
        Tuple[np.ndarray, open3d.geometry.TriangleMesh]: A tuple containing the updated vertex
        indices and the eroded mesh.

    The `verbose` argument takes a list of strings that specify what information should be printed.
        - 'all': Prints all below.
        - 'vertex_progression': Prints information about vertex triples.
        - 'vector_direction': Prints information about vector directions.
        - 'vector_angle': Prints information about vector angles.
        - 'ray': Prints information about the ray being casted.
        - 'ray_scene': Prints information about the raycasting scene.
        - 'mesh': Prints information about the mesh.
        - 'collision': Prints information about the collision detection.
    """
    # total_vertex_count = np.asarray(mesh.vertices).shape[0]
    verbose = set(verbose)
    if len(verbose) > 0:
        print('Printing with Settings:', verbose)

    if direction is None:
        vertices_idx, vertices = find_all_above(mesh, calculate_bounds_height(mesh), True)
    else:
        vertices_idx, vertices = find_accessible(mesh, rain_direction=direction)

    set_vertices_idx = set()
    for idx in vertices_idx:
        set_vertices_idx.add(idx)
    # print('set', set_vertices_idx)

    # Create New Mesh
    new_mesh = o3d.geometry.TriangleMesh()
    new_vertices = np.asarray(mesh.vertices)
    new_triangles = np.asarray(mesh.triangles)
    updated_vertices = []

    new_mesh.vertices = o3d.utility.Vector3dVector(new_vertices)
    new_mesh.triangles = o3d.utility.Vector3iVector(new_triangles)

    mesh_max_height = find_maximum(mesh)[1][0, 2]
    rng = np.random.default_rng(10)

    for iter_no in range(iterations):
        v_idx_curr = int(vertices_idx[int(rng.random() * vertices.shape[0])])
        print('Iter: ', iter_no, ', V_idx: ', v_idx_curr)

        lifetime = 0
        strength = 0.5
        v_idx_prev = None

        while lifetime < erosion_lifetime:
            neighbors_idx, _ = find_neighbors(new_mesh, v_idx_curr)
            v_idx_next = int(find_minimum(new_mesh, 1, neighbors_idx)[0])

            if v_idx_next not in vertices_idx and direction is None:
                break

            if v_idx_prev:
                if 'vertex_progression' in verbose or 'all' in verbose:
                    print(
                        'Vertex Triples:',
                        v_idx_prev,
                        v_idx_curr,
                        v_idx_next,
                        type(new_vertices[v_idx_prev]),
                        new_vertices[v_idx_prev],
                        new_vertices[v_idx_curr],
                        new_vertices[v_idx_next],
                    )
                vector_1 = new_vertices[v_idx_curr] - new_vertices[v_idx_prev]
                vector_2 = new_vertices[v_idx_next] - new_vertices[v_idx_curr]
                direction_1 = np.sign(vector_1)
                direction_2 = np.sign(vector_2)
                if 'vector_direction' in verbose or 'all' in verbose:
                    print(vector_1, vector_2, direction_1, direction_2, np.dot(direction_1, direction_2))

                if vector_2[2] > 0:
                    break

                vector_1[2] = 0
                vector_2[2] = 0
                norm_vector_1 = np.linalg.norm(vector_1)
                norm_vector_2 = np.linalg.norm(vector_2)
                angle = np.arccos(np.clip(np.dot(vector_1, vector_2) / (norm_vector_1 * norm_vector_2), -1.0, 1.0))
                if 'vector_angle' in verbose or 'all' in verbose:
                    print(vector_1, vector_2, direction_1, direction_2, np.dot(direction_1, direction_2), angle)
                    # if angle < 0:
                    #     print('Negative angle Calculated', angle)
                if angle > np.pi / 2:
                    if 'vector_angle' in verbose or 'all' in verbose:
                        print('Angle found > PI / 2', angle)
                    break

            ray = o3d.core.Tensor([[*new_vertices[v_idx_curr], 0, 0, 1]], dtype=o3d.core.Dtype.Float32)
            if 'ray' in verbose or 'all' in verbose:
                print('ray:', ray, 'vertex:', new_vertices[v_idx_curr])

            ray[0, 2] += 1e-6
            if 'ray' in verbose or 'all' in verbose:
                print('updated ray:', ray, 'vertex:', new_vertices[v_idx_curr])

            raycasting_scene = o3d.t.geometry.RaycastingScene()
            if 'ray_scene' in verbose or 'all' in verbose:
                print('scene:', raycasting_scene)

            if 'mesh' in verbose or 'all' in verbose:
                print('new mesh', new_mesh, type(new_mesh))
            new_mesh_legacy = o3d.t.geometry.TriangleMesh.from_legacy(new_mesh)
            if 'mesh' in verbose or 'all' in verbose:
                print('new mesh legacy', new_mesh_legacy, type(new_mesh_legacy))

            mesh_id = raycasting_scene.add_triangles(new_mesh_legacy)
            if 'mesh' in verbose or 'all' in verbose:
                print('mesh_id:', mesh_id)

            collision = raycasting_scene.cast_rays(ray)
            if 'collision' in verbose or 'all' in verbose:
                print(
                    'collision t_hit:',
                    collision['t_hit'],
                    type(collision['t_hit']),
                    collision['t_hit'].numpy(),
                    type(collision['t_hit'].numpy()),
                )

            if collision['t_hit'].numpy()[0] == np.inf:
                new_vertices[v_idx_curr, 2] -= (
                    strength * abs(new_vertices[v_idx_next, 2] - new_vertices[v_idx_curr, 2]) / mesh_max_height
                )
            else:
                new_vertices[v_idx_curr, 2] += (
                    strength * abs(new_vertices[v_idx_next, 2] - new_vertices[v_idx_curr, 2]) / mesh_max_height
                )

            new_mesh.vertices = o3d.utility.Vector3dVector(new_vertices)
            updated_vertices.append(v_idx_curr)

            lifetime += 1
            strength *= 0.69
            v_idx_prev = v_idx_curr
            v_idx_curr = v_idx_next

    if len(verbose) > 0:
        print('')

    new_mesh.vertices = o3d.utility.Vector3dVector(new_vertices)
    new_mesh.triangles = o3d.utility.Vector3iVector(new_triangles)
    return np.array(updated_vertices), new_mesh
