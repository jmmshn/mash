===================
Jupyter Integration
===================

Crystal Toolkit offers integration with JupyterLab to
allow easy viewing of crystal structures and other Materials Project
data interactively.

Installation
------------

The in-notebook renderer requires `pythreejs` the detailed installation instructions are at https://github.com/jupyter-widgets/pythreejs:


Uisng `conda` (Recomended) 

```
conda install -c conda-forge pythreejs
```

Using `pip`:

```
pip install pythreejs
```

And then install the extension for jupyter notebooks

```
jupyter nbextension install --py --symlink --sys-prefix pythreejs
jupyter nbextension enable --py --sys-prefix pythreejs
```

Or for jupyter lab:

```
jupyter labextension install @jupyter-widgets/jupyterlab-manager 
jupyter labextension install jupyter-threejs
```

Usage
-----

Importing the viewer

```
from crystal_toolkit.helpers.pythreejs_renderer import view
```

The viewer can be used for any object with a implemented `get_scene` function.

```
view(structure)
```
