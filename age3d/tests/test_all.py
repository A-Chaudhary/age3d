import pytest
import age3d
import open3d as o3d
import numpy as np
import random

# from unittest.mock import patch


# @pytest.mark.dependency()
@pytest.mark.parametrize(('file_path'), ["age3d/models/monkey.stl", "age3d/models/monkey_cleaned.stl"])
def test_import_mesh(file_path):
    mesh = age3d.import_mesh(file_path)
    assert type(mesh).__name__ == "TriangleMesh"


# @pytest.mark.dependency(depends=[test_import_mesh])
@pytest.mark.parametrize(
    ('file_path', 'true_details'),
    [("age3d/models/monkey.stl", (2866, 968))],  # ,("age3d/models/monkey_cleaned.stl", (505, 968))],
)
def test_mesh_details(file_path, true_details):
    mesh = o3d.geometry.TriangleMesh()
    vertices = np.load('age3d/tests/monkey_vertices.npy')
    triangles = np.load('age3d/tests/monkey_triangles.npy')
    mesh.vertices = o3d.utility.Vector3dVector(vertices)
    mesh.triangles = o3d.utility.Vector3iVector(triangles)

    details = age3d.mesh_details(mesh)
    print(len(details[0]), true_details[0], len(details[1]), true_details[1])
    assert len(details[0]) == true_details[0] and len(details[1]) == true_details[1]


# @pytest.mark.dependency(depends=[test_import_monkey, test_mesh_details])
def test_clean_mesh():
    mesh = o3d.geometry.TriangleMesh()
    vertices = np.load('age3d/tests/monkey_vertices.npy')
    triangles = np.load('age3d/tests/monkey_triangles.npy')
    mesh.vertices = o3d.utility.Vector3dVector(vertices)
    mesh.triangles = o3d.utility.Vector3iVector(triangles)

    details = age3d.mesh_details(mesh)
    age3d.clean_mesh(mesh)
    details_after_cleaning = age3d.mesh_details(mesh)
    assert len(details_after_cleaning[0]) == 505
    assert len(details_after_cleaning[1]) == 968
    assert len(details[1]) == len(details_after_cleaning[1])


@pytest.mark.parametrize(
    ('idx'),
    # [pytest.param(-1, marks=pytest.mark.xfail(reason="invalid argument")),
    [np.array([0, 1, 2, 3]), np.array([0])],
)
def test_get_mask(idx):
    mesh = o3d.geometry.TriangleMesh()
    vertices = np.load('age3d/tests/monkey_vertices.npy')
    triangles = np.load('age3d/tests/monkey_triangles.npy')
    mesh.vertices = o3d.utility.Vector3dVector(vertices)
    mesh.triangles = o3d.utility.Vector3iVector(triangles)

    assert np.sum(age3d.get_mask(mesh, idx)) == idx.shape[0]


@pytest.mark.parametrize(
    ('k', 'idx_mask'),
    # [pytest.param(-1, marks=pytest.mark.xfail(reason="invalid argument")),
    [(0, []), (1, []), (0, np.array([1, 2, 3, 4])), (1, np.array([1, 2, 3, 4]))],
)
def test_find_minimum(k, idx_mask):
    mesh = o3d.geometry.TriangleMesh()
    vertices = np.load('age3d/tests/monkey_vertices.npy')
    triangles = np.load('age3d/tests/monkey_triangles.npy')
    mesh.vertices = o3d.utility.Vector3dVector(vertices)
    mesh.triangles = o3d.utility.Vector3iVector(triangles)

    assert len(age3d.find_minimum(mesh, k, idx_mask)[0]) == k
    assert len(age3d.find_minimum(mesh, k, idx_mask)[1]) == k


@pytest.mark.parametrize(
    ('k', 'idx_mask'),
    # [pytest.param(-1, marks=pytest.mark.xfail(reason="invalid argument")),
    [(0, []), (1, []), (0, np.array([1, 2, 3, 4])), (1, np.array([1, 2, 3, 4]))],
)
def test_find_maximum(k, idx_mask):
    mesh = o3d.geometry.TriangleMesh()
    vertices = np.load('age3d/tests/monkey_vertices.npy')
    triangles = np.load('age3d/tests/monkey_triangles.npy')
    mesh.vertices = o3d.utility.Vector3dVector(vertices)
    mesh.triangles = o3d.utility.Vector3iVector(triangles)

    assert len(age3d.find_maximum(mesh, k, idx_mask)[0]) == k
    assert len(age3d.find_maximum(mesh, k, idx_mask)[1]) == k


@pytest.mark.parametrize(
    ('k'),
    [(i) for i in range(-1, 2)],
)
def test_find_all_below(k):
    mesh = o3d.geometry.TriangleMesh()
    vertices = np.load('age3d/tests/monkey_vertices.npy')
    triangles = np.load('age3d/tests/monkey_triangles.npy')
    mesh.vertices = o3d.utility.Vector3dVector(vertices)
    mesh.triangles = o3d.utility.Vector3iVector(triangles)

    res = age3d.find_all_below(mesh, k)[1]
    for vertex in res:
        assert vertex[2] < k


