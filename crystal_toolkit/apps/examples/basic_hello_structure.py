# as explained in "preamble" section in documentation
import dash
import dash_html_components as html
import dash_core_components as dcc
import crystal_toolkit.components as ctc

app = dash.Dash()
ctc.register_app(app)

# create our crystal structure using pymatgen
from pymatgen import Structure, Lattice

structure = Structure(Lattice.cubic(4.2), ["Na", "K"], [[0, 0, 0], [0.5, 0.5, 0.5]])

# create the Crystal Toolkit component
structure_component = ctc.StructureMoleculeComponent(structure)

# add the component's layout to our app's layout
my_layout = html.Div([structure_component.layout()])

# as explained in "preamble" section in documentation
app.layout = ctc.crystal_toolkit_layout(my_layout)
if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
