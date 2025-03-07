import numpy as np
import pytest

from nanomesh import MeshContainer, Mesher3D, TetraMesh, TriangleMesh
from nanomesh.image2mesh._mesher3d import BoundingBox, pad


@pytest.fixture
def image_cube():
    from nanomesh import Volume

    data = np.ones([10, 10, 10], dtype=int)
    data[2:7, 2:7, 2:7] = 0

    return Volume(data)


@pytest.fixture
def mesh_box():
    """Box triangle mesh."""
    points = np.array([[0., 0., 0.], [10., 0., 0.], [0., 20., 0.],
                       [10., 20., 0.], [0., 0., 30.], [10., 0., 30.],
                       [0., 20., 30.], [10., 20., 30.]])
    cells = np.array([[0, 4, 6], [0, 6, 2], [5, 1, 3], [5, 3, 7], [0, 1, 5],
                      [0, 5, 4], [6, 7, 3], [6, 3, 2], [1, 0, 2], [1, 2, 3],
                      [4, 5, 7], [4, 7, 6]])

    return TriangleMesh(points=points, cells=cells)


@pytest.mark.parametrize('side,width, expected_bbox', (
    ('top', 5,
     BoundingBox(xmin=0.0, xmax=10.0, ymin=0.0, ymax=20.0, zmin=0.0,
                 zmax=35.0)),
    ('bottom', 5,
     BoundingBox(
         xmin=0.0, xmax=10.0, ymin=0.0, ymax=20.0, zmin=-5.0, zmax=30.0)),
    ('left', 10,
     BoundingBox(
         xmin=0.0, xmax=10.0, ymin=-10.0, ymax=20.0, zmin=0.0, zmax=30.0)),
    ('right', np.pi,
     BoundingBox(
         xmin=0.0, xmax=10.0, ymin=0.0, ymax=20 + np.pi, zmin=0.0, zmax=30.0)),
    ('front', 0.1,
     BoundingBox(
         xmin=-0.1, xmax=10.0, ymin=0.0, ymax=20.0, zmin=0.0, zmax=30.0)),
    ('back', 123,
     BoundingBox(
         xmin=0.0, xmax=133.0, ymin=0.0, ymax=20.0, zmin=0.0, zmax=30.0)),
))
def test_mesh3d_pad(mesh_box, side, width, expected_bbox):
    """Test mesh3d.pad function."""
    out = pad(mesh_box, side=side, width=width)

    assert len(out.points) == len(mesh_box.points) + 4
    assert len(out.cells) == len(mesh_box.cells) + 10

    bbox = BoundingBox.from_points(out.points)

    assert bbox == expected_bbox


def test_mesh3d_pad_no_width(mesh_box):
    """Test early return when width==0."""
    out = pad(mesh_box, side='top', width=0)

    assert out is mesh_box


def test_mesh3d_pad_invalid_side(mesh_box):
    """Test invalide keyword argument."""
    with pytest.raises(ValueError):
        _ = pad(mesh_box, side='FAIL', width=123)


@pytest.mark.parametrize('side,label,name,expected_labels', (
    ('left', None, None, {
        1: 633,
        2: 1729,
        3: 290
    }),
    ('front', 1, None, {
        1: 857,
        2: 1851
    }),
    ('back', 2, None, {
        1: 620,
        2: 1966
    }),
    ('left', 3, None, {
        1: 633,
        2: 1729,
        3: 290
    }),
    ('bottom', np.pi, None, {
        1: 608,
        2: 1794,
        3: 277
    }),
    ('right', 3, None, {
        1: 611,
        2: 1760,
        3: 300
    }),
    ('bottom', None, 'moo', {
        1: 608,
        2: 1794,
        3: 277
    }),
    ('bottom', None, 'background', {
        1: 885,
        2: 1794,
    }),
    ('bottom', None, 'X', {
        1: 608,
        2: 2071,
    }),
))
def test_pad_label(image_cube, side, label, name, expected_labels):
    """Test `label` parameter for `pad`."""
    mesher = Mesher3D(image_cube)
    mesher.generate_contour()

    mesher.pad_contour(side=side, width=1, label=label, name=name)
    mesh = mesher.tetrahedralize(opts='-pAq1.2')

    assert isinstance(mesh, MeshContainer)

    tetra_mesh = mesh.get('tetra')

    assert isinstance(tetra_mesh, TetraMesh)

    unique, counts = np.unique(tetra_mesh.labels, return_counts=True)

    labels = dict(zip(unique, counts))

    if pytest.OS_MATCHES_DATA_GEN:
        # https://github.com/hpgem/nanomesh/issues/144
        assert expected_labels == labels

    keys = tuple(tetra_mesh.field_to_number.keys())
    default_keys = ('background', 'X')

    if not name:
        assert keys == default_keys
    elif name in default_keys:
        assert keys == default_keys
    else:
        assert keys == default_keys + (name, )
