[![Documentation Status](https://readthedocs.org/projects/nanomesh/badge/?version=latest)](https://nanomesh.readthedocs.io/en/latest/?badge=latest)
[![Linux](https://github.com/hpgem/nanomesh/actions/workflows/test_on_linux.yml/badge.svg)](https://github.com/hpgem/nanomesh/actions/workflows/test_on_linux.yml)
[![MacOS](https://github.com/hpgem/nanomesh/actions/workflows/test_on_macos.yaml/badge.svg)](https://github.com/hpgem/nanomesh/actions/workflows/test_on_macos.yaml)
[![Windows](https://github.com/hpgem/nanomesh/actions/workflows/test_on_windows.yaml/badge.svg)](https://github.com/hpgem/nanomesh/actions/workflows/test_on_windows.yaml)

# nanomesh

Creates 3d meshes from microscopy experimental data.

Documentation: https://nanomesh.readthedocs.io/en/latest/

## Installation

If you use conda, create a new environment:

```
conda create -n nanomesh python=3.9
conda activate nanomesh
```

Install nanomesh:

```
git clone https://github.com/hpgem/nanomesh.git
cd nanomesh
pip install .
```

Note, [to enable the IPython widgets](https://ipywidgets.readthedocs.io/en/latest/user_install.html#installation):

```
jupyter nbextension enable --py widgetsnbextension
```

Note, [if you are using Jupyter lab](https://github.com/InsightSoftwareConsortium/itkwidgets#installation):

```
jupyter labextension install @jupyter-widgets/jupyterlab-manager jupyter-matplotlib jupyterlab-datawidgets itkwidgets
```

### With pygalmesh (linux only)

To use some of the additional functionality depending on pygalmesh,
first install the dependencies for pygalmesh (CGAL and EIGEN3)

```
sudo apt-get install libcgal-dev libeigen3-dev
```

The instructions are the same as above, except specify `with_pygalmesh` as option
to trigger the installation of pygalmesh. Currently this installs
[our fork](https://github.com/hpgem/pygalmesh).

```
pip install .[with_pygalmesh]
```

### Development

Install `nanomesh` using the development dependencies:

`pip install -e .[develop]`

Running the tests:

`pytest`

Linting/checks:

`pre-commit`

Building the docs:

```
make html --directory docs
```


### License

Copyright (c) 2020,

Licensed under the Apache License, Version 2.0 (the \"License\"); you
may not use this file except in compliance with the License. You may
obtain a copy of the License at

<http://www.apache.org/licenses/LICENSE-2.0>

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an \"AS IS\" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

### Credits

This package was created with
[Cookiecutter](https://github.com/audreyr/cookiecutter) and the
[NLeSC/python-template](https://github.com/NLeSC/python-template).
