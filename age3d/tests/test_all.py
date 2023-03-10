import pytest
from age3d import import_mesh, clean_mesh, mesh_details, find_minimum, find_all_below, find_all_above, find_all_between
import numpy as np
import random

# from unittest.mock import patch


# @pytest.mark.dependency()
@pytest.mark.parametrize(('file_path'), ["age3d/models/monkey.stl", "age3d/models/monkey_cleaned.stl"])
def test_import_mesh(file_path):
    mesh = import_mesh(file_path)
    assert type(mesh).__name__ == "TriangleMesh"


# @pytest.mark.dependency(depends=[test_import_mesh])
@pytest.mark.parametrize(
    ('file_path', 'true_details'),
    [("age3d/models/monkey.stl", (2866, 968))],  # ,("age3d/models/monkey_cleaned.stl", (505, 968))],
)
def test_mesh_details(file_path, true_details):
    mesh = import_mesh(file_path)
    details = mesh_details(mesh)
    print(len(details[0]), true_details[0], len(details[1]), true_details[1])
    assert len(details[0]) == true_details[0] and len(details[1]) == true_details[1]


# @pytest.mark.dependency(depends=[test_import_monkey, test_mesh_details])
def test_clean_mesh():
    mesh = import_mesh("age3d/models/monkey.stl")
    details = mesh_details(mesh)
    clean_mesh(mesh)
    details_after_cleaning = mesh_details(mesh)
    assert len(details_after_cleaning[0]) == 505
    assert len(details_after_cleaning[1]) == 968
    assert len(details[1]) == len(details_after_cleaning[1])


@pytest.mark.parametrize(
    ('k'),
    # [pytest.param(-1, marks=pytest.mark.xfail(reason="invalid argument")),
    [(0), (1)],
)
def test_find_minimum(k):
    mesh = import_mesh("age3d/models/monkey_cleaned.stl")
    assert len(find_minimum(mesh, k)) == k


@pytest.mark.parametrize(
    ('k'),
    [(i) for i in range(-1, 2)],
)
def test_find_all_below(k):
    mesh = import_mesh("age3d/models/monkey_cleaned.stl")
    res = find_all_below(mesh, k)
    for vertex in res:
        assert vertex[2] < k


@pytest.mark.parametrize(
    ('k'),
    [(i) for i in range(-1, 2)],
)
def test_find_all_above(k):
    mesh = import_mesh("age3d/models/monkey_cleaned.stl")
    res = find_all_above(mesh, k)
    for vertex in res:
        assert vertex[2] > k


@pytest.mark.parametrize(
    ('k', 'inclusive'),
    [(random.randint(-100, 100), isAbove) for _ in range(2) for isAbove in [True, False]],
)
def test_find_below_and_above(k, inclusive):
    mesh = import_mesh("age3d/models/monkey_cleaned.stl")
    details = mesh_details(mesh)
    above = find_all_above(mesh, k, inclusive)
    below = find_all_below(mesh, k, not inclusive)

    assert len(above) + len(below) == len(details[0])


@pytest.mark.parametrize(
    ('k1', 'k2'),
    [(sorted([random.randint(-100, 100), random.randint(-100, 100)])) for _ in range(5)],
)
def test_find_below_between_above(k1, k2):
    mesh = import_mesh("age3d/models/monkey_cleaned.stl")
    details = mesh_details(mesh)
    below = find_all_below(mesh, k1, True)
    between = find_all_between(mesh, k1, k2)
    above = find_all_above(mesh, k2, True)

    assert len(above) + len(between) + len(below) == len(details[0])
