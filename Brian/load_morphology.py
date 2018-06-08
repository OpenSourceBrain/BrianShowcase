from brian2tools.nmlimport.nml import load_morphology, validate_morphology, load_morph_from_cells, ValidationException
from brian2tools.plotting.morphology import plot_morphology, plot_dendrogram
from os.path import abspath, dirname,join
from neuroml.loaders import NeuroMLLoader
import matplotlib.pyplot as plt



def get_nml_file(file):
    return NeuroMLLoader.load(abspath(file))

examples = {"../NeuroML2/pyr_4_sym.cell.nml", "../NeuroML2/L23_NoHotSpot.cell.nml"}

for example in examples:
    nml_obj = get_nml_file(join(dirname(abspath(__file__)), example))
    cell_obj = nml_obj.cells[0]
    morph_obj = cell_obj.morphology

    print("Loaded %s to NeuroML: %s"%(example, cell_obj.id))

    morphology = load_morphology(join(dirname(abspath(__file__)), example))

    print("Loaded %s to Brian: %s"%(example, cell_obj.id))

    plot_morphology(morphology, plot_3d=False, show_compartments=True,
                    show_diameter=True, colors=('red',))

    print("Plotted: %s"%(example))
    plt.figure()
    plot_dendrogram(morphology)

    print("Plotted dendrogram: %s"%(example))

    plt.show()

