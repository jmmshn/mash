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

Usage

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


-----

To use ...