@pytest.mark.parametrize(
    ('k'),
    [(i) for i in range(-1, 2)],
)
def test_find_all_above(k):
    mesh = o3d.geometry.TriangleMesh()
    vertices = np.load('age3d/tests/monkey_vertices.npy')
    triangles = np.load('age3d/tests/monkey_triangles.npy')
    mesh.vertices = o3d.utility.Vector3dVector(vertices)
    mesh.triangles = o3d.utility.Vector3iVector(triangles)

    res = age3d.find_all_above(mesh, k)[1]
    for vertex in res:
        assert vertex[2] > k


@pytest.mark.parametrize(
    ('k', 'inclusive'),
    [(random.randint(-100, 100), isAbove) for _ in range(2) for isAbove in [True, False]],
)
def test_find_below_and_above(k, inclusive):
    mesh = o3d.geometry.TriangleMesh()
    vertices = np.load('age3d/tests/monkey_vertices.npy')
    triangles = np.load('age3d/tests/monkey_triangles.npy')
    mesh.vertices = o3d.utility.Vector3dVector(vertices)
    mesh.triangles = o3d.utility.Vector3iVector(triangles)

    details = age3d.mesh_details(mesh)
    above = age3d.find_all_above(mesh, k, inclusive)[1]
    below = age3d.find_all_below(mesh, k, not inclusive)[1]

    assert len(above) + len(below) == len(details[0])


@pytest.mark.parametrize(
    ('k1', 'k2'),
    [(sorted([random.randint(-100, 100), random.randint(-100, 100)])) for _ in range(5)],
)
def test_find_below_between_above(k1, k2):
    mesh = o3d.geometry.TriangleMesh()
    vertices = np.load('age3d/tests/monkey_vertices.npy')
    triangles = np.load('age3d/tests/monkey_triangles.npy')
    mesh.vertices = o3d.utility.Vector3dVector(vertices)
    mesh.triangles = o3d.utility.Vector3iVector(triangles)

    details = age3d.mesh_details(mesh)
    below = age3d.find_all_below(mesh, k1, True)[1]
    between = age3d.find_all_between(mesh, k1, k2)
    above = age3d.find_all_above(mesh, k2, True)[1]

    assert len(above) + len(between) + len(below) == len(details[0])


def test_make_point_cloud():
    mesh = o3d.geometry.TriangleMesh()
    vertices = np.load('age3d/tests/monkey_vertices.npy')
    triangles = np.load('age3d/tests/monkey_triangles.npy')
    mesh.vertices = o3d.utility.Vector3dVector(vertices)
    mesh.triangles = o3d.utility.Vector3iVector(triangles)

    pc = age3d.make_point_cloud(np.asarray(mesh.vertices), [255, 0, 0])
    assert type(pc).__name__ == "PointCloud"


def test_find_neighbors():
    mesh = o3d.geometry.TriangleMesh()
    vertices = np.load('age3d/tests/monkey_vertices.npy')
    triangles = np.load('age3d/tests/monkey_triangles.npy')
    mesh.vertices = o3d.utility.Vector3dVector(vertices)
    mesh.triangles = o3d.utility.Vector3iVector(triangles)
    v_idx, vertices = age3d.find_neighbors(mesh, 0)

    assert all(v_idx == [1, 2])


@pytest.mark.parametrize(('direction', 'output_len'), [(np.array([0, 0, 0]), 2866), (np.array([0, 0, -1]), 687)])
def test_find_accessible(direction, output_len):
    mesh = o3d.geometry.TriangleMesh()
    vertices = np.load('age3d/tests/monkey_vertices.npy')
    triangles = np.load('age3d/tests/monkey_triangles.npy')
    mesh.vertices = o3d.utility.Vector3dVector(vertices)
    mesh.triangles = o3d.utility.Vector3iVector(triangles)
    v_idx, vertices = age3d.find_accessible(mesh, rain_direction=direction)
    print('len', len(v_idx))
    assert len(v_idx) == output_len


@pytest.mark.parametrize(
    ('file_path', 'verbose', 'direction'),
    [
        ("age3d/models/monkey.stl", ['all'], None),
        ("age3d/models/monkey.stl", [], None),
        ("age3d/models/monkey.stl", [], np.array([0, 0, -1])),
    ],
)
def test_full_run(file_path, verbose, direction):
    mesh = age3d.import_mesh(file_path)
    mesh = age3d.mesh_subdivision(mesh, 2)
    _, new_mesh = age3d.erode(mesh, iterations=20, erosion_lifetime=10, direction=direction, verbose=verbose)

    assert all(np.asarray(mesh.triangles).flatten() == np.asarray(new_mesh.triangles).flatten())
