from openff.toolkit import __version__
from openff.toolkit.topology import Molecule, Topology
from openff.toolkit.typing.engines.smirnoff import ForceField
from openff.toolkit.utils.toolkits import (
    GLOBAL_TOOLKIT_REGISTRY,
    AmberToolsToolkitWrapper,
    RDKitToolkitWrapper,
)

from packaging.version import Version
from qcportal import PortalClient


# partially safeguard against a malformed version number;
# 0.minor.patch and major.0.patch should be okay but not 0.0.patch
found_version = Version(__version__)
assert not (found_version.minor == 0 and found_version.major == 0)

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

