from openff.toolkit.utils.toolkits import (
    GLOBAL_TOOLKIT_REGISTRY,
    AmberToolsToolkitWrapper,
    RDKitToolkitWrapper,
)

from qcportal import PortalClient

from openff.toolkit.topology import Molecule, Topology
from openff.toolkit.typing.engines.smirnoff import ForceField

print(GLOBAL_TOOLKIT_REGISTRY.registered_toolkit_versions)

assert RDKitToolkitWrapper().is_available()
assert AmberToolsToolkitWrapper().is_available()

offmol = Molecule.from_smiles('CCO')
Molecule.from_rdkit(offmol.to_rdkit())
ff = ForceField('openff-1.0.0.offxml')
ff.create_openmm_system(offmol.to_topology())

client = PortalClient("https://api.qcarchive.molssi.org:443/")

# copied from cookbook, there's probably a lighter way to do this
# dummy check, which just cares about basic QCArchive import/usage
# https://docs.openforcefield.org/projects/toolkit/en/stable/users/molecule_cookbook.html
record = [*client.query_molecules(molecular_formula="C16H20N3O5")][-1]

